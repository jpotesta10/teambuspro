class Bus():
  pass

bus = Bus()

first_key = 'first
first_val = 'Corey'


setattr(bus, first_key, first_val)

first = getattr(bus, first_key)

print(first)
