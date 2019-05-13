import React, { Component } from 'react';
import Main from '../css/Main.css';
import LineGraph from '../components/LineGraph.js';
import { BarData } from '../mocks/MockData.js';
import { Col, Row } from 'react-bootstrap';
import 'bootstrap/dist/css/bootstrap.css';
import { Link } from 'react-router-dom';
import ApiUtils from '../utils/ApiUtils.js';



class PropertyPage extends Component {

  constructor (props) {
    super(props);
    if (props.location.state === undefined){
      window.location = '/';
    }
    this.state = {
      data: props.location.state.form,
      adzuna: props.location.state.form.property.adzuna,
      search: props.location.state.form.search
    }
    console.log("PROPERTY PROPS");
    console.log(props);
  }

  componentDidMount () {
    console.log("Property")
    console.log(this.state.data);
  }

  back() {

  }

  render(){
    return (
      <div className="bg outer pad-top pad-bottom">
        <div className="results-bg container-small">
          <div className="row-pad">
            <div>

              <Link to={{pathname:'/search', state:{search:this.state.search}}}>
              <a style={{cursor:"pointer"}} onClick={this.back}>&lt;&lt; Back to Search Results</a>
              </Link>
              <br></br>
              <div className="row pad-top">
                <div className="col-10">
                  <h1 className="align-left">{this.state.adzuna.title}</h1>
                  <p style={{fontSize:"125%"}} className="align-left">{this.state.adzuna.location.display_name}</p>
                </div>
                <div className="col-2">
                  <h3 className="align-right">£{this.state.adzuna.sale_price}</h3>
                  <p className="align-right">guide price</p>
                </div>
              </div>
            </div>
          </div>
          <div>
            <a href={this.state.adzuna.redirect_url} target="_blank" rel="noopener noreferrer">
              <img className="property-image" src={this.state.adzuna.image_url} alt=""/>
            </a>
          </div>
          <div className="row row-pad">
            <div className="description">
              <p>{this.state.adzuna.description}</p>
              <a href={this.state.adzuna.redirect_url} target="_blank" rel="noopener noreferrer" style={{float:"right", display:"inline"}}>Read More...</a>
            </div>
          </div>
          <div className="pad-hor-both pad-top">
            <div className="overline pad-top-large">
              <div>
                <h1 className="align-center value-green" style={{fontSize:"350%"}}>£{this.state.data.property.market_value - this.state.adzuna.sale_price}</h1>
                <h3 className="align-center">Below Estimated Market Value</h3>
              </div>
            </div>
          </div>
          <div className="pad-hor-both" style={{textAlign:"justify"}}>
            <p className="align-center"> The market value for this area has been estimated at £{this.state.data.property.market_value} meaning that
            this property has a potential return of investment of up to £{this.state.data.property.market_value - this.state.adzuna.sale_price}
            </p>
          </div>

          <div className="pad-hor-both pad-top">
            <div>
              <h1 className="align-center value-green" style={{fontSize:"350%"}}>£650 PCM</h1>
              <h3 className="align-center">Average Rental in Local Area</h3>
            </div>
          </div>
          <div className="pad-hor-both" style={{textAlign:"justify"}}>
            <p className="align-center"> The market value for this area has been estimated at £{this.state.data.property.market_value} meaning that
            this property has a potential return of investment of up to £{this.state.data.property.market_value - this.state.adzuna.sale_price}
            </p>
          </div>
          <div className="graph">
            <LineGraph width="500" height="500"/>
          </div>

        </div>
      </div>
    );
  }
}

export default PropertyPage;
