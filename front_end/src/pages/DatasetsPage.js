import React, { Component } from 'react';
import Main from '../css/Main.css';
import LineGraph from '../components/LineGraph.js';
import { BarData } from '../mocks/MockData.js';
import { Col, Row, Table } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import { Link } from 'react-router-dom';
import ApiUtils from '../utils/ApiUtils.js';



class DatasetsPage extends Component {

  constructor (props) {
    super(props);

  }


  render(){
    return (
      <div className="bg outer pad-top pad-bottom">
        <div className="results-bg container">
          <Table>
            <thead>
              <tr>
                <td>Dataset</td>
                <td>Link to Dataset</td>
                <td>Dataset License</td>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>
                  <h4>Historic House sales</h4>
                </td>
                <td>
                  <a
                  href="https://www.gov.uk/government/collections/price-paid-data"
                  target="_blank" rel="noopener noreferrer">Link to dataset</a>
                </td>

                <td>
                  <a
                  href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
                  target="_blank" rel="noopener noreferrer">License</a>
                </td>
              </tr>
              <tr>
                <td>
                  <h4>University Locations</h4>
                </td>

                <td>
                  <a
                  href="https://get-information-schools.service.gov.uk/"
                  target="_blank" rel="noopener noreferrer">Link to dataset</a>
                </td>

                <td>
                  <a
                  href="https://www.nationalarchives.gov.uk/doc/open-government-licence/version/3/"
                  target="_blank" rel="noopener noreferrer">License</a>
                </td>
              </tr>
              <tr>
                <td>
                  <h4>University Admissions</h4>
                </td>

                <td>
                  <a
                    href="https://www.ucas.com/data-and-analysis/undergraduate-statistics-and-reports/ucas-undergraduate-end-cycle-data-resources/applicants-and-acceptances-universities-and-colleges-2018"
                    target="_blank" rel="noopener noreferrer">Link to dataset</a>
                </td>
                <td>
                  <a
                    href=""
                    target="_blank" rel="noopener noreferrer">License</a>
                </td>
              </tr>
            </tbody>
          </Table>
          <div className="adzuna-text pad-hor pad-top" style={{whiteSpace:"nowrap"}}>
            <p>This website is not affiliated in any way with the institutions whose logos are displayed on advertisements. All advertisements are supplied by &nbsp;
              <a href="https://property.adzuna.co.uk" target="_blank" rel="noopener noreferrer">Adzuna</a>
            </p>
          </div>
        </div>
      </div>
    );
  }
}

export default DatasetsPage;

// <LineGraph width={700} height={500} data={data}/>
//             <LineGraph width={700} height={500} data={this.state.data.historic_data.outcode}/>
