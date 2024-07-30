#!/usr/bin/node

// Import the fs module
const fs = require('fs');

// Read the file specified by the first command-line argument
fs.readFile(process.argv[2], 'utf8', function (error, content) {
  // Log the error if it exists, otherwise log the content of the file
  console.log(error || content);
});

