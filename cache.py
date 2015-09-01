import shutil
import os

count = 0
exceptions = ['data_0','data_1','data_2','data_3','index']
os.chdir(os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Cache'))
files = os.listdir()

for filee in files:
	if filee not in exceptions:
		os.remove(os.path.expanduser(r'~\AppData\Local\Google\Chrome\User Data\Default\Cache\\' + filee))
		count += 1

if len(os.listdir()) == 5:
	input('\n' + str(count) + ' files have been deleted')
else:
	input('Something went wrong (')

exit()
