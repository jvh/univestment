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
      state_handled_data: data,
      startX:data.length - 84,
      clickedLeft:0,
      clickedRight:84
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
          out_data.push({x:data.historic.x[i], month:data.historic.month[i], historic:Math.round(data.historic.y[i]), predicted:Math.round(data.historic.y[i])});
        } else {
          out_data.push({x:data.historic.x[i], month:data.historic.month[i], historic:Math.round(data.historic.y[i])});
        }
      } else if (data.predicted.x[i-data.historic.x.length] !== undefined){
        out_data.push({x:data.predicted.x[i-data.historic.x.length], month:data.predicted.month[i-data.historic.x.length], predicted:Math.round(data.predicted.y[i-data.historic.x.length])});
      }
    }

    console.log("OUT DATA");
    console.log(out_data)

    return out_data;
  }

  reset(){
    const data = this.handleData (this.state.data);
    this.setState({
    clickedLeft:data.length-84,
    clickedRight:data.length}, () => this.zoom());
  }

  zoom(){
    if (this.state.reduced_data !== undefined && this.props.zoom === false) {

    } else {
      const data = this.state.data;
      var out_data = [];
      if (this.state.clickedLeft > this.state.clickedRight) {
        var temp = this.state.clickedLeft;
        this.setState({clickedLeft: this.state.clickedRight});
        this.setState({clickedRight: temp});
      }
      var maxX = this.state.clickedRight + this.state.startX + 1;
      var minX = this.state.clickedLeft  + this.state.startX;

      this.setState({left: minX, right: maxX})

      for (var i = minX; i < maxX; i++) {
        if (data.historic.x[i] !== undefined) {
          if (i == data.historic.x.length-1) {
            out_data.push({x:data.historic.x[i], month:data.historic.month[i], historic:Math.round(data.historic.y[i]), predicted:Math.round(data.historic.y[i])});
          } else {
            out_data.push({x:data.historic.x[i], month:data.historic.month[i], historic:Math.round(data.historic.y[i])});
          }
        } else if (data.predicted.x[i-data.historic.x.length] !== undefined){
          out_data.push({x:data.predicted.x[i-data.historic.x.length], month:data.predicted.month[i-data.historic.x.length], predicted:Math.round(data.predicted.y[i-data.historic.x.length])});
        }
      }
      this.setState({reduced_data:out_data, clickedLeft:'', clickedRight:''});
    }
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

  reset = () => {
    if (this.props.zoom) {
      return (
        <div className="align-right">
          <button onClick={this.reset.bind(this)}>Reset Zoom</button>
        </div>
      );
    } else return
  }

  render() {

    var data = this.state.reduced_data;

    if (data === undefined) {
      return <div></div>
    } else {

      return (
        <div>
        <div className="disable-select">
        <LineChart width={700} height={400}
          data={data.slice()}
          onMouseDown={e => {
            console.log(e);
            console.log(this.state);
            if (this.props.zoom === true){
              if (e != null ){
                this.setState({ clickedLeft: e.activeTooltipIndex })
              } else {
                this.setState({ clickedLeft: this.state.clickedLeft})
              }
            }
          }}
          onMouseMove={e => {
          console.log(this.state);
            if (this.state.clickedLeft && e != null && this.props.zoom === true){
              if (e.activeLabel != this.state.clickedLeft){
                this.setState({clickedRight: e.activeTooltipIndex }, () => {console.log(this.state)});
              }
            }
          }}
          onMouseUp={
            this.zoom.bind(this)
          }>
          <XAxis dataKey="month">
            <Label value={this.props.xTitle} offset={0} position="insideBottom" />
          </XAxis>
          <YAxis label={{ value:this.props.yTitle, angle: -90, position: 'insideLeft' }}/>
          <Tooltip />
          <Legend iconType="plainline" iconSize={30} verticalAlign="top" height={36}/>
          {
            this.renderHistoric()
          }
          {
            this.renderPredicted()
          }
          {
             (this.state.clickedLeft && this.state.clickedRight) ? (
             <ReferenceArea x1={this.state.state_handled_data[this.state.clickedLeft+this.state.startX].month} x2={this.state.state_handled_data[this.state.clickedRight + this.state.startX].month}  strokeOpacity={0.3} /> ) : null
          }
        </LineChart>
        </div>
        </div>
      );
    }
  }
}
