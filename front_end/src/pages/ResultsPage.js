import React, { Component } from 'react';
import Main from '../css/Main.css';

import LineGraph from '../components/LineGraph.js';

import { BarData } from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';

import ApiUtils from '../utils/ApiUtils.js';
import ResultsList from '../components/ResultsList.js';
import HomePageSearch from '../components/HomePageSearch.js';
import ResultsMap from '../components/ResultsMap.js';

class ResultsPage extends Component {

  constructor (props) {
    super(props);
    this.state = {
      search_results: null,  width: 0, height: 0
    }

    this.updateWindowDimensions = this.updateWindowDimensions.bind(this);
  }

  componentWillUnmount() {
    window.removeEventListener('resize', this.updateWindowDimensions);
  }

  updateWindowDimensions() {
    this.setState({ width: window.innerWidth, height: window.innerHeight });
  }

  componentDidMount () {
      console.log(this.props.location.state);
      console.log("RESULTS");
      this.updateWindowDimensions();
      window.addEventListener('resize', this.updateWindowDimensions);
      this.handleSubmit();
  }

  handleSubmit () {

    console.log("Submit")

    const { location, min_price, max_price, min_beds } = this.props.location.state.form;

    var search = { location };

    search = (min_price === "No min" || min_price === undefined) ? search : { ...search, min_price };
    search = (max_price === "No max" || max_price === undefined) ? search : { ...search, max_price };
    search = (min_price === "No min" || min_beds === undefined) ? search : { ...search, min_beds };

    console.log("search");

    ApiUtils.search(search)
    .then(this.handleSearchSuccess)
    .catch(this.handleSearchFailure);

  }

  handleSearchSuccess = response => {
    console.log(response);
    this.setState({search_results: response});
  }

  render(){

    if (this.state.search_results === null) {
      return (<div></div>);
    } else {
      if (this.state.width < 1830) {
        return (
          <div>
            <div className="container-small results-bg">
            <HomePageSearch {...this.props}/>
            </div>
            <ResultsMap results={this.state.search_results}/>
            <ResultsList results={this.state.search_results}/>
          </div>
        );
      } else {
        return (
          <div className="container-large">
            <div className="row">
              <div className="col-6">
                <ResultsList results={this.state.search_results}/>
              </div>
              <div className="col-6">
                <div className="container-small">
                  <div className="spacer-sml">
                  </div>
                  <div className="row-pad row result results-bg">
                    <div className="col-12">
                      <HomePageSearch {...this.props}/>
                    </div>
                  </div>
                </div>
                <div className="container-small">
                  <div className="spacer-sml">
                  </div>
                  <div className="row result results-bg">
                    <ResultsMap results={this.state.search_results}/>
                  </div>
                </div>
              </div>
            </div>
          </div>
        )
      }
    }
  }
}

export default ResultsPage;
