import React from 'react';
import { Switch, Route } from 'react-router-dom';
import { Col } from 'react-bootstrap';

import HomePage from '../pages/HomePage.js';
import ResultsPage from '../pages/ResultsPage.js';
import PropertyPage from '../pages/PropertyPage.js';
import DatasetsPage from '../pages/DatasetsPage.js';


const Main = props => {

  // Usage: setBaseProps(Component)(props) -> component renderer with props baked in
  const setBaseProps = Component => props => routerProps =>
    <Component {...routerProps} {...props} />

  const homePageRenderer = setBaseProps(HomePage)(props);
  const resultsPageRenderer = setBaseProps(ResultsPage)(props);
  const propertyPageRenderer = setBaseProps(PropertyPage)(props);
  const datasetsPageRenderer = setBaseProps(DatasetsPage)(props);

  return (
    <main>
      <Switch>
        <Route exact path='/' render={homePageRenderer} />
        <Route exact path='/property' render={propertyPageRenderer} />
        <Route exact path='/search' render={resultsPageRenderer} />
        <Route exact path='/datasets' render={datasetsPageRenderer} />
        <Route exact path='/*' render={homePageRenderer} />
      </Switch>
    </main>
  );
}

export default Main;
