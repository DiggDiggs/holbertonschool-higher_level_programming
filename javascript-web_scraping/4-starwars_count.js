#!/usr/bin/node
const request = require('request');
const apiUrl = process.argv[2];
const characterId = 18;

function countMoviesWithCharacter(data) {
    if (!Array.isArray(data.characters)) {
        return 0;
    }

    let count = 0;
    for (const characterUrl of data.characters) {
        const characterIdInUrl = characterUrl.split('/').slice(-2, -1)[0];
        if (parseInt(characterIdInUrl) === characterId) {
            count ++;
        }
    }
    return count;
}

request.get(apiUrl, (err, response, body) => {
    if (err) {
        console.error(err);
    } else if (response.statusCode === 200) {
        const data = JSON.parse(body);
        const numberOfMovies = countMoviesWithCharacter(data);
        console.log(`${numberOfMovies}`);
    } else {
        console.error(`Error: Unexpected status code ${response.statusCode}`);
    }
});