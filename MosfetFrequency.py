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
