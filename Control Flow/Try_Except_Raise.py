def raises_value_error():
  raise ValueError
try:
  raises_value_error();
except:
  print("You raised a ValueError!");