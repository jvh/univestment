import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';

import {Row, Col} from 'react-bootstrap';

import { Link } from 'react-router-dom';

const ResultCard = (props) => {



  const findWithAttr = (array, attr, value) => {
    for(var i = 0; i < array.length; i += 1) {
        if(array[i][attr] === value) {
            return i;
        }
    }
    return -1;
  }

  const renderUniLogo = (university) => {
    console.log(props.results_state.search.search_results.universities);
    var unis = props.results_state.search.search_results.universities;
    var uni = findWithAttr (unis, 'name', university);

    console.log(unis[uni]);

    if (unis[uni].logo !== null) {
      return (
        <img className="card-uni-logo" src={unis[uni].logo} alt={university}/>
      );
    }
    return (
      <p>{university}</p>
    );

  }

  const adzuna = props.data;

  const allResults = props.all_results;

  const img_url = adzuna.image_url;

  const maxLength = 150;

  var description = adzuna.description;

  if (description.length > maxLength) {
    description = description.substr(0,maxLength);
    var index = description.lastIndexOf(" ");
    description = description.substr(0,index) + " ...";
  }

  console.log(props);

  return (
    <div>
      <div className="spacer-sml">
      </div>
      <div className="row result results-bg rounded">
        <div className="col-sm-12 col-md-4">
          <div className="result-card">
            <Link to={{pathname:'/property', state:{form: props}}}>
              <img className="result-image" src={img_url} alt=""/>
            </Link>
          </div>
        </div>
        <div className="col-sm-12 col-md-8">
          <div className="row pad-top">
            <div className="col-9">
              <h3 className="align-left">{adzuna.title}</h3>
            </div>
            <div className="col-3">
              <h3 className="align-right">£{adzuna.sale_price}</h3>
              <p className="align-right">guide price</p>
            </div>
            <div className="col-9 description" style={{display:"inline-block"}}>
              <p style={{fontSize:"85%"}}>{description}
                <Link to={{pathname:'/property', state:{form: props}}}>
                  <a href={adzuna.redirect_url} target="_blank" rel="noopener noreferrer">(Read more...)</a>
                </Link>
              </p>
            </div>
            <div className="col-3">
              <h3 className="align-right">£{Math.round(props.investment.mortgage_return.potential_rent_profit/10)*10}</h3>
              <p className="align-right">PCM Cash Flow</p>
            </div>
          </div>

          <div className="row">
            <div className="align-left adzuna-text pad-hor pad-top col-6" style={{whiteSpace:"nowrap"}}>
              {
                renderUniLogo(adzuna.university)
              }
            </div>
            <div className="align-right adzuna-text pad-hor pad-top col-6" style={{whiteSpace:"nowrap"}}>
              <a href={adzuna.redirect_url} target="_blank" rel="noopener noreferrer" style={{position:"relative", top:"2px"}}>Properties by </a>
              <a href={adzuna.redirect_url} target="_blank" rel="noopener noreferrer">
                <img className="adzuna_logo" src={require("../img/adzuna_logo.jpg")} alt=""/>
              </a>
            </div>
          </div>
          <div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ResultCard;
