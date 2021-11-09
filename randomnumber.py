#!/usr/bin/env python3
import random, time, sys
print()
print()
counter = 0
while counter < 1000:
 counter +=1
 num= random.randint(1,1000)
 numtext = str(num)
 sys.stdout.write("\r" + "   " + numtext + "  ")
 sys.stdout.flush()
#  print(num, end="\r", flush=True)
 time.sleep(1)
