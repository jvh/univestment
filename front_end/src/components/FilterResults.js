import React, { Component } from 'react'
import '../css/Main.css';

import {
  Form, FormControl, HelpBlock, ControlLabel, Button,
  FormGroup, ToggleButton, ToggleButtonGroup, Row, Col, InputGroup,
  FormLabel
} from 'react-bootstrap';

import { Collapse } from 'react-collapse';

import ApiUtils from '../utils/ApiUtils.js';

import SearchForm from '../forms/SearchForm.js';

import { Link } from 'react-router-dom';

//import ValidationUtils from '../utils/ValidationUtils';

class FilterResults extends Component {

    constructor(props) {
      super(props);
      this.state = {
        form: {
          location: ''
        },
        isOpened: false
      }

      this.handleFormChange = this.handleFormChange.bind(this);
    }

    advOptions = () => {
      this.setState({isOpened: !this.state.isOpened});
    }

    handleFormChange = event => {
     var value = event.target.value;
     const name = event.target.name;

     this.setState({
       form: {
         ...this.state.form,
         [name]: value
       }
     });
   };

   render() {
     return (
       <div>

       <Form onSubmit={this.handleSubmit}>
         <FormLabel style={{fontWeight:"bold"}}>Location</FormLabel>
         <FormGroup controlId="postcode">
           <FormControl
             name="location"
             type="text"
             value={this.state.form.location}
             placeholder="Please enter Postcode..."
             onChange={this.handleFormChange}
           />
         </FormGroup>

         <Row>
           <FormGroup as={Col} controlId="min_price">
             <FormLabel style={{fontWeight:"bold"}}>Min Price</FormLabel>

             <InputGroup>
               <InputGroup.Prepend>
                 <InputGroup.Text id="inputGroupPrepend">£</InputGroup.Text>
               </InputGroup.Prepend>
               <FormControl as="select"
                 name="min_price"
                 value={this.state.form.min_price}
                 onChange={this.handleFormChange}>

                 <option>No min</option>
                 <option>10,000</option>
                 <option>20,000</option>
                 <option>30,000</option>
                 <option>40,000</option>
                 <option>50,000</option>
                 <option>60,000</option>
                 <option>70,000</option>
                 <option>80,000</option>
                 <option>90,000</option>
                 <option>100,000</option>
                 <option>110,000</option>
                 <option>120,000</option>
                 <option>130,000</option>
                 <option>140,000</option>
                 <option>150,000</option>
                 <option>175,000</option>
                 <option>200,000</option>
                 <option>225,000</option>
                 <option>250,000</option>
                 <option>275,000</option>
                 <option>300,000</option>
                 <option>325,000</option>
                 <option>350,000</option>
                 <option>375,000</option>
                 <option>400,000</option>
                 <option>450,000</option>
                 <option>500,000</option>
                 <option>550,000</option>
                 <option>600,000</option>
                 <option>650,000</option>
                 <option>700,000</option>
                 <option>800,000</option>
                 <option>900,000</option>
                 <option>1,000,000</option>
                 <option>1,100,000</option>
                 <option>1,200,000</option>
                 <option>1,300,000</option>
                 <option>1,400,000</option>
                 <option>1,500,000</option>
                 <option>1,750,000</option>
                 <option>2,000,000</option>
               </FormControl>
             </InputGroup>
           </FormGroup>

           <FormGroup as={Col} controlId="min_price">
             <FormLabel style={{fontWeight:"bold"}}>Max Price</FormLabel>
             <InputGroup>
               <InputGroup.Prepend>
                 <InputGroup.Text id="inputGroupPrepend">£</InputGroup.Text>
               </InputGroup.Prepend>
               <FormControl as="select"
                 name="max_price"
                 value={this.state.form.max_price}
                 onChange={this.handleFormChange}>
                 <option>No max</option>
                 <option>10,000</option>
                 <option>20,000</option>
                 <option>30,000</option>
                 <option>40,000</option>
                 <option>50,000</option>
                 <option>60,000</option>
                 <option>70,000</option>
                 <option>80,000</option>
                 <option>90,000</option>
                 <option>100,000</option>
                 <option>110,000</option>
                 <option>120,000</option>
                 <option>130,000</option>
                 <option>140,000</option>
                 <option>150,000</option>
                 <option>175,000</option>
                 <option>200,000</option>
                 <option>225,000</option>
                 <option>250,000</option>
                 <option>275,000</option>
                 <option>300,000</option>
                 <option>325,000</option>
                 <option>350,000</option>
                 <option>375,000</option>
                 <option>400,000</option>
                 <option>450,000</option>
                 <option>500,000</option>
                 <option>550,000</option>
                 <option>600,000</option>
                 <option>650,000</option>
                 <option>700,000</option>
                 <option>800,000</option>
                 <option>900,000</option>
                 <option>1,000,000</option>
                 <option>1,100,000</option>
                 <option>1,200,000</option>
                 <option>1,300,000</option>
                 <option>1,400,000</option>
                 <option>1,500,000</option>
                 <option>1,750,000</option>
                 <option>£2,000,000</option>
               </FormControl>
             </InputGroup>
           </FormGroup>

           <FormGroup as={Col} controlId="min_price">
             <FormLabel style={{fontWeight:"bold"}}>Min. Beds</FormLabel>
             <FormControl as="select"
               name="min_beds"
               value={this.state.form.min_beds}
               onChange={this.handleFormChange}>
               <option>No min</option>
               <option>1</option>
               <option>2</option>
               <option>3</option>
               <option>4</option>
               <option>5</option>
               <option>6</option>
               <option>7</option>
               <option>8</option>
               <option>9</option>
               <option>10</option>
             </FormControl>
           </FormGroup>
         </Row>

         <Row>

           <Collapse isOpened={this.state.isOpened}>

             <FormGroup as={Col} controlId="distance">
               <FormLabel style={{fontWeight:"bold"}}>Distance from Location</FormLabel>


               <InputGroup>
                 <FormControl as="select">
                  name="distance"
                  value={this.state.form.distance}
                  defaultValue=10
                  onChange={this.handleFormChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>5</option>
                  <option>10</option>
                  <option>15</option>
                  <option>20</option>
                  <option>30</option>
                  <option>40</option>
                 </FormControl>
                 <InputGroup.Append>
                   <InputGroup.Text id="inputGroupAppend">km</InputGroup.Text>
                 </InputGroup.Append>
               </InputGroup>
             </FormGroup>


             <FormGroup as={Col} controlId="property_type">
               <FormLabel style={{fontWeight:"bold"}}>Property Type</FormLabel>
               <FormControl as="select">
                 name="property_type"
                 value={this.state.form.prop_type}
                 onChange={this.handleFormChange}>
                 <option>Show All</option>
                 <option>Houses</option>
                 <option>Flats</option>
               </FormControl>
             </FormGroup>
           </Collapse>
         </Row>

         <Row className="pad-top">

           <FormGroup as={Col} controlId="advanced">
             <div className="text-left">
               <Button variant="link" onClick={this.advOptions}>
                 Advanced Options...
               </Button>
             </div>
           </FormGroup>

         <FormGroup as={Col} controlId="search">
           <div  className="text-right">
            <Link to={{pathname:'/search', state:{form: this.state.form}}}>
             <Button type="button">
               Search
             </Button>
             </Link>
           </div>
         </FormGroup>
         </Row>
       </Form>
       </div>
     );
  }
}


export default FilterResults;
