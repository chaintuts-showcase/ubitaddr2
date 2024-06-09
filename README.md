## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* uBitAddr2 is an offline Bitcoin address generator for microcontroller platforms

## Development
________________

### Git Workflow
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Generate a random private key and associated address for Bitcoin, Bitcoin Cash
* Key formats include WIF (BTC, BCH)
* Address formats include Legacy Base58 (BTC, BCH)
* Display the address and private key on a character LCD screen, rotating every 60 seconds
* Print the address and private key to serial

### Requirements
* Requires CircuitPython

### Platforms
* Adafruit M4 microcontrollers (ItsyBitsy M4, Grand Central M4, Metro M4)

## Usage
____________

### Code Installation
* Connect your microprocessor to PC via USB
* Copy the source Python files and libraries to the `CircuitPython` directory
* Configure desired currency and output methods

### Peripheral Installation
* Wire up the desired output - currently supports a character LCD with I2C backpack, or output to PC via USB cable (no accessories needed)

### General usage
* Once the code is loaded, restart the board to automatically generate a new address, private key

### Run unit tests
* Run `python -m pytest <test file>`