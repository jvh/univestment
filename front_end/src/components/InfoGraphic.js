import React, {Component} from 'react';
import Main from '../css/Main.css';

import BarChart from '../components/BarChart.js';
import ApiUtils from '../utils/ApiUtils.js';
import { BarData } from '../mocks/MockData.js';


import 'bootstrap/dist/css/bootstrap.css';

class InfoGraphic extends Component {

  constructor() {
    super()
    this.state = {
      data: null,
      error: null
    }
  }

  isLoading = () => this.state.data === null && !this.hasError();
  hasError = () => this.state.error !== null;

  componentDidMount() {
    this.fetchData();
  }

  handleGetDataSuccess = response => {
    this.setState({data: response.result.data});
  };

  getBarGraph(data) {
  }

  handleGetDataFailure = error => {
  };

  fetchData = () => {
    ApiUtils.getData()
      .then(this.handleGetDataSuccess)
      .catch(this.handleGetDataFailure);
  };

  render(){

    if (this.isLoading()){
      return (<div></div>)
    }

    if (this.hasError()) {
      return (<div></div>)
    }

    return (
      <div className="App">
        <h1>Bar Chart</h1>
        <BarChart data={this.state.data} height="500" width="700"/>
      </div>
    );

  }
}

export default InfoGraphic;
