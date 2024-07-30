#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (_err, res) {
  console.log('code:', res.statusCode); // Printing the response status code where there is a received a response 
});
