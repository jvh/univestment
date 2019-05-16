import React, { Component } from 'react';
import { Switch, Route, BrowserRouter } from 'react-router-dom';
import './App.css';
import Main from './components/Main.js';
import Header from './components/Header.js';
import Footer from './components/Footer.js';

class App extends Component {
  componentDidMount(){
    document.title = "Jack Tarbox"
  }
  render() {
      return(
        <div className="bg">
          <BrowserRouter>
            <Header/>
            <Main/>
          </BrowserRouter>
        </div>
      );
  }
}

export default App;

//<Footer/>
