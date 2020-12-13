# AquaPi Smart Aquarium
A Raspberry Pi project that uses 3 features to monitor an aquarium:
- Level sensor for determining water level
- Waterproof temperature sensor for monitoring the aquarium temperature
- Pump system for pumping out dirty water and pumping in fresh water

## Summary
This code utlizies high level functions to communicate with sensors and set their configuration for proper monitoring of an aquarium.

Unfortunately, I can't make the sub-repository for chip communication public. However that package provides a simple interface for communicating with sensors va I2C and SPI.

Another feature I considered adding was a home-made water quality sensor using a custom AFE and a LED/diode combination. This is still a WIP.
	

MIT License

Copyright (c) 2020 Engineering Outdoors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
