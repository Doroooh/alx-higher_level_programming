#!/usr/bin/node
// prints a square

if (isNaN(process.argv[2])) {
	console.log('Missing size');
} else {
	for (let r = 0; r < parseInt(process.argv[2]); r++) {
		console.log('X'.repeat(parseInt(process.argv[2])));
  }
}
