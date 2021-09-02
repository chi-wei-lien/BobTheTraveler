#!/usr/bin/env python
import glob, os
import subprocess
from sys import argv
import time

day = 0

#get all file
allFile = []
allDir = []

for root, dirs, files in os.walk(os.getcwd()):
	for file in files:
		if file.endswith(".py"):
			if(file == "bob%s.py" % day):
				continue
			allFile.append(os.path.join(root, file))
			allDir.append(root)
			# print(os.path.join(root, file))

#midify file
fileOrder = 0

# time.sleep(3)
if fileOrder >= len(allFile):
	exit()

with open(allFile[fileOrder], "r") as f:
	lines = f.readlines()

with open(allFile[fileOrder], "w") as f:
	lines.insert(0, "#============BOB the Traveler============\n")
	lines.insert(1, "#==========Travel Diary. Day %d==========\n" % day)
	lines.insert(2, "#               @   @@\n")
	lines.insert(3, "#                    @(\n")
	lines.insert(4, "#            ,@@@@@@@@@@@@@&\n")
	lines.insert(5, "#            @/       @@\n")
	lines.insert(6, "#           @          @@\n")
	lines.insert(7, "#          .@   (       @\n")
	lines.insert(8, "#           @           @\n")
	lines.insert(9, "#        *  @          @\n")
	lines.insert(10,"#     @      @@      @@\n")
	lines.insert(11,"#   @@           @  @\n")
	lines.insert(12,"#  @@  @@@@  @@ @     ,  @\n")
	lines.insert(13,"#  @  *  % &@   @     @   %@\n")
	lines.insert(14,"# @@  %    @     @   (@    @#\n")
	lines.insert(15,"# @(   .   @     @    @     @\n")
	lines.insert(16,"# &@ #,    @     @    @@@   @\n")
	lines.insert(17,"#  @       @. @@ @     @ @  @\n")
	lines.insert(18,"#   @       @ @@       @  @ @.\n")
	lines.insert(19,"#   %@   @@ @@@@       @   @@\n")
	lines.insert(20,"#    @      @  @   @@  @@\n")
	lines.insert(21,"#     /@@@@@@@ @   @@   @\n")
	lines.insert(22,"#              @   @(@  @\n")
	lines.insert(23,"#              @   @ @  @@\n")
	lines.insert(24,"#              @@  @ @   @\n")
	lines.insert(25,"#               @@@   @ .@\n")
	lines.insert(26, "#===========Traveled locations===========\n")
	for addr in range(day):
		lines.insert((27+addr), "#%s\n" % allFile[addr])
	lines.insert(27+day, "#========================================\n")
	f.write("".join(lines))

#change previous file
if (fileOrder - 1) >= 0:
	with open(allFile[fileOrder-1], "r") as f:
	    lines = f.readlines()

	previous_file = open(allFile[fileOrder-1], "w")
	lineHeight = 27 + day
	countLine = 0
	for line in lines:
		if countLine < lineHeight:
			countLine += 1
		else:
			previous_file.write(line)
	previous_file.close()

#self replicate
nextday = day + 1
name = str(argv[0])
newFileName = "bob%d.py" % nextday
if(name == "bob0.py"):
	command = "cp " + os.getcwd() + "/" + name + " " + allDir[day] + "/" + newFileName
else:
	command = "cp " + name + " " + allDir[day] + "/" + newFileName
print(command)
subprocess.call(command, shell=True)

#edit clone
file = open(allDir[day] + "/" + newFileName, "r")
lines = file.readlines()
file.close()

new_file = open(allDir[day] + "/" + newFileName, "w")
avoidLine = "day = %d" %day
newLine = "day = %d" %(day+1)
avoidOrderLine = "fileOrder = %d" % fileOrder
newOrderLine = "fileOrder = %d" % (fileOrder+1)

for line in lines:
	if line.strip("\n") == avoidLine:
		new_file.write(newLine)
		new_file.write("\n")
	elif line.strip("\n") == avoidOrderLine:
		new_file.write(newOrderLine)
		new_file.write("\n")
	else:
		new_file.write(line)

new_file.close()


if (day-1) >= 0:
	deleteCommand = "rm %s/bob%d.py" % (allDir[day-1], day)
	subprocess.call(deleteCommand, shell=True)
else:
	deleteCommand = "rm bob%d.py" % (day)
	subprocess.call(deleteCommand, shell=True)

launchCommand = "python3 %s/bob%d.py" % (allDir[day], nextday)
subprocess.call(launchCommand, shell=True)
