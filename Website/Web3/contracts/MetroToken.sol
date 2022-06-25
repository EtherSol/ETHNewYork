// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MetroToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MetroToken", "MTNY") {
        _mint(msg.sender, initialSupply);
    }
}