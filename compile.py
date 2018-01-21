import os, zipfile

# dir_name = '.'
# extension = ".zip"

# os.chdir(dir_name) # change directory from working dir to dir with files

path = "."
onid = ""
count  = 0
err = 0
for item in os.listdir(path):

	if os.path.isfile(item):
		pass
	elif os.path.isdir(item):
		try:
			onid = item
			item = path+'/'+item
			# print item

			os.chdir(item)
			os.system('pwd')
			os.system('git checkout ' + onid + '-assignment-1')		
			# TODO: Change assignment-1 to whatever assignment

			newpath = 'projects/'+onid+'/assignment-1/Calendar'		
			# TODO: Need to change for every path for new assignment submissions
			os.chdir(newpath)
			os.system('mvn compile')
			os.chdir('../../../../../')
			count += 1
		except Exception as e:
			# os.chdir('..')
			os.system('cd /z/362/')		# TODO: Fix to root directory of all student repos
			print 'ERROR: \t' + str(e)
			err += 1
			# pass


# os.system('pwd')
print 'count - ' + str(count)
print 'errors - ' + str(err)