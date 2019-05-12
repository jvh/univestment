import React, { Component } from 'react';
import Main from '../css/Main.css';

import LineGraph from '../components/LineGraph.js';

import { BarData } from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';

import { Link } from 'react-router-dom';

import ApiUtils from '../utils/ApiUtils.js';

class PropertyPage extends Component {

  constructor (props) {
    super(props);
    this.state = {
      data: props.location.state.form
    }
  }

  componentDidMount () {
    console.log("Property")
    console.log(this.state.data);

  }

  render(){
    return (
      <div className="bg outer pad-top pad-bottom">
        <div className="results-bg container">
          <div className="row row-pad">
            <div className="col-sm-12 col-md-4">
              <div>
                <Link to={{pathname:'/property', state:{form: this.state.data}}}>
                  <img className="result-image" src={this.state.data.image_url} alt=""/>
                </Link>
              </div>
              <div>
                <h1 className="align-center">£{this.state.data.sale_price}</h1>
              </div>
            </div>
            <div className="col-sm-12 col-md-8">
              <div>
                <p style={{color:"gray", fontSize:"75%"}}>{this.state.data.display_name}</p>
              </div>
              <div className="description">
                <p style={{fontSize:"85%"}}>{this.state.data.description}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default PropertyPage;
