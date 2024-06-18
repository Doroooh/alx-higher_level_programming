#!/usr/bin/node
exports.logMe = (function (item) {
  let r = 0;
  return function (item) { console.log(r++ + ': ' + item); };
}());
