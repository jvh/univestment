import React, { Component } from 'react';
import  { Modal, Button } from 'react-bootstrap';
import { Link } from 'react-router-dom';

export default class Marker extends Component {

  constructor(props){
    super(props);
  }

  state = {
    showInfoWindow: false
  };
  handleMouseOver = e => {
    console.log("MOUSE OVER")
    this.setState({
      showInfoWindow: true
    });
  };
  handleMouseExit = e => {
    this.setState({
      showInfoWindow: false
    });
  };
  handleClose = e => {
    this.setState({
      showInfoWindow: false
    })
  }

  render () {

    const adzuna = this.props.result.property.adzuna;
    const allResults = this.props.result.all_results;

    const img_url = adzuna.image_url;

    const maxLength = 150;

    var description = adzuna.description;

    if (description.length > maxLength) {
      description = description.substr(0,maxLength);
      var index = description.lastIndexOf(" ");
      description = description.substr(0,index) + " ...";
    }
    const { showInfoWindow } = this.state;
    return (
      <div>
      <div onClick={this.handleMouseOver}>
          <img className="marker " style={{cursor:"pointer"}} src={require('../img/marker.png')}/>
      </div>
      <Modal show={showInfoWindow} onHide={this.handleClose} style={{paddingTop:"25vh"}}>
        <Modal.Body>
          <Link to={{pathname:'/property', state:{form: this.props.result}}}>
            <img style={{width:"100%"}} src={this.props.result.property.adzuna.image_url}/>
          </Link>
          <div className="row pad-hor">
            <div className="align-left adzuna-text pad-hor pad-top col-6" style={{whiteSpace:"nowrap"}}>
              <a href={adzuna.redirect_url} target="_blank" rel="noopener noreferrer" style={{position:"relative", top:"2px"}}>Properties by </a>
              <a href={adzuna.redirect_url} target="_blank" rel="noopener noreferrer">
                <img className="adzuna_logo" src={require("../img/adzuna_logo.jpg")} alt=""/>
              </a>
            </div>
            <div className="col-6 pad-top">
              <h3 className="align-right">£{adzuna.sale_price}</h3>
              <p className="align-right">guide price</p>
            </div>
          </div>
          <div className="col-12">
            <h3 className="align-center">{adzuna.title}</h3>
          </div>
          <div className="col-12">
            <p className="align-left">{adzuna.description}
              <Link to={{pathname:'/property', state:{form: this.props.result}}}>
                <a href={adzuna.redirect_url} target="_blank" rel="noopener noreferrer"> (Read more...)</a>
              </Link>
            </p>
          </div>
        </Modal.Body>
      </Modal>
      </div>
    )
  }
}



//  <Link to={{pathname:'/property', state:{form: this.props.result}}}>
//    <img className="marker " style={{cursor:"pointer"}} src={require('../img/marker.png')}/>
//  </Link>
