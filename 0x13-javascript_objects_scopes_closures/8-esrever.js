#!/usr/bin/node
exports.esrever = function (list) {
	if (list === undefined) return [];
	let reversed = [];
	for (let r = list.length - 1; r >= 0; r--) {
		reversed.push(list[r]);
	}
	return reversed;
};
