#!/usr/bin/env python3

import AquaPiSystem
import time

aquarium = AquaPiSystem.AquaPi()

while True:
	system_outputs = aquarium.ReadOutputs()
	aquarium.ManagePump()
	print(aquarium.ReadOutputs())
	# time.sleep(0.1)