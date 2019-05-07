import React, {Component} from 'react';
import * as d3 from "d3";

class BarChart extends Component {
  componentDidMount() {
    this.drawChart();
  }

  drawChart() {

    const data = this.props.data;

    const height = this.props.height;

    var maxVal = Math.max( ...data );
    console.log (maxVal);

    var barMult = height / (maxVal+(maxVal/10))

    const svg = d3.select("body")
    .append("svg")
    .attr("width", 700)
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
      .attr("fill", "green")
  }

  render(){
    return <div id={"#" + this.props.id}></div>
  }
}

export default BarChart;
