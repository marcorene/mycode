import datetime
import os

print(datetime.datetime.today())
os.system("cd ~/mycode")
os.system("git add *")
os.system('git commit -m "another line"')
os.system("git push origin master")
