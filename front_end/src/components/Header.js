import React from 'react'
import '../css/Main.css';

const Header = props => {

  return (

<div>
  <nav className="navbar navbar-expand-md background navbar-dark">
    <div className="container">
      <a className="navbar-brand" href="/">FilmKnight</a>
      <div className="collapse navbar-collapse text-center justify-content-end" id="mainNavbar">
      <a className="btn navbar-btn background ml-2 text-white" href="/bar">
        <i className="fa d-inline fa-lg fa-user-circle-o"></i>Bar</a>
      <a className="btn navbar-btn background ml-2 text-white" href="/line">
        <i className="fa d-inline fa-lg fa-user-circle-o"></i>Line</a>
      </div>
    </div>
  </nav>
</div>

  );
}


export default Header;
