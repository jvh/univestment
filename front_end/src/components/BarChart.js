import React, {Component} from 'react';
import * as d3 from "d3";
import '../css/Main.css';
import ColourUtils from '../utils/ColourUtils.js';

class BarChart extends Component {
  componentDidMount() {
    this.drawChart();
  }

  drawChart() {

    const data = this.props.data;

    const height = this.props.height;
    const width = this.props.width;

    var maxVal = Math.max( ...data );
    console.log (maxVal);

    var barMult = height / (maxVal+(maxVal/10))

    const svg = d3.select("body")
    .append("svg")
    .attr("width", width)
    .attr("height", height)
    .style("margin-left", 100);

    svg.selectAll("rect")
      .data(data)
      .enter()
      .append("rect")
      .attr("x", (d, i) => i * 70)
      .attr("y", (d, i) => 500 - barMult * d)
      .attr("width", 65)
      .attr("height", (d, i) => d * barMult)
      .attr("fill", ColourUtils.dark_blue);
  }

  render(){
    return <div id={"#" + this.props.id}></div>
  }
}

export default BarChart;
