'''
-------------------------------
# TRAVAIL A REALISER
-------------------------------

Dans cet exercice vous devrez remplir les fonctions permettant de:
1) générer une clé partagée avec Diffie-Hellman
2) chiffrer un messages avec RSA
3) déchiffrer un message avec RSA


-------------------------------
# CONSIGNES
-------------------------------

/!\ Vous avez 1h20 + 25mn si nécessité de tier temps /!\ 


1) Remplissez votre prénom et votre nom en début de fichier dans les cases concernées

2) Remplissez les méthodes précédées de la mention #TODO (...)

3) Ne touchez pas aux en-têtes des fonctions (ne pas modifier les paramètres)

4) Respectez les formats de sortie des fonctions (les valeurs retournées). Des exemples sont
donnés pour vous aider à comprendre ce qui est attendu en sortie.

Il est également interdit de communiquer avec les autres étudiants.


-------------------------------
# Rendu
-------------------------------

Envoyer ce fichier à l'adresse:

mickael.bettinelli@univ-smb.fr

'''


######################################
#TODO
# Renseignez le champs suivants:
# Prénom: 
# Nom: 
######################################


###############################################################################################
###########################       Diffie-Hellman  6 points     ################################
###############################################################################################

#TODO
def diffieHellman():
    # coder les différentes étapes de Diffie-Hellman ici:
    # étape 0: générer deux entiers a et b aléatoirement (correspondant aux variables personnelles de Alice et Bob)
    # étape 1: choisir g et p, p doit être premier, et g plus petit que p
    # étape 2: calculer A (ou B, au choix)
    # étape 3: calculer K
    pass

###############################################################################################
################################      RSA   14 points    ######################################
###############################################################################################


#TODO
# Objectif: cette fonction calcule le pgcd de a et b
# Paramètres: a et b, les valeurs dont il faut calculer le pgcd
# Sortie: le plus grand dénominateur commun entre a et b
def pgcd(a, b):
    pass

#TODO
# Objectif: cette fonction recherche un nombre premier compris dans un intervalle
# Paramètres: borne_min, la borne basse de l'intervalle; borne_max, la borne haute de l'intervalle
# Sortie: une valeur qui est un nombre premier (ex: 3, 7, 11, etc.)
def generer_nombre_premier(borne_min, borne_max):
    pass

#TODO
# Objectif: cette fonction calcule e, la clef publique de RSA
# Paramètres: phi, le paramètre généré pour RSA
# Sortie: la clef publique e pour RSA
def generer_e_rsa(phi):
    pass

# Objectif: cette fonction calcule l'inverse d'un nombre a sur son ensemble Z/bZ
# Paramètres: a, le nombre dont on veut connaître l'inverse; b, l'ensemble sur lequel chercher l'inverse
# Sortie: l'inverse de a
def generer_inverse(a, b, x = 0, y = 1):
    x, y = y, x - (b // a) * y
    if b % a == 0:
        return x, y
    return generer_inverse(b % a, a, x, y)

# Objectif: cette fonction génère les clefs p, q, n, phi, e, et d pour RSA
# Paramètres: aucun
# Sortie: les clés p, q, n, phi, e, et d dans un dictionnaire
def generer_clefs_rsa():
    # Génère deux nombres premiers p et q
    p = generer_nombre_premier(pow(10, 3), pow(10, 6))
    q = generer_nombre_premier(pow(10, 3), pow(10, 6))
    n = p * q
    phi = (p - 1) * (q - 1)
    e = generer_e_rsa(phi)
    d = generer_inverse(e, phi)[0]
    # Si l'inverse de e (d) est d < 0 ou d > phi, le remettre dans l'intervalle [0, phi-1]
    d %= phi
    keys = {
        "p": p,
        "q": q,
        "phi": phi,
        "public": e,
        "private": d,
        "modulus": n
    }
    return keys

#TODO
# Objectif: cette fonction chiffre une lettre avec RSA
# Paramètres: lettre, la lettre à chiffrer; e et n, les clefs publiques
# Sortie: la lettre chiffré
def chiffrer_lettre_rsa(lettre, e, n):
    pass

#TODO
# Objectif: cette fonction déchiffre une seule lettre avec RSA
# Paramètres: lettre, la lettre à chiffrer; d et n, les clefs privées
# Sortie: la lettre chiffré
def dechiffrer_lettre_rsa(lettre, d, n):
    pass

#TODO
def rsa():
    # coder les différentes étapes du RSA ici:
    # étape 0: créer et intialiser une string qui servira de message à chiffrer
    # étape 1: générer les clés
    # étape 2: chiffrer le message (la string qui contient plusieurs lettres)
    # indice -> utiliser la fonction "chiffrer_lettre_rsa" pour chaque lettre du message à chiffer
    # étape 3: déchiffrer le message
    # indice -> utiliser la fonction "dechiffrer_lettre_rsa" pour chaque lettre du message à déchiffer
    # étape 4: vérifier que les messages chiffrés et déchiffrés sont identiques
    pass

if __name__ == '__main__':
    rsa()
    diffieHellman()
    


