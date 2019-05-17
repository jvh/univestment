import React, { Component } from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import { Link } from 'react-router-dom';
import {
  Form, FormControl, HelpBlock, ControlLabel, Button,
  FormGroup, ToggleButton, ToggleButtonGroup, Row, Col, InputGroup,
  FormLabel
} from 'react-bootstrap';
import { Collapse } from 'react-collapse';

const  renderOption = (uni) => {
    return (
      <option>Hello</option>
    )
  }

class Filtering extends Component {

  constructor(props) {
    super(props);
    this.state={
      callback:props.callback,
      showUniversityFilters:false,
      form:props.filters,
      all_unis:props.universities
    }
  }

  handleSearchSubmit = () => {
    this.props.history.push({
      pathname: '/',
      state: {
        form: this.state.form
      }
    })
  }

  validatePostcode = postcode => {
    postcode = postcode.replace(/\s/g, "");
    var regex = /^[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} ?[0-9][A-Z]{2}$/i;
    return regex.test(postcode);
  }

  handleFormChange = event => {

     var value = event.target.value;
     const name = event.target.name;

     // if (name === "sort" && value === "University") {
     //   this.setState({showUniversityFilters: true});
     // } else if (name === "sort") {
     //     this.setState({showUniversityFilters: false});
     // }

     this.setState({
       form: {
         ...this.state.form,
         [name]: value
       }
     });

     this.state.callback({name: name, value: value});

   };

   handleSearchChange = event => {
     var value = event.target.value;
     const name = event.target.name;

     this.setState({
       form: {
         ...this.state.form,
         [name]: value
       }
     });

   }

  renderAllOptions () {
    var items=[];
    items.push(<option>Select University</option>);
    this.state.all_unis.forEach(function(uni) {
      items.push(<option>{uni.name}</option>);
    })
    return items;
  }

  render () {


  return (
    <div className="filter results-bg">
      <div className="container-large">
        <div className="justify-content-center filter-inner">
          <div className="row">
            <div className="col-4">
              <Form onSubmit={this.handleSearchSubmit}>
                <FormGroup controlId="postcode">
                  <button class="btn btn-outline-secondary" type="button" onClick={this.handleSearchSubmit}>Back to Search</button>
                </FormGroup>
              </Form>
            </div>
            <div className="col-3">
            </div>
            <div className="col-5">
              <div className="sort-by">

                <Form onSubmit={this.handleSubmit}>
                  <Row>
                    <FormGroup controlId="filter_label">
                      <FormLabel style={{fontWeight:"bold", fontSize:"120%"}} className="filters-label">Filters:</FormLabel>
                    </FormGroup>
                    <FormGroup as={Col} controlId="sort_by">
                      <FormControl as="select"
                        name="sort"
                        value={this.state.form.sort}
                        onChange={this.handleFormChange}>
                        <option>Sort By</option>
                        <option>Price high to low</option>
                        <option>Price low to high</option>
                        <option>Relevance</option>
                      </FormControl>
                    </FormGroup>
                    <FormGroup as={Col} controlId="universities">
                      <FormControl as="select"
                        name="universities"
                        value={this.state.form.universities}
                        onChange={this.handleFormChange}>
                        {
                          this.renderAllOptions()
                        }
                      </FormControl>
                    </FormGroup>
                  </Row>
                </Form>
              </div>
            </div>

          </div>
        </div>
      </div>
    </div>
  );
  }

}

export default Filtering;



// <FormGroup as={Col} controlId="results_num">
//   <FormControl as="select"
//     name="results_per_page"
//     value={this.state.form.results_per_page}
//     onChange={this.handleFormChange}>
//     <option>Results per page</option>
//     <option>10</option>
//     <option>25</option>
//     <option>50</option>
//   </FormControl>
// </FormGroup>

// <div className="col-2">
// </div>
// <div className="col-4">
//   <Form onSubmit={this.handleSearchSubmit}>
//     <FormGroup controlId="postcode">
//       <InputGroup>
//         <FormControl
//           name="where"
//           type="text"
//           value={this.state.form.where}
//           placeholder="Please enter Postcode..."
//           onChange={this.handleSearchChange}
//         />
//         <InputGroup.Append>
//           <button class="btn btn-outline-secondary" type="button" onClick={this.handleSearchSubmit}>Go</button>
//         </InputGroup.Append>
//       </InputGroup>
//     </FormGroup>
//   </Form>
// </div>

  // <div className="col-3">
  //   <Form onSubmit={this.handleSearchSubmit}>
  //     <FormGroup controlId="postcode">
  //       <InputGroup>
  //         <FormControl
  //           name="where"
  //           type="text"
  //           value={this.state.form.where}
  //           placeholder="Please enter Postcode..."
  //           onChange={this.handleFormChange}
  //         />
  //         <InputGroup.Append>
  //           <button class="btn btn-outline-secondary" type="button" onClick={this.handleSearchSubmit}>Go</button>
  //         </InputGroup.Append>
  //       </InputGroup>
  //     </FormGroup>
  //   </Form>
  // </div>


  // <div className="row">
  //   <Collapse isOpened={this.state.showUniversityFilters}>
  //     <div className="university-filters border">
  //       <Form onSubmit={this.handleSubmit}>
  //         <Row>
  //           <FormGroup as={Col} controlId="results_num">
  //             <FormControl as="select"
  //               name="results_per_page"
  //               value={this.state.form.results_per_page}
  //               onChange={this.handleFormChange}>
  //               <option>Select University</option>
  //               <option>Uni of 1</option>
  //               <option>Uni of 2</option>
  //               <option>Uni of 3</option>
  //             </FormControl>
  //           </FormGroup>
  //         </Row>
  //       </Form>
  //     </div>
  //   </Collapse>
  // </div>

  // <FormGroup as={Col} controlId="min_price">
  //   <FormControl as="select"
  //     name="beds"
  //     value={this.state.form.beds}
  //     onChange={this.handleFormChange}>
  //     <option>University</option>
  //     {
  //       this.renderOptions()
  //     }
  //   </FormControl>
  // </FormGroup>

    // <FormGroup as={Col} controlId="min_price">
    //   <FormControl as="select"
    //     name="beds"
    //     value={this.state.form.beds}
    //     onChange={this.handleFormChange}>
    //     <option>Min. Price</option>
    //     <option>3</option>
    //     <option>4</option>
    //     <option>5+</option>
    //   </FormControl>
    // </FormGroup>

// <FormGroup as={Col} controlId="min_price">
//   <FormControl as="select"
//     name="beds"
//     value={this.state.form.beds}
//     onChange={this.handleFormChange}>
//     <option>No. Beds</option>
//     <option>3</option>
//     <option>4</option>
//     <option>5+</option>
//   </FormControl>
// </FormGroup>
//
// <FormGroup as={Col} controlId="min_price">
//   <FormControl as="select"
//     name="beds"
//     value={this.state.form.beds}
//     onChange={this.handleFormChange}>
//     <option>Max. Price</option>
//     <option>3</option>
//     <option>4</option>
//     <option>5+</option>
//   </FormControl>
// </FormGroup>
