function ChangeLabel() {

    let text1 = document.getElementById("prediction-text");
    let text = text1.textContent;
    text = text.slice(0, -15);

    const startIndex = text.indexOf('[') + 2;
    const endIndex = text.indexOf(']') - 1;
    const zone = text.substring(0, startIndex);
    let arr = text.substring(startIndex, endIndex + 1);
    arr = arr.slice(6);
    const array = arr.split(",");
    const table = document.createElement("table");

    const table = document.createElement("table");

    arr.forEach((item) => {
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.innerText = item;
        tr.appendChild(td);
        table.appendChild(tr);
    });

    array.forEach((item) => {
        const tr = document.createElement("tr");
        const td = document.createElement("td");
        td.innerText = item;
        tr.appendChild(td);
        table.appendChild(tr);
    });





}