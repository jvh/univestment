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
import Admissions from '../components/Admissions.js';

const MOCK = false;

class ResultsPage extends Component {

  constructor (props) {
    super(props);
    this.state = props.location.state.old_state;
    if (this.state === undefined) {
      this.state = {
        ...this.state,
        isLoading:true,
        filters:{sort:"Sort By", universities:"Select University", results_per_page:"Results per page"}
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
    search = (beds === "All" || beds === undefined) ? search : { ...search, beds };
    search = (distance === undefined) ? search : { ...search, distance };
    search = (km_away_from_uni === undefined) ? search : { ...search, km_away_from_uni };

    if (MOCK) {
      this.setState({search: {
          form:this.state.form,
          search_results: Filtered
        }
      }, () => this.filter());
    } else {
      ApiUtils.search(search)
      .then(this.handleSearchSuccess)
      .catch(this.handleSearchFailure);
    }

  }

  filter (filters) {


    const results = this.state.search.search_results;

    var filtered_results = [];


    if (this.state.filters.universities !== undefined && this.state.filters.universities !== "Select University") {

      var university = this.state.filters.universities;

      results.properties.forEach(function(result) {
        if(result.data.university === university) {
          filtered_results.push(result);
        }
      });
    } else {
      results.properties.forEach(function(result) {
        filtered_results.push(result);
      });
    }


    if (this.state.filters.sort !== undefined || this.state.filters.sort !== "Sort By") {
      if (this.state.filters.sort === "Price high to low") {
        filtered_results.sort((a, b) => (a.data.sale_price < b.data.sale_price) ? 1 : -1)
      } else
      if (this.state.filters.sort === "Price low to high") {
        filtered_results.sort((a, b) => (a.data.sale_price > b.data.sale_price) ? 1 : -1)
      }
    }

    this.setState({filtered_results: filtered_results, isLoading:false}, () => this.setState({isLoading: true}, () => this.setState({isLoading: false})));

  }

  handleSearchSuccess = response => {
    this.setState({search: {
        form:this.state.form,
        search_results: response
      }
    }, () => this.filter());
  }

  handleSearchFailure = response => {

  }

  filterCallback = filters => {
    this.setState({filters:{
      ...this.state.filters,
      [filters.name]: filters.value
    }}, () => this.filter());
  }

  render(){

    if(this.state.isLoading || this.state.filtered_results === undefined) {
      return (
        <LoadingSpinner/>
      )
    } else {
      if (this.state.width < 1830) {
        return (
          <div>
          <Filtering {...this.props} callback={this.filterCallback.bind(this)} filters={this.state.filters} universities={this.state.search.search_results.universities}/>
            <div className="container-small">
              <div className="spacer-sml">
              </div>
              <div className="row result results-bg">
                <ResultsMap  results={this.state.filtered_results} where={this.state.form.where} results_state={this.state}/>
              </div>
              <div className="spacer-sml">
              </div>
            </div>
            <div className="container-small">
              <div className="row result rounded results-bg">
                <Admissions data={this.state.search.search_results.universities}/>
              </div>
            </div>
            <ResultsList search={this.state.search} results_state={this.state} filtered_results={this.state.filtered_results}/>
          </div>
        );
      } else {
        return (
          <div>
          <Filtering {...this.props} callback={this.filterCallback.bind(this)} filters={this.state.filters} universities={this.state.search.search_results.universities}/>
          <div className="container-large">
            <div className="row">
              <div className="col-6">
                <ResultsList search={this.state.search} results_state={this.state} filtered_results={this.state.filtered_results}/>
              </div>
              <div className="col-6">
                <div className="container-small">
                  <div className="spacer-sml">
                  </div>
                  <div className="row result results-bg">
                    <ResultsMap results={this.state.filtered_results} where={this.state.form.where} results_state={this.state}/>
                  </div>
                  <div className="spacer-sml">
                  </div>
                </div>
                <div className="container-small">
                  <div className="row result rounded results-bg">
                    <Admissions data={this.state.search.search_results.universities}/>
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
