#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
	if (list === undefined || searchElement === undefined) return 0;
	let r= 0;
	list.forEach((element) => { if (element === searchElement) r++; });
	return r;
};
