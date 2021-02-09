#!/usr/bin/node
/* script that prints the number of movies where the character “Wedge Antilles”
is present The first argument is the API URL of the Star wars
API: https://swapi-api.hbtn.io/api/films/ Wedge Antilles is character ID 18
You must use the module request */

const request = require('request');
const requestURL = process.argv[2];
const characterID = '/18/';
let count = 0;

request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    for (const film of JSON.parse(body).results) {
      for (const character of film.characters) {
        if (character.includes(characterID)) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
