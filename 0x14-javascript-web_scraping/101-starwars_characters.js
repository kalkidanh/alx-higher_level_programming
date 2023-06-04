#!/usr/bin/node

const request = require('request');

const url = 'https://swapi.dev/api/films/' + process.argv[2] + '/';
let characters = [];

request(url, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  characters = JSON.parse(body).characters;
  getCharacters(0);
});

const getCharacters = (count) => {
  if (count === characters.length) {
    return;
  }

  request(characters[count], (error, response, body) => {
    if (error) {
      console.log(error);
      return;
    }
    console.log(JSON.parse(body).name);
    getCharacters(count + 1);
  });
};
