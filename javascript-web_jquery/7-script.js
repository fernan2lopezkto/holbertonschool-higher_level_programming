#!/usr/bin/node

$(
    fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
        .then(res => res.json())
        .then(res => $('DIV#character').text(res.name))
)