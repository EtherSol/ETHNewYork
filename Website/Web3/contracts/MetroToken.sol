// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/token/ERC20/extensions/ERC20Votes.sol"

contract MetroToken is ERC20Votes {
    constructor(uint256 initialSupply) ERC20("MetroToken", "MTNY") {
        _mint(msg.sender, initialSupply);
    }
}