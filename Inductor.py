import numpy as np
import regex as re
import matplotlib.pyplot as plt


time_step_formula = lambda x: (1/1000000)*x + 1000
initial_current = "2.5A"
load = "1.5R"
current_formula = lambda x: ( np.maximum(0,2*x-1000)) # 1 ampere increment

inductance_input = "0.75uH" 
max_steps_def = 3000
end_time = 3000

# replace any comma with a dot
inductance_input = inductance_input.replace(",", ".")
initial_current = initial_current.replace(",", ".")
load = load.replace(",", ".")
# ragex to extract the value and the unit


def unit(_value, _unit):
  if(_unit == "M"): 
    _value = _value * 1000000
  elif(_unit == "k"):
    _value = _value * 1000
  elif (_unit == "m"):
      _value = _value / 1000
  elif (_unit == "u"):
      _value = _value / 1000000
  elif (_unit == "n"):
      _value = _value / 1000000000
  elif (_unit == "p"):
      _value = _value / 1000000000000
  return _value

__regex_harry = r"[a-z|M]"

try: 
  _value = unit(float(re.findall(r"0?\.?\d+", inductance_input)[0]),re.findall(__regex_harry, inductance_input)[0])
  _f_current = unit(float(re.findall(r"0?\.?\d+", initial_current)[0]),re.findall(__regex_harry, initial_current)[0])
  _load_mesmo = unit(float(re.findall(r"0?\.?\d+", load)[0]),re.findall(__regex_harry, load)[0])
except: 
  _value = float(re.findall(r"0?\.?\d+", inductance_input)[0])
  _f_current = float(re.findall(r"0?\.?\d+", initial_current)[0])
  _load_mesmo = float(re.findall(r"0?\.?\d+", load)[0])
  

_steps  = np.linspace(1, end_time, max_steps_def)  # 100 steps from 0 to 1

_time_steps = time_step_formula(_steps) 
_current = current_formula(_steps)
#print (_time_steps)
#print (_current)


voltages = _value * np.gradient(_current, _time_steps) + _f_current * _load_mesmo

#print (voltages)

plt.plot(_time_steps, voltages)
#plot the current to with x's instead of line
plt.plot(_time_steps, _current, 'x')
plt.xlabel('time (s)')
plt.ylabel('voltage (V)')
#auto adjust the y values
plt.autoscale(enable=True)

plt.show()
