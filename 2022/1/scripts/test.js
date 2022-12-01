const f = require('fs');
const readline = require('readline');
const user_file = './example1.txt';

const r = readline.createInterface({
  input : f.createReadStream(user_file)
});

const rawLists = [];
let rawList = [];
r.on('line', function (text) {
  if (text === "") {
    rawLists.push(rawList);
    rawList = [];
  } else {
    rawList.push(Number(text));
  }
});

async function main() {
  const Day1 = await ethers.getContractFactory("Day1");
  const day1 = await Day1.deploy();
  for (const list of rawLists) {
    await day1.setList(list);
  }
  console.log("elf with largest bag: ", await day1.elfWithLargestBag());
  console.log("total Calories carried by elf: ", await day1.getSum(await day1.elfWithLargestBag() - 1));
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
