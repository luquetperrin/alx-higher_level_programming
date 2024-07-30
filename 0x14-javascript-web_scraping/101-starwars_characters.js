#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

const apiUrl = `https://swapi-api.hbtn.io/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie data:', error);
    return;
  }

  const movieData = JSON.parse(body);

  const characterUrls = movieData.characters;

  const fetchCharacter = (index) => {
    if (index >= characterUrls.length) {
      return;
    }

    request(characterUrls[index], (error, response, body) => {
      if (error) {
        console.error('Error fetching character data:', error);
        return;
      }

      const characterData = JSON.parse(body);

      console.log(characterData.name);

      fetchCharacter(index + 1);
    });
  };

  fetchCharacter(0);
});
