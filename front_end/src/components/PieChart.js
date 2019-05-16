import React, { PureComponent } from 'react';
import {
  Label, LineChart, Legend, Line, CartesianGrid, XAxis, YAxis, Tooltip, ReferenceArea, PieChart, Pie, Sector, Cell,
} from 'recharts';



const COLORS = ['#EAC435', '#FF5A60', '#345995', '#03CEA4', '#7FB7BE', '#EAC435', '#FF5A60', '#345995', '#03CEA4', '#7FB7BE'];

const renderActiveShape = (props) => {

  const RADIAN = Math.PI / 180;
  const {
    cx, cy, midAngle, innerRadius, outerRadius, startAngle, endAngle,
    fill, payload, percent, value, name
  } = props;
  const sin = Math.sin(-RADIAN * midAngle);
  const cos = Math.cos(-RADIAN * midAngle);
  const sx = cx + (outerRadius + 10) * cos;
  const sy = cy + (outerRadius + 10) * sin;
  const mx = cx + (outerRadius + 30) * cos;
  const my = cy + (outerRadius + 30) * sin;
  const ex = mx + (cos >= 0 ? 1 : -1) * 22;
  const ey = my;
  const textAnchor = cos >= 0 ? 'start' : 'end';

  return (
    <g>
      <Sector
        cx={cx}
        cy={cy}
        innerRadius={innerRadius}
        outerRadius={outerRadius}
        startAngle={startAngle}
        endAngle={endAngle}
        fill={fill}
      />
      <Sector
        cx={cx}
        cy={cy}
        startAngle={startAngle}
        endAngle={endAngle}
        innerRadius={outerRadius + 6}
        outerRadius={outerRadius + 10}
        fill={fill}
      />
      <path d={`M${sx},${sy}L${mx},${my}L${ex},${ey}`} stroke={fill} fill="none" />
      <circle cx={ex} cy={ey} r={2} fill={fill} stroke="none" />
      <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} textAnchor={textAnchor} fill="#333">{`${name}`}</text>
      <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} dy={18} textAnchor={textAnchor} fill="#999">
        {`Number of Admissions: ${value}`}
      </text>
      <text x={ex + (cos >= 0 ? 1 : -1) * 12} y={ey} dy={36} textAnchor={textAnchor} fill="#999">
        {`(Proportion: ${(percent * 100).toFixed(2)}%)`}
      </text>
    </g>
  );
};


export default class RePieChart extends PureComponent {

  constructor(props) {
    super(props);
    this.state={
      data:props.data,
      callback:props.callback
    }
  }

  static jsfiddleUrl = 'https://jsfiddle.net/alidingling/hqnrgxpj/';

  state = {
    activeIndex: 0,
  };

  onPieEnter = (data, index) => {
    this.setState({
      activeIndex: index,
    });
  };

  handleOnClick (e) {
    console.log("clicked")
    console.log(e);
    this.state.callback(e);
  }

  render() {
    return (
      <div  className="piechart">
      <PieChart width={800} height={400}>
        <Pie
          activeIndex={this.state.activeIndex}
          activeShape={renderActiveShape}
          data={this.state.data}
          cx={400}
          cy={200}
          outerRadius={120}
          fill="#8884d8"
          dataKey="value"
          onMouseEnter={this.onPieEnter}
           onClick={this.handleOnClick.bind(this)}
        >
        {
          this.state.data.map((entry, index) => <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />)
        }
        </Pie>
      </PieChart>
      </div>
    );
  }
}
