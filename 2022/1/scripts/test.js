const f = require('fs');
const readline = require('readline');
const user_file = './example1.txt';

const r = readline.createInterface({
  input : f.createReadStream(user_file)
});

const rawList = [];
let i = 0;
r.on('line', function (text) {
  if (text === "") {
    rawList.push(0);
  } else {
    rawList.push(Number(text));
  }
});

async function main() {
  const Day1 = await ethers.getContractFactory("Day1");
  const day1 = await Day1.deploy();
  await day1.setList(rawList);
  console.log(await day1.elfWithLargestBag());
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
