import React, { PureComponent } from 'react';
import {
  Label, LineChart, Legend, Line, CartesianGrid, XAxis, YAxis, Tooltip, ReferenceArea,
} from 'recharts';

export default class Example extends PureComponent {

  constructor(props) {
    super(props);
    console.log(props);
    var data = this.handleData (props.data);
    this.state = {
      data:data
    }
  }

  handleData(data){
    var out_data = [];
    var i = 0;
    for (i=data.historic.x.length-60; i<data.historic.x.length; i++) {
      out_data.push({month:i, historic:Math.round(data.historic.y[i])});
    }
    out_data.push({month:data.predicted.x[0], historic:Math.round(data.predicted.y[0])});
    out_data.push({month:data.historic.x[i], predicted:Math.round(data.predicted.y[0])});
    for (var i=0; i<data.predicted.x.length; i++){
      out_data.push({month:data.predicted.x[i], predicted:Math.round(data.predicted.y[i])});
    }
    console.log("OUTDATA");
    console.log(out_data);
    return out_data;
  }

  render() {
    return (
      <LineChart width={700} height={400}
          data={this.state.data}
          onMouseDown={e => this.setState({ clickedLeft: e.activeLabel })}
          onMouseMove={e => this.setState({ clickedRight: e.activeLabel })}
          onMouseUp={this.zoom.bind(this)}>
        <XAxis dataKey="month"/>
        <YAxis/>
        <Tooltip />
        <Legend verticalAlign="top" height={36}/>
        <Line type="monotone" dataKey="historic" stroke="#8884d8" dot={false}/>
        <Line type="monotone" dataKey="predicted" stroke="#000000" dot={false}/>
      </LineChart>
    );
  }
}
