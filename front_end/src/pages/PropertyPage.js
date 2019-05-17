import React, { Component } from 'react';
import Main from '../css/Main.css';
import LineGraph from '../components/LineGraphProp.js';
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
      adzuna: props.location.state.form.data,
      old_state: props.location.state.form.results_state
    }
  }

  findWithAttr(array, attr, value) {
    for(var i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
    return -1;
  }

  round(float) {
    return Math.round(float/100)*100;
  }


  xToMonths (data) {
    var i = 0;
    var year = 1995;
    var month = 3

    data.historic = { ...data.historic, month:[] };
    data.predicted = { ...data.predicted, month:[] };

    while (i < data.historic.x.length + data.predicted.x.length -1) {
      if (i < data.historic.x.length) {
        data.historic.month[i] = ''+ year + '-' + month + '-' + '01';
      } else {
        data.predicted.month[i-data.historic.x.length] = ''+ year + '-' + month + '-' + '01';
      }
      month++;
      if (month === 13) {
        month = 1;
        year++;
      }
      i++;
    }

    return data;
  }

  renderMarketValue = () => {
    if (this.state.data.investment.market_value > this.state.adzuna.sale_price) {
      return (
        <div>
          <div>
            <h1 className="align-center value-green" style={{fontSize:"350%"}}>£{this.round(this.state.data.investment.market_value - this.state.adzuna.sale_price)}</h1>
            <h3 className="align-center">Below Estimated Market Value</h3>
          </div>
          <div className="pad-hor-both" style={{textAlign:"justify"}}>
            <p className="align-center"> The market value for this area has been estimated at £{this.round(this.state.data.investment.market_value)} meaning that
              this property has a potential return of investment of up to £{this.round(this.state.data.investment.market_value - this.state.adzuna.sale_price)}
            </p>
          </div>
        </div>
      );
    } else {
      return
    }
  }

//<p style={{fontSize:"125%"}} className="align-left">{this.state.adzuna.location.display_name}</p>

  render(){

    const outcode = this.findWithAttr(this.state.old_state.search.search_results.outcodes, 'outcode', this.state.data.data.outcode);
    const data = this.state.old_state.search.search_results.outcodes[outcode];

    return (
      <div className="bg outer pad-top pad-bottom">
        <div className="results-bg container-small">
          <div className="row-pad">
            <div>

              <Link to={{pathname:'/search', state:{old_state:this.state.data.results_state}}}>
                <a style={{cursor:"pointer"}} onClick={this.back}>&lt;&lt; Back to Search Results</a>
              </Link>
              <br></br>
              <div className="row pad-top">
                <div className="col-10">
                  <h1 className="align-left">{this.state.adzuna.title}</h1>
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
            <div className="description pad-hor-both">
              <p>{this.state.adzuna.description}</p>
              <div className="align-right adzuna-text pad-top" style={{whiteSpace:"nowrap"}}>
                <a href={this.state.adzuna.redirect_url} target="_blank" rel="noopener noreferrer" style={{position:"relative", top:"4px"}}>Read more on &nbsp;</a>
                <a href={this.state.adzuna.redirect_url} target="_blank" rel="noopener noreferrer">
                  <img className="adzuna_logo" src={require("../img/adzuna_logo.jpg")} alt=""/>
                </a>
              </div>
            </div>
          </div>

          <div className="pad-hor-both pad-top">
            <div className="overline pad-top">
              <div>
                <h1 className="align-center value-green" style={{fontSize:"350%"}}>£{Math.round(this.state.data.investment.mortgage_return.potential_rent_profit)}</h1>
                <h3 className="align-center">Potential Cash Flow PCM</h3>
              </div>
              <div className="pad-hor-both" style={{textAlign:"justify"}}>
                <p className="align-center"> The average rental income for this area is approximately £{Math.round(this.state.data.investment.mortgage_return.rent)}, £{Math.round(this.state.data.investment.mortgage_return.potential_rent_profit)} more than the monthly mortgage payments.*
                </p>
              </div>
              {
                this.renderMarketValue()
              }
            </div>
          </div>

          <div className="pad-hor-both pad-top">
            <div className="graph-outer overline pad-top">
              <h1 className="align-center" style={{fontSize:"275%"}}>Market Value Prediction</h1>
              <LineGraph width={700} height={500} data={this.xToMonths(data)} xTitle="Month" yTitle="Sale Price" zoom={true}/>
            </div>
            <p className="pad-top pad-bottom" style={{fontSize:"67%"}}>*Average monthly payments based on 20 year mortgage at 3.9% with 25% deposit of displayed guide price.</p>
          </div>

        </div>
      </div>
    );
  }
}

export default PropertyPage;

// <LineGraph width={700} height={500} data={data}/>
//             <LineGraph width={700} height={500} data={this.state.data.historic_data.outcode}/>
