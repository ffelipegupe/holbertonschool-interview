#!/usr/bin/node
const MovieId = process.argv[2];

const request = require('request');

const url = 'https://swapi-api.hbtn.io/api/films/' + MovieId + '/';

request(url, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const json = JSON.parse(body);
  const values = json.characters;
  for (let i = 0; i < values.length; i++) {
    request(values[i], function (err, res, body) {
      if (err) {
        console.log(err);
      }
      const chars = JSON.parse(body);
      const name = chars.name;
      console.log(name);
    });
  }
});
