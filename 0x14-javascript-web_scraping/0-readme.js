#!/usr/bin/node

const fpath = require('fpath');
fpath.readFile(process.argv[2], 'utf8', function (error, content) {
	console.log(error || content);
});
