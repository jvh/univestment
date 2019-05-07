import React from 'react';
import Main from '../css/Main.css';

import BarChart from '../components/BarChart.js';

import { BarData } from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';

const BarPage = (props) => {
   return (
     <div className="App">
       <h1>Bar Chart</h1>
       <BarChart data={BarData} />
     </div>
   );
}

export default BarPage;
