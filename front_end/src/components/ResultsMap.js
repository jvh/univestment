
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import ApiUtils from '../utils/ApiUtils.js';
import { Link } from 'react-router-dom';
import Marker from './Marker.js';

// const Marker = (props) =>  <div>
//                         <Link to={{pathname:'/property', state:{form: props.result}}}>
//                           <img className="marker " style={{cursor:"pointer"}} src={require('../img/marker.png')}/>
//                         </Link>
//                         <div>
//                           <h1 className="tooltip">hello</h1>
//                         </div>
//                       </div>;

class ResultsMap extends Component {

  constructor(props) {
    super(props)

    console.log("MAP PROPS")
    console.log(props);

    this.state = {
      results: props.results,
      zoom:11,
      isLoading:true,
      results_page_state: props.results_state
    }
  }

  componentDidMount () {
    var where = {where:this.props.where};
    ApiUtils.coords(where)
      .then(this.handleCoordSuccess)
      .catch(this.handleCoordsFailure);
  }

  handleCoordSuccess = coords => {
    this.setState({
      center: {
        lng:coords[0],
        lat:coords[1]
      },
      isLoading:false
    });
  }

  handleCoordsFailure = response => {
    console.log(response);
  }

  static defaultProps = {
    center: {
      lat: 50.934502,
      lng: -1.45786
    },
    zoom: 11
  };

  placePins(state){
    console.log("PINS")
    console.log(state);
    const resultPins = state.results.map((result, index) => {
        if (result.data.latitude == null || result.data.longitude == null) {
          return null;
        } else {
         result={...result, results_state:this.state.results_page_state};
          return (
            <Marker result={result} lat={result.data.latitude} lng={result.data.longitude}/>
          );
        }
    });

    return resultPins;
  }

  render() {
    if (this.state.isLoading) {
      return (
        <div></div>
      )
    } else {
      return (
        <div className="map-outer rounded">
        <div className="map">
          <GoogleMapReact
            bootstrapURLKeys={{ key:'AIzaSyCElo3BDmiGTGaF6E-Cq6aVwgiihfPPA7c'}}
            defaultCenter={this.state.center}
            defaultZoom={this.state.zoom}
          >
          {
            this.placePins(this.state)
          }
          </GoogleMapReact>
        </div>
        </div>
      );
    }
  }
}

export default ResultsMap;
