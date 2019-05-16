import React from 'react';
import ReactDOM from 'react-dom';
import * as V from 'victory';
import { VictoryLine, VictoryChart, VictoryAxis,
        VictoryTheme, VictoryZoomContainer } from 'victory';

const data = [
  {quarter: 1, earnings: 13000},
  {quarter: 2, earnings: 16500},
  {quarter: 3, earnings: 14250},
  {quarter: 4, earnings: 19000}
];

class LineGraph extends React.Component {

  constructor(props){
    super(props);
    this.state = {
      data: this.handleData(props.data)
    }
  }

  handleData(data){
    var out_data = {historic:[], predicted:[]};
    var i = 0;
    for (i=data.historic.x.length-60; i<data.historic.x.length; i++) {
      out_data.historic.push({x:data.historic.x[i], y:Math.round(data.historic.y[i])});
    }
    out_data.predicted.push({x:data.historic.x[i-1], y:Math.round(data.historic.y[i-1])});
    for (var k=0; k<data.predicted.x.length; k++){
      out_data.predicted.push({x:data.predicted.x[k], y:Math.round(data.predicted.y[k])});
    }
    console.log("OUTDATA");
    console.log(out_data);
    return out_data;
  }

  render() {
    return (
      <VictoryChart  containerComponent={<VictoryZoomContainer/>}>
        <VictoryLine
          style={{
            data: { stroke: "#F18805" }
          }}
          data={this.state.data.historic}
          x="x"
          y="y"
        />
        <VictoryLine
          style={{
            data: { stroke: "#F18805", strokeDasharray: "3 3"}
          }}
          data={this.state.data.predicted}
          x="x"
          y="y"
        />
      </VictoryChart>
    )
  }
}

export default LineGraph;
