import shutil
import os


def recursiveList(road,dst,ignored):
	dirs = os.listdir(road)
	for adir in dirs:
		curr = road+'/'+adir

		if adir in ignored:
			continue

		if(os.path.isdir(curr)):
			recursiveList(curr,dst,ignored)
		else:
			fname,fnext = os.path.splitext(curr)
			if(fnext == '.pdf'):
				shutil.copy(curr,dst+os.path.basename(curr))



ignore = {'cp',};
recursiveList('/home','cp/',ignore);



