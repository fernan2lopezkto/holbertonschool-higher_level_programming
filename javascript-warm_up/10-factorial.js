#!/usr/bin/node

function factorialRecursivo (n) {
if (n === 0){
	return 1;
}
return n * factorialRecursivo (n-1);
}

if (isNaN(process.argv[2])) {
  console.log(1);
} else {
  console.log(factorialRecursivo(process.argv[2]));
}
