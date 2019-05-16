import React, { Component } from 'react';
import Main from '../css/Main.css';

import LineGraph from '../components/LineGraph.js';

import { Filtered } from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';

import ApiUtils from '../utils/ApiUtils.js';
import ResultsList from '../components/ResultsList.js';
import FilterResults from '../components/FilterResults.js';
import ResultsMap from '../components/ResultsMap.js';
import Filtering from '../components/Filtering.js';
import LoadingSpinner from '../components/LoadingSpinner.js';

const MOCK = false;

class ResultsPage extends Component {

  constructor (props) {
    super(props);
    this.state = props.location.state.old_state;
    if (this.state === undefined) {
      this.state = {
        ...this.state,
        isLoading:true
      }
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
      this.updateWindowDimensions();
      window.addEventListener('resize', this.updateWindowDimensions);
      if (this.props.location.state === undefined) {
        window.location = '/';
      }
      if (this.props.location.state.old_state === undefined || this.props.location.state.old_state === null){
        this.state={isLoading: true};
        this.handleSubmit();
      }
  }

  handleSubmit () {

    const { where, price_min, price_max, beds, distance, km_away_from_uni } = this.props.location.state.form;

    this.setState({form:this.props.location.state.form});

    var radius_from = distance;

    var search = { where };

    search = (price_min === "No min" || price_min === undefined) ? search : { ...search, price_min };
    search = (price_max === "No max" || price_max === undefined) ? search : { ...search, price_max };
    search = (beds === "No min" || beds === undefined) ? search : { ...search, beds };
    search = (distance === undefined) ? search : { ...search, distance };

    if (MOCK) {
      this.setState({search: {
          form:this.state.form,
          search_results: Filtered
        }
      });
      this.setState({isLoading: false});
    } else {
      ApiUtils.search(search)
      .then(this.handleSearchSuccess)
      .catch(this.handleSearchFailure);
    }

  }

  handleSearchSuccess = response => {
    this.setState({search: {
        form:this.state.form,
        search_results: response
      }
    });
    this.setState({isLoading: false});
  }

  handleSearchFailure = response => {

  }

  render(){

    if(this.state.isLoading) {
      return (
        <LoadingSpinner/>
      )
    } else {

      console.log(this.state);
      if (this.state.width < 1830) {
        return (
          <div>
            <div className="container-small">
              <div className="spacer-sml">
              </div>
              <div className="row-pad row result rounded results-bg">
                <div className="col-12">
                  <FilterResults {...this.props}/>
                </div>
              </div>
            </div>
            <div className="container-small">
              <div className="spacer-sml">
              </div>
              <div className="row result results-bg">
                <ResultsMap  results={this.state.search.search_results} where={this.state.form.where} results_state={this.state}/>
              </div>
            </div>
            <ResultsList search={this.state.search} results_state={this.state}/>
          </div>
        );
      } else {
        return (
          <div>
          <Filtering/>
          <div className="container-large">
            <div className="row">
              <div className="col-6">
                <ResultsList search={this.state.search} results_state={this.state}/>
              </div>
              <div className="col-6">
                <div className="container-small">
                  <div className="spacer-sml">
                  </div>
                  <div className="row result results-bg">
                    <ResultsMap results={this.state.search.search_results} where={this.state.form.where} results_state={this.state}/>
                  </div>
                  <div className="spacer-sml">
                  </div>
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
