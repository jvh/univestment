import React, { Component } from 'react'
import '../css/Main.css';

import {
  Form, FormControl, HelpBlock, ControlLabel, Button,
  FormGroup, ToggleButton, ToggleButtonGroup, Row, Col, InputGroup,
  FormLabel
} from 'react-bootstrap';

import Switch from 'react-switch';

import { Collapse } from 'react-collapse';

import ApiUtils from '../utils/ApiUtils.js';

import SearchForm from '../forms/SearchForm.js';

import { Link } from 'react-router-dom';

//import ValidationUtils from '../utils/ValidationUtils';

class HomePageSearch extends Component {

    constructor(props) {
      super(props);
      this.state = {
        form: {
          where: '',
          uni_search: false
        },
        isOpened: props.isOpened,
        isSubmitEnabled: false,
        uniSearch:false
      }
      this.handleFormChange = this.handleFormChange.bind(this);
    }

    advOptions = () => {
      this.setState({isOpened: !this.state.isOpened});
      if (this.props.collapse !== null) {
        this.props.collapse();
      }
    }

  validatePostcode = postcode => {
    postcode = postcode.replace(/\s/g, "");
    var regex = /^[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} ?[0-9][A-Z]{2}$/i;
    return regex.test(postcode);
  }

  handleSwitchChange = () => {
    this.setState({
      uniSearch:!this.state.uniSearch,
      form: {
        ...this.state.form,
        uni_search:!this.state.form.uni_search
      }});
  }

  handleSubmit = event => {
    this.props.history.push({
      pathname: '/search',
      state: {form: this.state.form}
    })
  }

  handleFormChange = event => {

     var value = event.target.value;
     const name = event.target.name;

     if (name === "where"){
       var valid = this.validatePostcode(value);
       this.setState({isSubmitEnabled:valid});
     }

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
             name="where"
             type="text"
             value={this.state.form.where}
             placeholder="Please enter Postcode..."
             onChange={this.handleFormChange}
           />
         </FormGroup>



            <Row>
             <FormGroup as={Col} controlId="distance">
               <FormLabel style={{fontWeight:"bold"}}>Distance from Location</FormLabel>
               <InputGroup>
                 <FormControl
                  as="select"
                  name="distance"
                  value={this.state.form.distance}
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


            <FormGroup as={Col} controlId="university_search">
                <FormLabel style={{fontWeight:"bold"}}>Distance From University</FormLabel>
                <FormControl
                 as="select"
                  name="km_away_from_uni"
                  value={this.state.form.km_away_from_uni}
                  onChange={this.handleFormChange}>
                  <option>1</option>
                  <option>2</option>
                  <option>3</option>
                  <option>4</option>
                  <option>5</option>
                </FormControl>
              </FormGroup>
            </Row>
           <Row>
             <FormGroup as={Col} controlId="min_price">
               <FormLabel style={{fontWeight:"bold"}}>Min Price</FormLabel>

               <InputGroup>
                 <InputGroup.Prepend>
                   <InputGroup.Text id="inputGroupPrepend">£</InputGroup.Text>
                 </InputGroup.Prepend>
                 <FormControl as="select"
                   name="price_min"
                   value={this.state.form.price_min}
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
                   name="price_max"
                   value={this.state.form.price_max}
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
               <FormLabel style={{fontWeight:"bold"}}>No. Beds</FormLabel>
               <FormControl as="select"
                 name="beds"
                 value={this.state.form.beds}
                 onChange={this.handleFormChange}>
                 <option>2</option>
                 <option>3</option>
                 <option>4</option>
                 <option>5+</option>
               </FormControl>
             </FormGroup>
           </Row>
           <Row>
         <FormGroup as={Col} controlId="search">
           <div  className="text-right">
            <Link to={{pathname:'/search', state:{form: this.state.form}}}>
             <Button type="button" disabled={!this.state.isSubmitEnabled}>
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


export default HomePageSearch;



           // <Collapse isOpened={this.state.isOpened} hasNestedCollapse={true}>


// </Collapse>
//
// <Row className="pad-top">
//
// <FormGroup as={Col} controlId="advanced">
//   <div className="text-left">
//     <Button variant="link" onClick={this.advOptions}>
//       Advanced Options...
//     </Button>
//   </div>
// </FormGroup>



// <Row>
//  <FormGroup as={Col} className="col-4" controlId="university_search">
//   <FormLabel style={{fontWeight:"bold"}}>University Search?</FormLabel>
//   <div className="switch-pad">
//     <div className="switch-inner">
//       <Switch
//         onChange={this.handleSwitchChange}
//         checked={this.state.uniSearch}
//         className="react-switch"
//       />
//     </div>
//   </div>
//  </FormGroup>
// </Row>




             //
             // <FormGroup as={Col} controlId="property_type">
             //   <FormLabel style={{fontWeight:"bold"}}>Property Type</FormLabel>
             //   <FormControl
             //    as="select"
             //     name="property_type"
             //     value={this.state.form.prop_type}
             //     onChange={this.handleFormChange}>
             //     <option>Show All</option>
             //     <option>Houses</option>
             //     <option>Flats</option>
             //   </FormControl>
             // </FormGroup>
