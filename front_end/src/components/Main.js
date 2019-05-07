import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { Col } from 'react-bootstrap';

import HomePage from '../pages/HomePage.js';
import BarPage from '../pages/BarPage.js';
import LinePage from '../pages/LinePage.js';


const Main = props => {

  // Usage: setBaseProps(Component)(props) -> component renderer with props baked in
  const setBaseProps = Component => props => routerProps =>
    <Component {...routerProps} {...props} />

  const homePageRenderer = setBaseProps(HomePage)(props);
  const barPageRenderer = setBaseProps(BarPage)(props);
  const linePageRenderer = setBaseProps(LinePage)(props);

  return (
    <main>
      <Col className="main">
        <Switch>
          <Route exact path='/' render={homePageRenderer} />
          <Route exact path='/line' render={linePageRenderer} />
          <Route exact path='/bar' render={barPageRenderer} />
          <Route exact path='/*' render={homePageRenderer} />
        </Switch>
      </Col>
    </main>
  );
}

export default Main;
