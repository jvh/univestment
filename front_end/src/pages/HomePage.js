import React, { Component } from 'react';
import Main from '../css/Main.css';
import HomePageSearch from '../components/HomePageSearch.js';

import 'bootstrap/dist/css/bootstrap.css';

class HomePage extends Component {
  render () {
    return (

      <div>
        <div className="homebackground">
          <div className="background-content">
            <div className="centre">
              <div className="homeDiv">
                <HomePageSearch/>
              </div>
            </div>
          </div>
        </div>
      </div>

    );
  }
}

export default HomePage;
