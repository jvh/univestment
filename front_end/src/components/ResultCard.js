import React from 'react';

import 'bootstrap/dist/css/bootstrap.css';

import {Row, Col} from 'react-bootstrap';

import { Link } from 'react-router-dom';

const ResultCard = (props) => {

  console.log(props);

  const img_url = props.image_url;

  const maxLength = 150;

  var description = props.description;

  if (description.length > maxLength) {
    description = description.substr(0,maxLength);
    var index = description.lastIndexOf(" ");
    description = description.substr(0,index) + " ...";
  }


  console.log(img_url);

  return (
    <div>
      <div className="spacer-sml">
      </div>
      <div className="row row-pad result results-bg rounded">
        <div className="col-sm-12 col-md-4">
          <div>
            <Link to={{pathname:'/property', state:{form: props}}}>
              <img className="result-image" src={img_url} alt=""/>
            </Link>
          </div>
          <div>
            <h1 className="align-center">£{props.sale_price}</h1>
          </div>
        </div>
        <div className="col-sm-12 col-md-8">
          <div>
            <p style={{color:"gray", fontSize:"75%"}}>{props.location.display_name}</p>
          </div>
          <div className="description">
            <p style={{fontSize:"85%"}}>{description}</p>
          </div>

          <div>
            <div className="col-sm">
              <a href={props.redirect_url} target="_blank" rel="noopener noreferrer">Properties by
              </a>
            </div>
            <div className="col-sm">
              <img className="adzuna_logo" src="../img/adzuna_logo.jpg" alt=""/>
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
