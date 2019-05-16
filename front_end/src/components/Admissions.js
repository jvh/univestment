import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import {Row, Col, Table} from 'react-bootstrap'
import { Link } from 'react-router-dom';
import { Collapse } from 'react-collapse';

import PieChart from './PieChart.js';
import LineGraph from './LineGraph.js';

const renderTableRow = (university) => {
  return (
    <tr>
      <td>{university.name}</td>
      <td className="align-center">{Math.round(university.admissions.predicted.y[0]/10)*10}</td>
      <td className="align-center">{Math.round(
        ((university.admissions.predicted.y[0] -
          university.admissions.historic.y[university.admissions.historic.y.length-1])
          /university.admissions.predicted.y[0])
        *1000)/10}%</td>
      <td className="align-center">{Math.round(university.admissions.predicted.y[1]/10)*10}</td>
      <td className="align-center">{Math.round(
        ((university.admissions.predicted.y[1] -
          university.admissions.predicted.y[0])
          /university.admissions.predicted.y[1])
        *1000)/10}%</td>
    </tr>
  )
}

class Admissions extends Component {

  constructor(props) {
    super(props);
    this.state={
      data:props.data,
      isOpened:false,
      pie_data:this.handleUniversityData(props.data)
    }
  }

  handleUniversityData(data){
    var out_data = [];

    console.log("ADMISSIONS DATA");
    console.log(data);
    data.forEach( function(uni) {
      out_data.push({name:uni.name, value:Math.round(uni.admissions.predicted.y[0])});
    });

    console.log(out_data)

    return out_data;
  }

  pieChartCallback(university) {

    var selected_university = null;

    this.props.data.forEach(function (uni) {
      if (uni.name.valueOf() == university.name.valueOf()) {
        console.log(uni.name);
        console.log(university.name);
        selected_university = uni;
      }
    })

    console.log(selected_university)

    this.setState({selectedUniversity:''}, () => this.setState({isOpened:true, selectedUniversity:selected_university}));

  }

  findWithAttr(array, attr, value) {
    for(var i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
    return -1;
  }

  renderLineGraph() {
    console.log("SELECTED UNI")
    if (this.state.selectedUniversity !== undefined && this.state.selectedUniversity !== '') {
      return (
        <div className="align-center line-inner pad-top-large">
          <h1>{this.state.selectedUniversity.name}</h1>
          <h4>Historic and Predicted Admssions</h4>
          <LineGraph width={700} height={500} data={this.state.selectedUniversity.admissions} zoom={false} xTitle="year" yTitle="Number of Admissions"/>
        </div>
      );
    }
    console.log(this.state.selectedUniversity)
    return
  }


  renderAdmissionsTable(){

    const universities = this.props.data;

    console.log(universities)

    var items = []

    universities.forEach(function(uni){
      items.push(renderTableRow(uni));
    });

    return items;

  }

  render() {
    if (this.state.pie_data === undefined) {
      return (<div></div>)
    } else {
    return (
      <div className="container-small">
        <div className="pad-hor-both">
          <div className="align-center pad-top-large ">
            <h1>University Statistics</h1>
          </div>
        </div>
        <div className="row justify-content-center pad-top">
          <div className="col-12">
            <PieChart data={this.state.pie_data} callback={this.pieChartCallback.bind(this)}/>
          </div>
          <div className="col-12 align-center pad-top">
          <h2 className="pad-bottom">Admissions</h2>
          <Table>
            <thead>
              <tr>
                <th>University</th>
                <th className="align-center">2019 Predictions</th>
                <th className="align-center">2019 % Incr.</th>
                <th className="align-center">2020 Predictions</th>
                <th className="align-center">2020 % Incr.</th>
              </tr>
            </thead>
            <tbody>
            {
              this.renderAdmissionsTable()
            }
            </tbody>
          </Table>
          </div>
          <Collapse isOpened={this.state.isOpened}>
            <div className="col-12 line-container">
              {
                this.renderLineGraph()
              }
            </div>
          </Collapse>

        </div>
      </div>
    );
  }
  }
};

export default Admissions;
