#!/usr/bin/node

// variavles
const argums = process.argv;

// there is more of one arguments
if (argums.length > 3) {
  let bigbig = 0;
  let secbig = 0;
  let i;
  for (i = 2; i < argums.length; i++) {
    let nume = parseInt(argums[i]);
    if (nume > bigbig && nume > secbig) {
      secbig = bigbig;
      bigbig = nume;
    } else if (nume < bigbig && nume > secbig) {
      secbig = nume;
    }
  }
  console.log(secbig);
} else {
  console.log(0);
}
