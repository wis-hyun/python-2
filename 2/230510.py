#1
import sys
print(sum(map(int, sys.argv[1:])))

#2
import os
result = os.popen('dir')
print(result.read())

#3
import glob
print(glob.glob("d:/secondpython/2회고사/*.py"))
