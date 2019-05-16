import React, { PureComponent } from 'react';
import {
  Label, LineChart, Legend, Line, CartesianGrid, XAxis, YAxis, Tooltip, ReferenceArea,
} from 'recharts';

export default class LineGraph extends PureComponent {

  constructor(props) {
    super(props);
    var data = this.handleData (props.data);
    this.state = {
      data:props.data,
      clickedLeft:data.length-84,
      clickedRight:data.length
    }

  }

  componentDidMount(){
    this.zoom();
  }


  handleData(data){
    var out_data = [];
    var i = 0;
    var maxX = Math.max.apply(Math, data.predicted.x);
    var minX = Math.min.apply(Math, data.historic.x);

    for (var i = 0; i < maxX; i++) {
      if (data.historic.x[i] !== undefined) {
        if (i === data.historic.length-1) {
          out_data.push({month:data.historic.x[i], historic:Math.round(data.historic.y[i]), predicted:Math.round(data.historic.y[i])});
        } else {
          out_data.push({month:data.historic.x[i], historic:Math.round(data.historic.y[i])});
        }
      } else if (data.predicted.x[i-data.historic.x.length] !== undefined){
        out_data.push({month:data.predicted.x[i-data.historic.x.length], predicted:Math.round(data.predicted.y[i-data.historic.x.length])});
      }
    }
    return out_data;
  }

  zoom(){
    const data = this.state.data;
    var out_data = [];
    if (this.state.clickedLeft > this.state.clickedRight) {
      var temp = this.state.clickedLeft;
      this.setState({clickedLeft: this.state.clickedRight});
      this.setState({clickedRight: temp});
    }
    var maxX = this.state.clickedRight;
    var minX = this.state.clickedLeft-1;

    this.setState({left: minX, right: maxX})

    for (var i = minX; i < maxX; i++) {
      if (data.historic.x[i] !== undefined) {
        if (i == data.historic.x.length-1) {
          out_data.push({month:data.historic.x[i], historic:Math.round(data.historic.y[i]), predicted:Math.round(data.historic.y[i])});
        } else {
          out_data.push({month:data.historic.x[i], historic:Math.round(data.historic.y[i])});
        }
      } else if (data.predicted.x[i-data.historic.x.length] !== undefined){
        out_data.push({month:data.predicted.x[i-data.historic.x.length], predicted:Math.round(data.predicted.y[i-data.historic.x.length])});
      }
    }
    this.setState({reduced_data:out_data, clickedLeft:'', clickedRight:''});
  }

  renderHistoric() {
    var data = this.state.reduced_data;

    var historic = false;

    data.forEach (function(d) {
      if (d.historic !== undefined) {
        historic = true;
      }
    });

    if (historic) {
        return (
          <Line type="monotone" dataKey="historic" stroke="#F18805" dot={false}/>
        )
    }

    return
  }

  renderPredicted() {
    var data = this.state.reduced_data;

    var predicted = false;

    data.forEach (function(d) {
      if (d.predicted !== undefined) {
        predicted = true;
      }
    });

    if (predicted) {
        return (
          <Line type="monotone" dataKey="predicted" stroke="#F18805" strokeDasharray="4 4" dot={false}/>
        )
    }


  }

  render() {

    var data = this.state.reduced_data;

    if (data === undefined) {
      return <div></div>
    } else {

      return (

        <div className="disable-select">
        <LineChart width={700} height={400}
          data={data.slice()}
          onMouseDown={e => {
            if (e != null){
              this.setState({ clickedLeft: e.activeLabel })
            } else {
              this.setState({ clickedLeft: this.state.clickedLeft})
            }
          }}
          onMouseMove={e => {
            if (this.state.clickedLeft && e != null){
              if (e.activeLabel != this.state.clickedLeft){
                this.setState({clickedRight: e.activeLabel });
              }
            }
          }}
          onMouseUp={this.zoom.bind(this)}>
          <XAxis dataKey="month"/>
          <YAxis/>
          <Tooltip />
          <Legend verticalAlign="top" height={36}/>
          {
            this.renderHistoric()
          }
          {
            this.renderPredicted()
          }
          {
             (this.state.clickedLeft && this.state.clickedRight) ? (
             <ReferenceArea x1={this.state.clickedLeft} x2={this.state.clickedRight}  strokeOpacity={0.3} /> ) : null
          }
        </LineChart>
        </div>
      );
    }
  }
}
