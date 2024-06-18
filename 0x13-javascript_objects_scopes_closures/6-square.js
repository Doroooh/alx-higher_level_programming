#!/usr/bin/node
const OldSq = require('./5-square');
module.exports = class Square extends OldSq {
	charPrint (r) {
		if (r === undefined) r = 'K';
		for (let q = 0; q < this.height; q++) {
			console.log(r.repeat(this.width));
    }
  }
};
