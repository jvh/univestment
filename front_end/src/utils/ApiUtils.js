import axios from 'axios';

const USE_MOCKS = false;

// REST API root URL
const host = 'http://localhost:5000';

// API endpoints
const endpoints = {
  test_data: { get: data => `${host}/test_data` }
};

// GET request function builder
const fetch = endpoint => endPointParams =>
  new Promise((resolve, reject) => {
    axios.get(endpoint.get(endPointParams))
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
                resolve(response.data)
;            })
            .catch(reject);
    });

// Add post POST request wrapper
const addPost = (societyId, content) =>
  post(endpoints.addPost.get(societyId), {
    content: content
  });

export default {
    getData: fetch(endpoints.test_data),
    addPost: addPost
  };
