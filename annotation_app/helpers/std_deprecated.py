def mapp(callback, iterable):
  output = []

  for item in iterable:
    output.append(callback(item))

  return output

def filterr(callback, iterable):
  output = []

  for item in iterable:
    if callback(item):
      output.append(item)

  return output

def maxx(iterable, key=None):
  current_max = iterable[0]

  for item in iterable[1:]:
    if key:
      if key(item) > key(current_max):
        current_max = item
    else:
      if item > current_max:
        current_max = item

  return current_max
