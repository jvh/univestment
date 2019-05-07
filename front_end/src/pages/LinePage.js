import React from 'react';
import Main from '../css/Main.css';

import LineGraph from '../components/LineGraph.js';

import { BarData } from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';



const LinePage = (props) => {
   return (
     <div className="App">
       <h1>Line Graph</h1>
       <LineGraph data={BarData} />
     </div>
   );
}

export default LinePage;
