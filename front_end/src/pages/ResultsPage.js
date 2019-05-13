import React, { Component } from 'react';
import Main from '../css/Main.css';

import LineGraph from '../components/LineGraph.js';

import { Filtered } from '../mocks/MockData.js';

import 'bootstrap/dist/css/bootstrap.css';

import ApiUtils from '../utils/ApiUtils.js';
import ResultsList from '../components/ResultsList.js';
import FilterResults from '../components/FilterResults.js';
import ResultsMap from '../components/ResultsMap.js';

import LoadingSpinner from '../components/LoadingSpinner.js';



class ResultsPage extends Component {

  constructor (props) {
    super(props);
    this.state = {
      width: 0, height: 0,
      isLoading: true
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
      this.setState({isLoading:true});
      console.log("RESULTS");
      console.log(this.props.location.state);
      console.log(this.props.location.state.search);
      this.updateWindowDimensions();
      window.addEventListener('resize', this.updateWindowDimensions);
      if (this.props.location.state === undefined) {
        window.location = '/';
      }
      if (this.props.location.state.search === undefined || this.props.location.state.search === null){
        console.log("HANDLE SUBMIT");
        this.handleSubmit();
      } else {
        console.log("SET STATE");
        console.log(this.props.location.state.search.form);
        this.setState({search:this.props.location.state.search, isLoading:false, form:this.props.location.state.search.form});
      }
  }

  handleSubmit () {

    console.log("Submit")

    const { where, price_min, price_max, beds, distance } = this.props.location.state.form;

    this.setState({form:this.props.location.state.form});

    var search = { where };

    search = (price_min === "No min" || price_min === undefined) ? search : { ...search, price_min };
    search = (price_max === "No max" || price_max === undefined) ? search : { ...search, price_max };
    search = (beds === "No min" || beds === undefined) ? search : { ...search, beds };
    search = (distance === undefined) ? search : { ...search, distance };

    console.log("search");

    ApiUtils.search(search)
    .then(this.handleSearchSuccess)
    .catch(this.handleSearchFailure);

  }

  handleSearchSuccess = response => {
    console.log(response);
    console.log(Filtered);
    this.setState({search: {
        form:this.state.form,
        search_results: Filtered
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
                <ResultsMap results={this.state.search.search_results} where={this.state.form.where}/>
              </div>
            </div>
            <ResultsList search={this.state.search}/>
          </div>
        );
      } else {
        return (
          <div className="container-large">
            <div className="row">
              <div className="col-6">
                <ResultsList search={this.state.search} s/>
              </div>
              <div className="col-6">
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
                    <ResultsMap results={this.state.search.search_results} where={this.state.form.where}/>
                  </div>
                  <div className="spacer-sml">
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
