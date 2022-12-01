const f = require('fs');
const readline = require('readline');
const user_file = './example1.txt';
const r = readline.createInterface({
  input : f.createReadStream(user_file)
});

const bags = [];
r.on('line', function (text) {
  console.log(text + (text === "" ? "<>" : ""));
});

