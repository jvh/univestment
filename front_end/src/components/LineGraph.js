import React, {Component} from 'react';
import * as d3 from "d3";

import '../css/Graphs.css';

class LineGraph extends Component {

  constructor(props) {
    super(props);
    this.state = {
      historic:props.data.historic,
      predicted:props.data.predicted
    }
  }

  componentDidMount() {
    console.log("SERIES");
    console.log(this.props);

    var average = []

    var y = this.state.historic.y

    for (var i=0; i<y.length; i++) {
      if (i < 10) {
        average.push(y[i]);
      } else {
        average.push((y[i-9]+y[i-8]+y[i-7]+y[i-6]+y[i-5]+y[i-4]+y[i-3]+y[i-2]+y[i-1]+y[i])/10);
      }
    }
    console.log("MOVING");
    console.log(this.state.historic)
    console.log(y);
    console.log(average);
    this.setState({historic:{x:this.state.historic.x,
      y:average}});

    this.drawChart();
  }

  drawChart() {

    const data = [
      {
        label:"historic",
        x: this.state.historic.x,
        y: this.state.historic.y,
        c: "ff5a60"
      },
      {
        label:"predicted",
        x: this.state.predicted.x,
        y: this.state.predicted.y,
        c: "39ba28"
      }
    ];

    const node = this.node;

    // var margin = {top: 50, right: 50, bottom: 50, left: 50}
    //   , width = this.props.width - margin.left - margin.right // Use the window's width
    //   , height = this.props.width - margin.top - margin.bottom; // Use the window's height

    const width = this.props.width;
    const height = this.props.height;

    var margin = {top: 50, right: 50, bottom: 50, left: 50},
      innerwidth = width - margin.left - margin.right,
      innerheight = height - margin.top - margin.bottom ;

    // The number of datapoints
    var n = 21;

    var xScale = d3.scaleLinear()
        .range([0, innerwidth])
        .domain([ d3.min(data, function(d) { return d3.max(d.x) - 60; }),
                  d3.max(data, function(d) { return d3.max(d.x); }) ]) ;

    var yScale = d3.scaleLinear()
        .range([innerheight, 0])
        .domain([ d3.min(data, function(d) { return d3.min(d.y); }),
                  d3.max(data, function(d) { return d3.max(d.y); }) ]) ;


    // 7. d3's line generator
    var line = d3.line()
        .x(function(d, i) {
          return xScale(d[0]);
        })
        .y(function(d) {
          return yScale(d[1]);
        });

    // 1. Add the SVG to the page and employ #2
    var svg = d3.select(node).append("svg")
        .attr("width", innerwidth + margin.left + margin.right)
        .attr("height", innerheight + margin.top + margin.bottom)
        .attr("style", "display:block")
        .append("g")
        .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

    // 3. Call the x axis in a group tag
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + innerheight + ")")
        .call(d3.axisBottom(xScale)); // Create an axis component with d3.axisBottom

    // 4. Call the y axis in a group tag
    svg.append("g")
        .attr("class", "y axis")
        .call(d3.axisLeft(yScale)); // Create an axis component with d3.axisLeft

    var data_lines = svg.selectAll(".d3_xy_chart_line")
        .data(data)
        .enter().append("g")
        .attr("class", "d3_xy_chart_line") ;

    data_lines.append("path")
        .attr("class", "line")
        .attr("d", function(d) { return line(d3.zip(d.x, d.y)); })
        .style("stroke", function(d) {
          console.log("D");
          console.log(d);
          return d.c
        }) ;

    // 9. Append the path, bind the data, and call the line generator
    svg.append("path")
        .datum(data) // 10. Binds data to the line
        .attr("class", "line") // Assign a class for styling
        .attr("d", line); // 11. Calls the line generator

    // // 12. Appends a circle for each datapoint
    // svg.selectAll(".dot")
    //     .data(dataset)
    //   .enter().append("circle") // Uses the enter().append() method
    //     .attr("class", "dot") // Assign a class for styling
    //     .attr("cx", function(d, i) { return xScale(i) })
    //     .attr("cy", function(d) { return yScale(d.y) })
    //     .attr("r", 5)
    //       .on("mouseover", function(a, b, c) {
    //   			console.log(a)
    // 		})
    //       .on("mouseout", function() {  })

  }

  render(){
    return <svg  className="graph" ref={node => this.node = node} width={this.props.width} height={this.props.height}></svg>
  }
}

export default LineGraph;
