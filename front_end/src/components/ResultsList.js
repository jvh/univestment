
import React from 'react';
import ResultCard from '../components/ResultCard.js';
import { Col } from 'react-bootstrap';

import 'bootstrap/dist/css/bootstrap.css';

const ResultsList = (props) => {

  const renderResultsCard = result => {
      return (
        <ResultCard {...result} results_state={props.results_state}/>
      );
  }

  var results = Array.from(props.search.search_results)

  console.log(results);

  if (results && results.length > 0) {
    return (
      <div className="container-small">
        {
          results
            .map(renderResultsCard)
        }
        <div className="spacer-sml">
        </div>
      </div>

    );
  } else {
    return null;
  }
};


export default ResultsList;
