
import React, { Component } from 'react';
import GoogleMapReact from 'google-map-react';
import ApiUtils from '../utils/ApiUtils.js';

const Marker = () =>  <div>
                        <img className="marker" style={{cursor:"pointer"}} src={require('../img/marker.png')}/>
                      </div>;

class ResultsMap extends Component {

  constructor(props) {
    super(props)
    this.state = {
      results: props.results,
      zoom:11,
      isLoading:true
    }
  }

  componentDidMount () {
    console.log(this.props.where)
    var where = {where:this.props.where};
    ApiUtils.coords(where)
      .then(this.handleCoordSuccess)
      .catch(this.handleCoordsFailure);
  }

  handleCoordSuccess = coords => {
    console.log("COORDS");
    console.log(coords);
    this.setState({
      center: {
        lng:coords[0],
        lat:coords[1]
      },
      isLoading:false
    });
  }

  handleCoordsFailure = response => {
    console.log("FAIL");
  }

  static defaultProps = {
    center: {
      lat: 50.934502,
      lng: -1.45786
    },
    zoom: 11
  };

  placePins(){
    const resultPins = this.state.results.map((result, index) => {
        console.log("RESULT");
        console.log(result);
        if (result.property.adzuna.latitude == null || result.property.adzuna.longitude == null) {
          return null;
        } else {
          return (
            <Marker lat={result.property.adzuna.latitude} lng={result.property.adzuna.longitude}/>
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
        <div className="map rounded">
          <GoogleMapReact
            bootstrapURLKeys={{ key:'AIzaSyCElo3BDmiGTGaF6E-Cq6aVwgiihfPPA7c'}}
            defaultCenter={this.state.center}
            defaultZoom={this.state.zoom}
          >
          {
            this.placePins()
          }
          </GoogleMapReact>
        </div>
      );
    }
  }
}

export default ResultsMap;
