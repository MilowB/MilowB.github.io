// Exécute le script d3 de chaque fichier de assets/charts dans le panneau correspondant.
(function () {
	'use strict';

	var SKIPPED_SELECTOR = /^(:root|html|body|main|h1|header|svg|p)(?![\w-])|^\.(canvas|hint)(?![\w-])/;

	function scopeCss(css, scope) {
		var doc = document.implementation.createHTMLDocument('');
		var style = doc.createElement('style');
		style.textContent = css;
		doc.head.appendChild(style);
		var output = [];
		Array.prototype.forEach.call(style.sheet.cssRules, function (rule) {
			if (rule.type !== CSSRule.STYLE_RULE) return;
			var selectors = rule.selectorText.split(',').map(function (s) { return s.trim(); })
				.filter(function (s) { return !SKIPPED_SELECTOR.test(s); })
				.map(function (s) {
					return /^\.tooltip(?![\w-])/.test(s) ? s.replace('.tooltip', '.chart-tooltip') : scope + ' ' + s;
				});
			if (selectors.length) output.push(selectors.join(',') + '{' + rule.style.cssText + '}');
		});
		return output.join('\n');
	}

	function scopedD3(host, tooltip, svgElement) {
		function resolve(selector) {
			if (selector === 'svg') return svgElement;
			return selector === '.tooltip' ? tooltip : host.querySelector(selector);
		}
		return Object.assign({}, d3, {
			select: function (target) { return d3.select(typeof target === 'string' ? resolve(target) : target); },
			selectAll: function (target) {
				return d3.selectAll(typeof target === 'string' ? host.querySelectorAll(target) : target);
			}
		});
	}

	function load(svgElement, index) {
		var host = svgElement.parentNode;
		var scope = 'chart-source-' + index;
		host.classList.add(scope);
		var fullscreenButton = host.querySelector('.chart-fullscreen');

		if (fullscreenButton) {
			fullscreenButton.addEventListener('click', function () {
				if (document.fullscreenElement === host) {
					document.exitFullscreen();
				} else if (host.requestFullscreen) {
					host.requestFullscreen();
				}
			});

			document.addEventListener('fullscreenchange', function () {
				var isFullscreen = document.fullscreenElement === host;
				fullscreenButton.setAttribute('aria-pressed', String(isFullscreen));
				fullscreenButton.setAttribute('aria-label', isFullscreen ? 'Quitter le plein écran' : 'Afficher le graphique en plein écran');
				fullscreenButton.title = isFullscreen ? 'Quitter le plein écran' : 'Afficher le graphique en plein écran';
				if (host._chartTooltip) {
					(isFullscreen ? host : document.body).appendChild(host._chartTooltip);
				}
			});
		}

		return fetch(svgElement.dataset.source).then(function (response) {
			if (!response.ok) throw new Error(response.status + ' ' + response.statusText);
			return response.text();
		}).then(function (html) {
			var source = new DOMParser().parseFromString(html, 'text/html');
			var sourceSvg = source.querySelector('svg');
			var script = source.querySelector('script:not([src])');
			if (!sourceSvg || !script) throw new Error('graphique introuvable dans le fichier');

			svgElement.setAttribute('viewBox', sourceSvg.getAttribute('viewBox'));
			var css = Array.prototype.map.call(source.querySelectorAll('style'), function (s) { return s.textContent; }).join('\n');
			var style = document.createElement('style');
			style.textContent = scopeCss(css, '.' + scope);
			document.head.appendChild(style);

			// Le tooltip est hors du panneau : celui-ci est transformé, ce qui fausse position: fixed.
			var tooltip = document.createElement('div');
			tooltip.className = 'chart-tooltip';
			tooltip.style.zIndex = '10000';
			document.body.appendChild(tooltip);
			host._chartTooltip = tooltip;

			svgElement.replaceChildren();
			new Function('d3', script.textContent)(scopedD3(host, tooltip, svgElement));
		}).catch(function (error) {
			var message = document.createElement('p');
			message.textContent = 'Impossible de charger le graphique (' + error.message + ').';
			host.appendChild(message);
		});
	}

	document.querySelectorAll('svg[data-source]').forEach(load);
})();
