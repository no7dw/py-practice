import sys
import os

print("script name is", sys.argv[0])
if len(sys.argv)>1:
  print("there are" ,len (sys.argv)-1, "arguments:")
  for arg in sys.argv[1:]:
    print(arg)
else:
  print("there are no arguments!")

for path in os.environ["PATH"].split(os.pathsep):
  print(path)

