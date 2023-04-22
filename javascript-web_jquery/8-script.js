#!/usr/bin/node

$(
    fetch('https://swapi-api.hbtn.io/api/films/?format=json')
        .then(resp => resp.json())
        .then(resp => {
            for (let i = 0; i < resp.results.length; i++) {
                let value = '<li>' + resp.results[i]['title'] + '</li>'
                $('#list_movies').append(value);
            }
      })
)