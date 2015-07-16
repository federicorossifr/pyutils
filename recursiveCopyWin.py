import shutil
import os
import sys
import win32api

def recursiveList(road,dst,ignored,ext):
	dirs = os.listdir(road)  #list files or directories in root directory
	for adir in dirs:   
		curr = road+'\\'+adir #get path

		if adir in ignored:
			continue

		if(os.path.isdir(curr)):  #if directory recursive access it
			try:
				recursiveList(curr,dst,ignored,ext)
			except(PermissionError) as e:
				continue
		
		else:
			fname,fnext = os.path.splitext(curr) #get filename and extension
			if(fnext in ext): 
				print("Copied: "+curr,end='\n')

				try:
					shutil.copy(curr,dst+os.path.basename(curr))
				except(shutil.SameFileError) as er:
					continue
			else:
				print("Skipped: "+curr,end='\n')


start = win32api.GetLogicalDriveStrings()
start = start.split('\000')[:-1]
ignore = {'Windows','Program Files','Program Files (x86)'} #filter folder and files
srch = {'.pdf'} #filter files extensions

try:
	os.makedirs("recpy");
except(FileExistsError) as e:
	print('') 	
for s in start:
	recursiveList(s,'recpy/',ignore,srch)



