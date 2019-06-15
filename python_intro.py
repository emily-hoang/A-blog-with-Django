def hi(name):
  if name == "Ola":
    print("Hi Ola!")
  elif name == "Nhung":
    print("Hello, Nhung!")
  else:
    print("Hi anonymus")
hi("Ola")

def hello(name):
  print('Hello ' + name + "!")

girls = [ "Rachelle", "Julia", "Rosie" ]
for name in girls:
  hello(name)
  print("Next girl")