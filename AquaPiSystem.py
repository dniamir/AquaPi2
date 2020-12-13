from chip_systems import ProjectSystem
import AquaPiSubSystems

# from chip_systems import MaximDS18B20
# from PumpSystem import AquaPyPumps
# from LevelSensor import eTapeSensor


class AquaPi(ProjectSystem.ProjectSystem):

	def __init__(self):
		self.temp_sensor = None
		self.fluid_sensor = None
		self.pumps = None
		self.SetupSystem()

	def SetupSystem(self):
		self.temp_sensor = AquaPiSubSystems.AquaPiTemperature()
		self.fluid_sensor = AquaPiSubSystems.AquaPiFluidLevel()
		self.pumps = AquaPiSubSystems.AquaPiPumpSwitches(pump1_pin=15)
		self.level_sensor = AquaPiSubSystems.AquaPiFluidLevel()

	def ReadOutputs(self):

		temperature_c = self.temp_sensor.ReadOutputs()
		fluid_level_cm = self.level_sensor.ReadOutputs()
		switch1, switch2 = self.pumps.ReadOutputs()
		return switch1, switch2, fluid_level_cm, temperature_c

	def ManagePump(self):

		if self.pumps.switch1 and self.pumps.pump1_state == 0:
			self.pumps.StartInPump()

		if not self.pumps.switch1 and self.pumps.pump1_state == 1:
			self.pumps.StopInPump()
