#!/usr/bin/node
const MovieId = process.argv[2];

const request = require('request');

request('https://swapi-api.hbtn.io/api/films/' + MovieId + '/', function (err, res, body) {
  const json = JSON.parse(body);
  const values = json.characters;
  for (let i = 0; i < values.length; i++) {
    request(values[i], function (err, res, body) {
	    const chars = JSON.parse(body);
	    const name = chars.name;
      console.log(name);
    });
	       }
});
