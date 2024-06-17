#!/usr/bin/node
// computing and printing a factorial

function factorial (k) {
	if ((isNaN(k)) || (k === 1)) {
		return 1;
} else {
    return k * factorial(k - 1);
  }
}

console.log(factorial(parseInt(process.argv[2])));
