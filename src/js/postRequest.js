import axios from 'axios';

const $axios = axios.create({
  baseURL: 'http://127.0.0.1:5000/',
  timeout: 5000,
  withCredentials: true,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Credentials': true,
  },
});

// Request Interceptor
$axios.interceptors.request.use((config) => {
  const conf = config;
  conf.headers.Authorization = 'Fake Token';
  return conf;
});

// Response Interceptor to handle and log errors
$axios.interceptors.response.use((response) => response,
  (error) => {
    // Handle Error
    // eslint-disable-next-line
    console.log(error);
    return Promise.reject(error);
  });

export default {
  fetchResource(path, data) {
    // return $axios.post(path, data)
    //   .then((response) => response.data);
    return axios.post(path, data, {
      baseURL: 'http://127.0.0.1:5000/',
      timeout: 5000,
      withCredentials: true,
      headers: {
        Accept: 'application/json',
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Credentials': true,
      },
    })
      .then((response) => response.data);
  },
};
