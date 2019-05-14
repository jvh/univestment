import React, { Component } from 'react';
import Main from '../css/Main.css';
import HomePageSearch from '../components/HomePageSearch.js';
import { Collapse } from 'react-collapse';

import 'bootstrap/dist/css/bootstrap.css';

class HomePage extends Component {

  constructor(props) {
    super(props);
    this.state = {
      isOpened: false
    }

    this.collapse = this.collapse.bind(this);
  }

  collapse() {
    this.setState({isOpened:!this.state.isOpened});
  }

  render () {
    return (

      <div>
        <div className="homebackground">
          <div className="grad">
            <div className="background-content">
              <Collapse isOpened={!this.state.isOpened}>
                <div className="logo-container">
                  <img className="title-logo" src={require('../img/drawing.svg')}/>
                </div>
                <div className="homeTitle container align-center">
                  <h1 className="title">PropertyMonopoly</h1>
                </div>
              </Collapse>
              <div className="centre">
                <div className="homeDiv">
                  <div className="transparent container-xsmall more-rounded">
                    <HomePageSearch collapse={this.collapse} isOpened={this.state.isOpened} {...this.props}/>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

    );
  }
}

export default HomePage;
