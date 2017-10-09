// dashboard: most recent upgrade events

var myVar = setInterval(myTimer, 5000);
function myTimer(){
Plotly.d3.csv("static/results/upgrade.csv", function(err, csvData1){
Plotly.d3.csv("static/results/downgrade.csv", function(err, csvData2){
  var x1 = [], y1 = [];
  for (var i=0; i<csvData1.length; i++) {
      row1 = csvData1[i];
      x1.push( row1['time']);
      y1.push( row1['count'] );
      }

      var trace1 = {
        x: x1, 
	y: y1,
        type: 'scatter',
        name: 'Downgrade',
        mode: 'lines',
        line: {color: '#1AA6B7'},
    };

  var x2 = [], y2 = [];
  for (var i=0; i<csvData2.length; i++) {
      row2 = csvData2[i];
      x2.push( row2['time']);
      y2.push( row2['count'] );
      }

      var trace2 = {
        x: x2,
        y: y2,
        type: 'scatter',
        name: 'Upgrade',
        mode: 'lines',
        line: {color: '#F487A9'},
    };


var data = [trace1, trace2];

var layout = {
  autosize: false,
  width: 1000,
  height: 700,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
  yaxis: {autorange: true},
  title: 'Membership Upgrade and Downgrade Over Time',
};

  Plotly.newPlot('membership', data, layout);

})
})



//second div

Plotly.d3.csv("static/results/newuser.csv", function(err, csvData1){
Plotly.d3.csv("static/results/cancel.csv", function(err, csvData2){
  var x1 = [], y1 = [];
  for (var i=0; i<csvData1.length; i++) {
      row1 = csvData1[i];
      x1.push( row1['time']);
      y1.push( row1['count'] );
      }

      var trace1 = {
        x: x1,
        y: y1,
        type: 'scatter',
        name: 'New User',
        mode: 'lines',
        line: {color: '#1AA6B7'},
    };

  var x2 = [], y2 = [];
  for (var i=0; i<csvData2.length; i++) {
      row2 = csvData2[i];
      x2.push( row2['time']);
      y2.push( row2['count'] );
      }

      var trace2 = {
        x: x2,
        y: y2,
        type: 'scatter',
        name: 'Cancellation',
        mode: 'lines',
        line: {color: '#F487A9'},
    };
//tobe continued
var data = [trace1, trace2];

var layout = {
  autosize: false,
  width: 1000,
  height: 700,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
  yaxis: {autorange: true},
  title: 'New User and Membership Cancellation',
};

  Plotly.newPlot('newandcancel', data, layout);

})
})


}
