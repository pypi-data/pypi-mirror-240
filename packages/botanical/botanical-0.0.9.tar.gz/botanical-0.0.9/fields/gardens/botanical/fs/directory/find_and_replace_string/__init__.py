

'''
import botanical.fs.directory.find_and_replace_string as find_and_replace_string

import pathlib
from os.path import dirname, join, normpath
this_folder = pathlib.Path (__file__).parent.resolve ()
find_and_replace_string.start (
	glob_string = str (this_folder) + "/DB/**/*",

	FIND = 'region 1',
	REPLACE_WITH = 'region one'
)
'''

'''
import glob
glob.glob ('./[0-9].*')
'''




import glob
import os.path

def start (
	glob_string = "",
	
	find = "",
	replace_with = ""
):
	FILES = glob.glob (glob_string, recursive = True)

	for FILE in FILES:
		IS_FILE = os.path.isfile (FILE) 
	
		if (IS_FILE == True):
			print (FILE)

	for FILE in FILES:
		IS_FILE = os.path.isfile (FILE) 
	
		if (IS_FILE == True):			
			try:
				with open (FILE) as FP_1:
					ORIGINAL = FP_1.read ()
					NEW_STRING = ORIGINAL.replace (find, replace_with)
			
				if (ORIGINAL != NEW_STRING):
					print ("replacing:", FILE)
					
					with open (FILE, "w") as FP_2:
						FP_2.write (NEW_STRING)
			
			except Exception as E:
				print ("exception:", E)
				

