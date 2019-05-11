import React, { Component } from 'react';
import Main from '../css/Main.css';
import HomePageSearch from '../components/HomePageSearch.js';

import 'bootstrap/dist/css/bootstrap.css';

class HomePage extends Component {

  constructor(props) {
    super(props);
  }

  render () {
    return (

      <div>
        <div className="homebackground">
          <div className="background-content">
            <div className="homeTitle container align-center">
              <h1>Univestment</h1>
            </div>
            <div className="centre">
              <div className="homeDiv">
                <div className="transparent container-xsmall more-rounded">
                  <HomePageSearch {...this.props}/>
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
