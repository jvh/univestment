import React, { Component } from 'react'
import '../css/Main.css';

import {
  Form, PageHeader, FormControl, HelpBlock, FormLabel, Button, Col,
  FormGroup, ToggleButton, ToggleButtonGroup, Row, Dropdown, DropdownItem,
  InputGroup

} from 'react-bootstrap';

import { Collapse } from 'react-collapse';

//import ValidationUtils from '../utils/ValidationUtils';

var isOpened = false;

const onClick = () => {
  isOpened = !isOpened;
  console.log("Clicked");
}

const SearchForm = props => {

  const { form, onChange, onSubmit } = props;

  var submitEnabled = true;

  // const onClickAdvanced = () => {
  //   isOpened = !isOpened;
  //   console.log(isOpened)
  // }

  return (
    <Form onSubmit={onSubmit}>
      <FormGroup controlId="postcode">
        <FormControl
          name="location"
          type="text"
          value={form.location}
          placeholder="Location..."
          onChange={onChange}
        />
      </FormGroup>

      <Row>
        <FormGroup as={Col} controlId="min_price">

          <InputGroup>
            <InputGroup.Prepend>
              <InputGroup.Text id="inputGroupPrepend">£</InputGroup.Text>
            </InputGroup.Prepend>
            <FormControl as="select"
              name="min_price"
              value={form.min_price}
              onChange={onChange}>

              <option>Min. Price</option>
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
          <InputGroup>
            <InputGroup.Prepend>
              <InputGroup.Text id="inputGroupPrepend">£</InputGroup.Text>
            </InputGroup.Prepend>
            <FormControl as="select"
              name="max_price"
              value={form.max_price}
              onChange={onChange}>
              <option>Max. Price</option>
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
          <FormControl as="select"
            name="min_beds"
            value={form.min_beds}
            onChange={onChange}>
            <option>Min. Beds</option>
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

      <div>

        <Collapse isOpened={isOpened}>
          <div>


          <FormGroup as={Col} controlId="min_price">
            <FormControl as="select"
              name="min_beds"
              value={form.min_beds}
              onChange={onChange}>
              <option>Min. Beds</option>
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
          </div>
        </Collapse>

      </div>

      <Row>

        <FormGroup as={Col} controlId="advanced">
          <div className="text-left">
            <Button variant="link" className="adv-btn" onClick={onClick}>
              Advanced Options...
            </Button>
          </div>
        </FormGroup>
        <FormGroup as={Col} controlId="submit">
          <div  className="text-right">
            <Button type="submit" disabled={!submitEnabled}>
              Search...
            </Button>
          </div>
        </FormGroup>
      </Row>
    </Form>
  );
}

export default SearchForm;



  // name="min_price"
  // type="drop"
  // value={form.min_price}
  // placeholder="Min. Price"
  // onChange={onChange}
