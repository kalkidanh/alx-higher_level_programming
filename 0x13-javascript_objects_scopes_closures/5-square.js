#!/usr/bin/node

const Rectangle = require('./4rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
};
