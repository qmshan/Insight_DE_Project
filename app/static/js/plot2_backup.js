// dashboard: most recent upgrade events
Plotly.d3.csv("static/results/batch_upgrade.csv", function(err, csvData1){
Plotly.d3.csv("static/results/batch_downgrade.csv", function(err, csvData2){
  var x1 = [], y1 = [];
  for (var i=0; i<csvData1.length; i++) {
      row1 = csvData1[i];
      x1.push( row1['gid'] );
      y1.push( row1['count'] );
      }

      var trace1 = {
        x: x1, 
	y: y1,
        name: 'Upgrade',
        type: 'bar'
        
    };

  var x2 = [], y2 = [];
  for (var i=0; i<csvData2.length; i++) {
      row1 = csvData2[i];
      x2.push( row1['gid'] );
      y2.push( row1['count'] );
      }

      var trace2 = {
        x: x2,
        y: y2,
        name: 'Downgrade2',
        type: 'bar'
    };

var data = [trace1,trace2];

var layout = {
  barmode: 'group',
  autosize: false,
  width: 600,
  height: 400,
  title: 'batch upgrade downgrade'
};
Plotly.newPlot('batch_upgrade_downgrade', data, layout);
})
})

// dashboard2:  User like&dislike events

// dashboard: most recent upgrade events
Plotly.d3.csv("static/results/batch_thumbsup.csv", function(err, csvData1){
Plotly.d3.csv("static/results/batch_thumbsdown.csv", function(err, csvData2){
  var x1 = [], y1 = [];
  for (var i=0; i<csvData1.length; i++) {
      row1 = csvData1[i];
      x1.push( row1['gid'] );
      y1.push( row1['count'] );
      }

      var trace1 = {
        x: x1, 
	y: y1,
        name: 'Likes',
        type: 'bar'
        
    };

  var x2 = [], y2 = [];
  for (var i=0; i<csvData2.length; i++) {
      row1 = csvData2[i];
      x2.push( row1['gid'] );
      y2.push( row1['count'] );
      }

      var trace2 = {
        x: x2,
        y: y2,
        name: 'Dislikes',
        type: 'bar'
    };

var data = [trace1,trace2];

var layout = {
  barmode: 'group',
  autosize: false,
  width: 600,
  height: 400,
  title: 'batch upgrade downgrade'
};
Plotly.newPlot('batch_like_dislike', data, layout);
})
})
