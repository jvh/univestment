import React, {Component} from 'react';
import Main from '../css/Main.css';

import BarChart from '../components/BarChart.js';
import ApiUtils from '../utils/ApiUtils.js';
import { BarData } from '../mocks/MockData.js';


import 'bootstrap/dist/css/bootstrap.css';

class BarPage extends Component {

  componentDidMount() {
    this.fetchData();
  }

  handleGetDataSuccess = response => {
    console.log(response);
  };

  handleGetDataFailure = error => {
    console.log(error);
  };

  fetchData = () => {
    ApiUtils.getData()
      .then(this.handleGetDataSuccess)
      .catch(this.handleGetDataFailure);
  }

  render(){

    const data = BarData

    return (
      <div className="App">
        <h1>Bar Chart</h1>
        <BarChart data={BarData} />
      </div>
    );
  }
}

export default BarPage;
