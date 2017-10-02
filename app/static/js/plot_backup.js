// dashboard: most recent upgrade events


Plotly.d3.csv("static/results/upgrade.csv", function(err, rows){
  function unpack(rows, key) {
  return rows.map(function(row) { return row[key]; });
}

var trace1 = {
  type: "scatter",
  mode: "lines",
  name: 'total',
  x: unpack(rows, 'time'),
  y: unpack(rows, 'count'),
  line: {color: '#AB228D'}
}

var data = [trace1];

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
  title: 'User Upgrade  Over Time',
};
Plotly.newPlot('upgrade', data, layout);
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


