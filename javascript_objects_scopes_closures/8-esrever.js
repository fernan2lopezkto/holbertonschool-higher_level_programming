#!/usr/bin/node

exports.esrever = function (list) {
  // return list.reverse();
  const outp = [];
  for (let i = 0; i < list.length; i++) {
    outp.unshift(list[i]);
  }
  return outp;
};
