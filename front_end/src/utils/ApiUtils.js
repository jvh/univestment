import axios from 'axios';

const USE_MOCKS = false;

// REST API root URL
const host = 'http://api.univestment.co.uk';


// API endpoints
const endpoints = {
  search: { get: () => `${host}/search` }
};

// GET request function builder
const fetch = (endpoint, params) =>
  new Promise((resolve, reject) => {
    axios.get(endpoint)
      .then(response => {
        resolve(response.data);
      })
      .catch(reject);
    });

// POST request function builder
const post = (endpoint, params) =>
  new Promise((resolve, reject) => {
    axios.post(endpoint, params)
      .then(response => {
        resolve(response.data);
      })
      .catch(reject);
    });

// DELETE request function builder
const del = (endpoint, params) =>
  new Promise((resolve, reject) => {
    axios.delete(endpoint, params)
      .then(response => {
        resolve(response.data);
      })
      .catch(reject);
    });

// Add post POST request wrapper
const addPost = (societyId, content) =>
  post(endpoints.addPost.get(societyId), {
    content: content
  });

const buildQuery = (params) => {
  var query=`where=${params.where}`;

  console.log("SEARCH PARAMS")
  console.log(params);

  //query = params.price_min === undefined ? query : `${query}&price_min=${params.price_min}`;
  //query = params.price_max === undefined ? query : `${query}&price_max=${params.price_max}`;
  //query = params.beds === undefined ? query : `${query}&beds=${params.beds}`;
  //query = params.distance === undefined ? `${query}&from_radius=10` : `${query}&from_radius=${params.distance}`;
  //query = params.km_away_from_uni === undefined ? `${query}&km_away_from_uni=1` : `${query}&km_away_from_uni=${params.distance}`;


  // if (params.km_away_from_uni !== undefined) {
  //   query = `${query}&search_student_lets=true`;
  //   query = params.distance === undefined ?  `${query}&radius_from=10` : `${query}&radius_from=${params.distance}`;
  //   query = `${query}&km_away_from_uni=${params.km_away_from_uni}`
  // } else {
  //   query = params.distance === undefined ? query : `${query}&distance=${params.distance}`;
  // }

  query = query.replace(/,/gi, "");
  query = query.replace(/ /gi, "");

  console.log(query);

  return query;
}

const coords = (params) => {
  var url = `${host}/coords?${buildQuery(params)}`;
  return new Promise((resolve, reject) => {
    axios.get(url)
      .then(response => {
        resolve(response.data);
      })
      .catch(reject);
    });
}

const search = (params) => {
  var url = `${host}/search?${buildQuery(params)}`;
  return new Promise((resolve, reject) => {
    axios.get(url)
      .then(response => {
        resolve(response.data);
      })
      .catch(reject);
    });
}

export default {
    search: search,
    coords: coords,
};
