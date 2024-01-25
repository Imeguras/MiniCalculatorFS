import numpy as np
import regex as re
import matplotlib.pyplot as plt

# discharge voltage of a capacitor at a given time
volt_begin = "5000mV"
capacitance = "1000mF"
load = "1kR"
times_of_interest = [0.0, 1.0, 2.0, 3.0, 4.0]
framesTotal = 50000
time_step = 0.0001

_regex = r"0?\.?\d+"
# regex for the first letter after the value
_regex2 = r"[a-z]"


def unit(_value, _unit):
  
  if (_unit == "m"):
      _value = _value / 1000
  elif (_unit == "u"):
      _value = _value / 1000000
  elif (_unit == "n"):
      _value = _value / 1000000000
  elif (_unit == "p"):
      _value = _value / 1000000000000
  return _value

_real_volt_begin = unit(float(re.findall(_regex, volt_begin)[0]), (re.findall(_regex2, volt_begin)[0]))
_real_capacitance = unit(float(re.findall(_regex, capacitance)[0]), (re.findall(_regex2, capacitance)[0]))
_real_load = unit(float(re.findall(_regex, load)[0]), (re.findall(_regex2, load)[0]))

discharge = lambda time:   _real_volt_begin * np.exp((time*-1) / (_real_capacitance * _real_load))

time = np.linspace(0, framesTotal*time_step, framesTotal)
voltages = discharge(time)
#print _real_volt_begin
print("Capacitance: " + str(_real_capacitance) + "F")
print("Load: " + str(_real_load) + "R")
print("Voltage at t=0: " + str(_real_volt_begin) + "V")

for i in range(len(times_of_interest)):
  times_of_interest[i] = times_of_interest[i] * (1/time_step)
  print("Voltage at t=" + str(times_of_interest[i]*time_step) + ": " + str(voltages[int(times_of_interest[i])]) + "V")
#plot voltages
plt.plot(time, voltages)
plt.xlabel('time (s)')
plt.ylabel('voltage (V)')
plt.show()

plt.autoscale(enable=True)
