
import React from 'react';
import '../css/LoadingSpinner.css';

const LoadingSpinner = () => {
  return (
    <div className="loading">
      <div className="sk-cube-grid">
        <div className="sk-cube sk-cube1"></div>
        <div className="sk-cube sk-cube2"></div>
        <div className="sk-cube sk-cube3"></div>
        <div className="sk-cube sk-cube4"></div>
        <div className="sk-cube sk-cube5"></div>
        <div className="sk-cube sk-cube6"></div>
        <div className="sk-cube sk-cube7"></div>
        <div className="sk-cube sk-cube8"></div>
        <div className="sk-cube sk-cube9"></div>
      </div>
      <div>
        <h3 className="align-center pad-top">Crunching the Numbers...</h3>
        <p className="align-center pad-top">This can take up to 10 minutes</p>
      </div>
    </div>
)};

export default LoadingSpinner;
