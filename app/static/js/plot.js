// dashboard: most recent upgrade events


Plotly.d3.csv("static/results/upgrade.csv", function(err, csvData1){
Plotly.d3.csv("static/results/downgrade.csv", function(err, csvData2){
Plotly.d3.csv("static/results/cancel.csv", function(err, csvData3){
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
        name: 'Upgrade',
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
        name: 'Downgrade',
        mode: 'lines',
        line: {color: '#022D41'},
    };

  var x3 = [], y3 = [];
  for (var i=0; i<csvData3.length; i++) {
      row3 = csvData3[i];
      x3.push( row3['time']);
      y3.push( row3['count'] );
      }

      var trace3 = {
        x: x3,
        y: y3,
        type: 'scatter',
        name: 'Cancellation',
        mode: 'lines',
        line: {color: '#F487A9'},
    };

var data = [trace1, trace2, trace3];

var layout = {
  autosize: false,
  width: 1000,
  height: 600,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
  yaxis: {range: [0, 250]},
  title: 'Membership Upgrade, Downgrade and Cancellation  Over Time',
};
Plotly.newPlot('membership', data, layout);
})
})
})


// dashboard: most recent downgrade
Plotly.d3.csv("static/results/downgrade.csv", function(err, rows){
  function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var trace2 = {
  type: "scatter",
  mode: "lines",
  name: 'total',
  x: unpack(rows, 'time'),
  y: unpack(rows, 'count'),
  line: {color: '#2EABA5'}
}

var data = [trace2];

var layout = {
  autosize: false,
  width: 800,
  height: 300,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
  title: 'User Downgrade Over Time',
};

Plotly.newPlot('downgrade', data, layout);
})

// dashboard: most recent cancellation
Plotly.d3.csv("static/results/cancel.csv", function(err, rows){
  function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var trace3 = {
  type: "scatter",
  mode: "lines",
  name: 'total',
  x: unpack(rows, 'time'),
  y: unpack(rows, 'count'),
  line: {color: 'AB2B0E'}
}

var data = [trace3];

var layout = {
  autosize: false,
  width: 800,
  height: 300,
  margin: {
    l: 50,
    r: 50,
    b: 100,
    t: 100,
    pad: 4
  },
  title: 'Cancellation  Over Time',
};

Plotly.newPlot('cancellation', data, layout);
})


