import React, { Component } from 'react';
import { Switch, Route, BrowserRouter } from 'react-router-dom';
import './App.css';
import Main from './components/Main.js';
import Header from './components/Header.js';

class App extends Component {
  componentDidMount(){
    document.title = "Jack Tarbox"
  }
  render() {
      return(
        <div>
          <BrowserRouter>
            <Header></Header>
            <Main></Main>
          </BrowserRouter>
        </div>
      );
  }
}

export default App;
