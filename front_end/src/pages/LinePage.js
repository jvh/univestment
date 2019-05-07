import React from 'react';
import Main from '../css/Main.css';

import BarChart from '../components/BarChart.js';

import LineData from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';



const LinePage = (props) => {
   return (
     <div className="App">
       <h1>Bar Chart</h1>
       <BarChart/>
     </div>
   );
}

export default LinePage;
