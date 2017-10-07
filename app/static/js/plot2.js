
// dashboard: most recent upgrade events

Plotly.d3.csv("static/results/batch_upgrade.csv", function(err, csvData1){
Plotly.d3.csv("static/results/batch_downgrade.csv", function(err, csvData2){
Plotly.d3.csv("static/results/batch_cancel.csv", function(err, csvData3){
  var xvalue = ['Group 1', 'Group2', 'Group3', 'Group4']
  var x1 = [], y1 = [];
  for (var i=0; i<csvData1.length; i++) {
      row1 = csvData1[i];
      x1.push( xvalue[i] );
      y1.push( row1['count'] );
      }

      var trace1 = {
        x: x1, 
	y: y1,
        name: 'Upgrade',
        type: 'bar',
	marker: {color: 'rgb(178,204,235)'}        
    };

  var x2 = [], y2 = [];
  for (var i=0; i<csvData2.length; i++) {
      row2 = csvData2[i];
      x2.push( xvalue[i] );
      y2.push( row2['count'] );
      }

      var trace2 = {
        x: x2,
        y: y2,
        name: 'Downgrade',
        type: 'bar',
	marker: {color: 'rgb(94, 94, 125)'}
    };

  var x3 = [], y3 = [];
  for (var i=0; i<csvData3.length; i++) {
      row3 = csvData3[i];
      x3.push( xvalue[i] );
      y3.push( row3['count'] );
      }

      var trace3 = {
        x: x3,
        y: y3,
        name: 'Cancellation',
        type: 'bar',
	marker: {color: 'rgb(246,162,188)' }
    };

var data = [trace1,trace2, trace3];

var layout = {
  barmode: 'group',
  autosize: false,
  width: 600,
  height: 400,
  title: 'Membership Upgrade, Downgrade and Cancellation'
};
Plotly.newPlot('batch_upgrade_downgrade', data, layout);
})
})
})

// dashboard2:  User like&dislike events
Plotly.d3.csv("static/results/batch_thumbsup.csv", function(err, csvData1){
Plotly.d3.csv("static/results/batch_thumbsdown.csv", function(err, csvData2){
  var xvalue = ['Group 1', 'Group2', 'Group3', 'Group4']
  var x1 = [], y1 = [];
  for (var i=0; i<csvData1.length; i++) {
      row1 = csvData1[i];
      x1.push( xvalue[i]);
      y1.push( row1['count'] );
      }

      var trace1 = {
        x: x1, 
	y: y1,
        name: 'Likes',
        type: 'bar',
	width: 0.25,
        marker: {
        color: 'rgb(178, 204, 235)'
        }
        
    };

  var x2 = [], y2 = [];
  for (var i=0; i<csvData2.length; i++) {
      row1 = csvData2[i];
      x2.push( xvalue[i] );
      y2.push( row1['count'] );
      }

      var trace2 = {
        x: x2,
        y: y2,
        name: 'Dislikes',
        type: 'bar',
	width: 0.25,
	marker: {
	color: 'rgb(94, 94, 125)'
	}
    };

var data = [trace1,trace2];

var layout = {
  barmode: 'group',
  autosize: false,
  width: 600,
  height: 400,
  title: 'Like and Dislike'
};
Plotly.newPlot('batch_like_dislike', data, layout);
})
})
