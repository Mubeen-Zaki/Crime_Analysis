function ChangeLabel() {

    let text1 = document.getElementById("prediction-text");
    let text = text1.textContent;
    text = text.slice(0, -15);

    const startIndex = text.indexOf('[') + 2;
    const endIndex = text.indexOf(']') - 1;
    let zone = text.substring(0, startIndex - 2);
    if (zone.includes('GREEN ZONE')) {
        zone = "<div style='margin-left:30%; color:green;font-size:50px; font-family:monsterrat;'>" + zone + "</div>";
    } else if (zone.includes('ORANGE ZONE')) {
        zone = "<div style='margin-left:30%; color:orange; font-size:50px; font-family:monsterrat;'>" + zone + "</div>";
    } else if (zone.includes('RED ZONE')) {
        zone = "<div style='margin-left:30%; color:red;font-size:50px; font-family:monsterrat;'>" + zone + "</div>";
    }


    let arr = text.substring(startIndex, endIndex + 1);
    arr = arr.slice(6);
    const array = arr.split(",");
    var tableBody = '<table class="table shadow-soft rounded">'
    tableBody += '<tr>'
    tableBody += '<th>STATE</th>';
    tableBody += '<th>DISTRICT</th>';
    tableBody += '<th>YEAR</th>';
    tableBody += '<th>MURDER</th>';
    tableBody += '<th>ATTEMPT TO MURDER</th>';
    tableBody += '<th>RAPE</th>';
    tableBody += '<th>KIDNAPPING & ABDUCTION</th>';
    tableBody += '<th>DACOITY</th>';
    tableBody += '<th>ROBBERY</th>';
    tableBody += '<th>THEFT</th>';
    tableBody += '<th>HURT</th>'

    tableBody += '</tr>';
    tableBody += '<tr>';
    array.forEach(function(ele) {
        tableBody += '<td class="border-0" scope="col">' + ele + '</td>';
    });
    tableBody += '</tr>';
    text1.innerHTML = '<b>' + zone + '</b>' + "<br><br><br><br><br><br><br><br><br>    " + tableBody;
    console.log(table);




}