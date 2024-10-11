
function openCSVFile(CSVfileName){
    $.ajax({
        type: "GET",
        url: CSVfileName,
        dataType: "text",
        success: processCSVContents
    });
}

function generateTable(dictionary) {  
    let table = '<table><tr>';  
    for (const [key, value] of Object.entries(dictionary)) {
        if(key != "commentaire")
            table += '<th>' + key + '</th>';  
    }
    table += "</tr><tr>"
    for (const [key, value] of Object.entries(dictionary)) {
        if(key != "commentaire")
            table += "<td>" + value + "</td>";
    }
    table += '</table>';
    if(dictionary["commentaire"] != undefined)
        table += "Commentaire : " + dictionary["commentaire"]
    return table;  
}  

function processCSVContents(text){
    var data = $.csv.toObjects(text);
    let etu_id = document.getElementById("etu_id");
    if (etu_id.value == "") {
        $('#resultat_evaluation').html("Il faut renseigner un numéro d'étudiant !");
    } else {
        res = null;
        for(i = 0; i < data.length; i++){
            if(data[i]["Num etu"] == etu_id.value) {
                res = data[i];
                break;
            }
        }
        if(res != null){
            to_print = generateTable(res)
            $('#resultat_evaluation').html(to_print);
        }
        else $('#resultat_evaluation').html("Numéro d'étudiant introuvable !"); 
    }
}