// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0;

import "hardhat/console.sol";

// The jungle must be too overgrown and difficult to navigate in vehicles or
// access from the air; the Elves' expedition traditionally goes on foot. As
// your boats approach land, the Elves begin taking inventory of their supplies.
// One important consideration is food - in particular, the number of Calories
// each Elf is carrying (your puzzle input).

// The Elves take turns writing down the number of Calories contained by the
// various meals, snacks, rations, etc. that they've brought with them, one item
// per line. Each Elf separates their own inventory from the previous Elf's
// inventory (if any) by a blank line.

// For example, suppose the Elves finish writing their items' Calories and end
// up with the following list:

// 1000
// 2000
// 3000

// 4000

// 5000
// 6000

// 7000
// 8000
// 9000

// 10000

// This list represents the Calories of the food carried by five Elves:

// - The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total
// of 6000 Calories.

// - The second Elf is carrying one food item with 4000 Calories.

// - The third Elf is carrying food with 5000 and 6000 Calories, a total of
// 11000 Calories.

// - The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total
// of 24000 Calories.

// - The fifth Elf is carrying one food item with 10000 Calories.

// In case the Elves get hungry and need extra snacks, they need to know which Elf
// to ask: they'd like to know how many Calories are being carried by the Elf
// carrying the most Calories. In the example above, this is 24000 (carried by the
// fourth Elf).

// Find the Elf carrying the most Calories.
// How many total Calories is that Elf carrying?


contract Day1 {
  struct Bag {
    // each item is represented by calories
    uint sum;
    uint[] items;
  }
  // each index of the bag in the array represents a distinct Elf
  mapping (uint => Bag) public bags;
  uint elves = 0;
  
  constructor() {}

  function setList(uint[] memory rawList) public {
    uint index = 0;
    for (uint i = 0; i < rawList.length; i++) {
      uint item = rawList[i];
      // console.log("item: ", item);
      if (item == 0) {
        index += 1;
        elves += 1;
      } else {
        bags[index].items.push(item);
        bags[index].sum += item;
        // console.log("pushed: ", item);
        // console.log("set sum: ",  bags[index].sum);
      }
      // console.log("");
    }
  }

  function getSum(uint index) public view returns (uint) {
    return bags[index].sum;
  }

  function elfWithLargestBag() public view returns (uint) {
    uint elf = 0;
    uint maxCals = 0;
    uint i;
    // console.log("elves: ", elves);
    for (i = 1; i < elves + 2; i++) {
      // console.log("i: ", i);
      Bag memory b = bags[i-1];
      // console.log("b.sum: ", b.sum);
      if (b.sum > maxCals) {
        maxCals = b.sum;
        elf = i;
      }
    }
    return elf;
  }

  function sumItems(uint[] memory items) public pure returns (uint) {
    uint ret = 0;
    for (uint i = 0; i < items.length; i++) {
      ret += items[i];
    }
    return ret;
  }
}

