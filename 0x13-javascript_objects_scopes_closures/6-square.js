#!/usr/bin/node
const OldSq = require('./5-square');
module.exports = class Square extends OldSq {
	charPrint (c) {
		if (c === undefined) c = 'X';
		for (let q = 0; q < this.height; q++) {
			console.log(c.repeat(this.width));
    }
  }
};
