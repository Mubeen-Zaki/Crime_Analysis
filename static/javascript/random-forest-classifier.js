function ChangeLabel() {

    let text1 = document.getElementById("prediction-text");
    let text = text1.textContent;
    text = text.slice(0, -15);

    const startIndex = text.indexOf('[') + 2;
    const endIndex = text.indexOf(']') - 1;
    const zone = text.substring(0, startIndex-2);
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
        array.forEach( function(ele)
        {
            tableBody += '<td class="border-0" scope="col">' + ele+'</td>';
        });
        tableBody += '</tr>';
    text1.innerHTML='<b>'+zone+'</b>'+"     "+tableBody;
    console.log(table);




}