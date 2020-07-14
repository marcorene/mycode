#!/usr/bin/env python3
import datetime
import random
import os
import ztest

print(datetime.datetime.now())
print(random.randint(0,10))
#os.system("ls")
print(datetime.date.today())
x = datetime.date.today()
print(x)
print(datetime.date.ctime(x))
ztest.main()
#print(ztest.main.myiplist())