import React from 'react'
import '../css/Main.css';

const Header = props => {

  return (

<div>
  <nav className="navbar navbar-expand-md background navbar-dark">
    <div className="container">
      <a className="navbar-brand header" href="/">
      <img className="header-logo" src={require('../img/logo_white.svg')}/>
      Univestment</a>
      <div className="collapse navbar-collapse text-center justify-content-end" id="mainNavbar">
      <a className="btn navbar-btn background ml-2 text-white" href="mailto:jt7g15@soton.ac.uk?Subject=Univestment Contact">
        <i className="fa d-inline fa-lg fa-user-circle-o"></i>Contact Us</a>
      </div>
    </div>
  </nav>
</div>

  );
}


export default Header;


// <a className="btn navbar-btn background ml-2 text-white" href="/">
//   <i className="fa d-inline fa-lg fa-user-circle-o"></i>Premium</a>
// <a className="btn navbar-btn background ml-2 text-white" href="/">
//   <i className="fa d-inline fa-lg fa-user-circle-o"></i>About Us</a>
