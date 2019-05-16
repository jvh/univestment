import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import {Row, Col} from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { Collapse } from 'react-collapse';

import PieChart from './PieChart.js';

const admissionsData = [
      { name: 'University of Southampton', value: 1000 },
      { name: 'Southampton Solent', value: 600 },
      { name: 'University of Winchester', value: 300 },
      { name: 'University of Portsmouth', value: 750 },
    ];




class Admissions extends Component {

  constructor(props) {
    super(props);
    this.state={
      data:props.data,
      isOpened:false,
      selectedUniversity:''
    }
  }

  pieChartCallback(university) {
    this.setState({isOpened:true, selectedUniversity:university.name});
    console.log(this.state.selectedUniversity);

  }

  render() {
    return (
      <div className="container-small">
        <div className="pad-hor-both">
          <div className="align-center pad-top-large underline">
            <h1>Key Statistics</h1>
          </div>
        </div>
        <div className="row">
          <div className="col-12">
            <PieChart data={admissionsData} callback={this.pieChartCallback.bind(this)}/>
          </div>
          <Collapse isOpened={this.state.isOpened}>
            <div className="col-12">
              <h1>{this.state.selectedUniversity}</h1>
            </div>
          </Collapse>
        </div>
      </div>
    );
  }
};

export default Admissions;
