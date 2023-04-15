#!/usr/bin/node
/*
 * crear una lista con diccionarios adentro
 * cada deccionario guarda <len de lista>:<value>
 * un for para printear ky:value
 */

const list = [];

exports.logMe = function (item) {
  list.push(item);
  console.log(list.length + ': ' + item);
};

// ouput format
// <number arg already printed>: <current arg value>
