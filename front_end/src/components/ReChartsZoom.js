import React, { PureComponent } from 'react';
import {
  Label, LineChart, Legend, Line, CartesianGrid, XAxis, YAxis, Tooltip, ReferenceArea,
} from 'recharts';

const initialState = {
  left : 'dataMin',
  right : 'dataMax',
  refAreaLeft : '',
  refAreaRight : '',
  top : 'dataMax+1',
  bottom : 'dataMin-1',
  animation : true
};

export default class Example extends PureComponent {

  constructor(props) {
    super(props);
    console.log(props);
    var data = this.handleData (props.data);
    this.state = initialState
    this.state = { ...this.state,
      full_data:data,
      data:data
    }
    console.log(this.state);
  }

  getAxisYDomain (from, to, ref, offset) {
    console.log("domain");
	   const refData = this.state.full_data.slice(from-1, to);
    let [ bottom, top ] = [ refData[0][ref], refData[0][ref] ];
    refData.forEach( d => {
      if ( d[ref] !== undefined ){
  	    if ( d[ref] > top ) top = d[ref];
        if ( d[ref] < bottom ) bottom = d[ref];
      }
    });


    return [ (bottom|0) - offset, (top|0) + offset ]
  }

  zoom(){
    console.log("zoom");
   	let { refAreaLeft, refAreaRight, data } = this.state;

 		if ( refAreaLeft === refAreaRight || refAreaRight === '' ) {
     	this.setState( () => ({
       	refAreaLeft : '',
         refAreaRight : ''
       }) );
     	return;
     }

 		// xAxis domain
 	  if ( refAreaLeft > refAreaRight )
     		[ refAreaLeft, refAreaRight ] = [ refAreaRight, refAreaLeft ];

 		// yAxis domain
     const [ bottom, top ] = this.getAxisYDomain( refAreaLeft, refAreaRight, 'historic', 500 );

     this.setState( () => ({
       refAreaLeft : '',
       refAreaRight : '',
     	 data : this.state.full_data.slice(),
       left : refAreaLeft,
       right : refAreaRight,
       bottom: bottom, top: top
     } ) );
   };

 	zoomOut() {
    console.log("domain");
   	const { data } = this.state;
   	this.setState( () => ({
       data : this.state.full_data.slice(),
       refAreaLeft : 0,
       refAreaRight : 0,
       left : 'dataMin',
       right : 'dataMax',
       top : 'dataMax+1',
       bottom : 'dataMin'
     }) );
   }

  handleData(data){
    var out_data = [];
    var maxX = Math.max.apply(Math, data.predicted.x);
    console.log(data.predicted.x);
    console.log(maxX);

    for (var i=0; i<=maxX; i++){

      if (data.historic.x.includes(i)) {
        if (data.historic.x.indexOf(i) === data.historic.x.length - 1) {
          out_data.push({month:data.historic.x[data.historic.x.indexOf(i)], historic:Math.round(data.historic.y[data.historic.x.indexOf(i)]), predicted:Math.round(data.historic.y[data.historic.x.indexOf(i)])})
        } else {
            out_data.push({month:data.historic.x[data.historic.x.indexOf(i)], historic:Math.round(data.historic.y[data.historic.x.indexOf(i)])});
        }
      } else if (data.predicted.x.includes(i)) {
        out_data.push({month:data.predicted.x[data.predicted.x.indexOf(i)], predicted:Math.round(data.predicted.y[data.predicted.x.indexOf(i)])});
      }
    }
    console.log("OUTDATA");
    console.log(out_data);
    return out_data;
  }

  render() {
    const { data, barIndex, left, right, refAreaLeft, refAreaRight, top, bottom} = this.state;
    return (
      <LineChart width={700} height={400} data={data}
        onMouseDown = { (e) => {
            this.setState({refAreaLeft:e.activeLabel});
            console.log(e)
          }
        }
        onMouseMove = { (e) => {
              console.log("MOVE");
            this.setState({refAreaRight:e.activeLabel}) ;

          }
        }
        onMouseUp = { this.zoom.bind( this ) }>
            <XAxis
              allowDataOverflow={true}
              dataKey="month"
              domain={[this.state.left, this.state.right]}
              type="number"
            />
            <YAxis
              allowDataOverflow={true}
              domain={[this.state.bottom, this.state.top]}
              type="number"
             />
        <Tooltip />
        <Legend verticalAlign="top" height={36}/>
        <Line type="monotone" dataKey="historic" stroke="#F18805" dot={false}/>
        <Line type="monotone" dataKey="predicted" stroke="#F18805" strokeDasharray="3 3" dot={false}/>
        {
             (refAreaLeft && refAreaRight) ? (
             <ReferenceArea yAxisId="1" x1={refAreaLeft} x2={refAreaRight}  strokeOpacity={0.3} /> ) : null

           }
      </LineChart>
    );
  }
}
