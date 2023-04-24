function kmeans() {
    var s = "{{url_for('static/javascript',filename='k-means-clustering-data.json')}}";

    tablefilling(1, s);
}

function linearr() {
    var s = "{{url_for('static/javascript',filename='linear_regression.json')}}";
    tablefilling(1, s);
}

function classification() {
    var s = "{{url_for('static/javascript',filename='classfication_data_with_cluster_labels.json')}}";
    tablefilling(1, s);
}

function analysis() {
    var s = "{{url_for('static/javascript',filename='visualization(2014-21).json')}}";
    tablefilling(1, s);
}

function timeseries1() {
    s = "{{url_for('static/javascript',filename='timeseries1.json')}}";
    tablefilling(1, s);
}

function tablefilling(n, s) {


    function readTextFile(file, callback) {
        var rawFile = new XMLHttpRequest();
        rawFile.overrideMimeType("application/json");
        rawFile.open("GET", file, true);
        rawFile.onreadystatechange = function() {
            if (rawFile.readyState === 4 && rawFile.status == "200") {
                callback(rawFile.responseText);
            }
        }
        rawFile.send(null);
    }
    readTextFile(s, function(text) {
        var data = JSON.parse(text);
        var tableBody = '<table class="table shadow-soft rounded">'
        tableBody += '<tr>'
        console.log(data);
        if (s == "k-means-clustering-data.json") {
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
            tableBody += '<th>GREVIOUS HURT</th>'

            tableBody += '</tr>';

            data.forEach(function(d) {


                tableBody += '<tr><td class="border-0" scope="col">' + d.STATE.UT;

                tableBody += '<td>' + d.DISTRICT;
                tableBody += '<td>' + d.YEAR;
                tableBody += '<td>' + d.MURDER;
                tableBody += '<td>' + d["ATTEMPT TO MURDER"];;
                tableBody += '<td>' + d.RAPE;
                tableBody += '<td>' + d["KIDNAPPING & ABDUCTION"];
                tableBody += '<td>' + d.DACOITY;
                tableBody += '<td>' + d.ROBBERY;
                tableBody += '<td>' + d.THEFT;
                tableBody += '<td>' + d.HURT["GREVIOUS HURT"];



                tableBody += '</td></tr>';



            });
        } else if (s == "linear_regression.json") {
            tableBody += '<th>YEAR</th>';
            tableBody += '<th>TOTAL IPC</th>';
            tableBody += '<th>Crime rate(IPC per 100k)</th>';

            tableBody += '</tr>';

            data.forEach(function(d) {


                tableBody += '<tr><td class="border-0" scope="col">' + d.Year;
                tableBody += '<td>' + d["Total IPC"];
                tableBody += '<td>' + d["Crime rate(IPC per 100k)"];;
                tableBody += '</td></tr>';
            });
        } else if (s == "classfication_data_with_cluster_labels.json") {
            tableBody += '<th>CLUSTER</th>';
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
            tableBody += '<th>GREVIOUS HURT</th>'
            tableBody += '</tr>';

            data.forEach(function(d) {


                tableBody += '<tr><td class="border-0" scope="col">' + d.cluster;
                tableBody += '<td>' + d.STATE.UT;
                tableBody += '<td>' + d.DISTRICT;
                tableBody += '<td>' + d.YEAR;
                tableBody += '<td>' + d.MURDER;
                tableBody += '<td>' + d["ATTEMPT TO MURDER"];
                tableBody += '<td>' + d.RAPE;
                tableBody += '<td>' + d["KIDNAPPING & ABDUCTION"];
                tableBody += '<td>' + d.DACOITY;
                tableBody += '<td>' + d.ROBBERY;
                tableBody += '<td>' + d.THEFT;
                tableBody += '<td>' + d.HURT["GREVIOUS HURT"];
                tableBody += '</td></tr>';



            });
        } else if (s == "visualization(2014-21).json") {
            tableBody += '<th>STATE/UT</th>';
            tableBody += '<th>YEAR</th>';
            tableBody += '<th>MURDERS</th>';
            tableBody += '<th>KIDNAPPING</th>';
            tableBody += '<th>CRIMES AGAINST CHILDREN</th>';
            tableBody += '<th>CRIMES AGAINST SENIOR CITIZENS</th>';
            tableBody += '<th>CRIMES AGAINST WOMEN</th>';
            tableBody += '<th>CURROPTION</th>';
            tableBody += '<th>TOTAL_CRIMES</th>';
            tableBody += '<th>CYBER_CRIMES</th>';
            tableBody += '</tr>';

            data.forEach(function(d) {
                tableBody += '<tr><td class="border-0" scope="col">' + d["State/UT"];;
                tableBody += '<td>' + d.Year;
                tableBody += '<td>' + d.Murders;
                tableBody += '<td>' + d.Kidnapping;
                tableBody += '<td>' + d.Crimes_against_children;
                tableBody += '<td>' + d.Crimes_against_senior_citizen;
                tableBody += '<td>' + d.Crimes_against_women;
                tableBody += '<td>' + d.Corruption;
                tableBody += '<td>' + d.Total_Crimes;
                tableBody += '<td>' + d.Cyber_Crime;


                tableBody += '</td></tr>';



            });
        } else if (s == "timeseries1.json") {
            tableBody += '<th>S. NO.</th>';
            tableBody += '<th>DS</th>';
            tableBody += '<th>Y</th>';
            tableBody += '</tr>';

            data.forEach(function(d) {
                tableBody += '<tr><td class="border-0" scope="col">' + d[""];;
                tableBody += '<td>' + d.ds;
                tableBody += '<td>' + d.y;
                tableBody += '</td></tr>';



            });
        }


        tableBody += '<table>';
        // FINALLY ADD THE NEWLY CREATED TABLE WITH JSON DATA TO A CONTAINER.


        //        console.log(s, "helloooooo")

        var divContainer = document.getElementById("csv-data");
        divContainer.innerHTML = tableBody;
    });
}