import pytest
import os

failure_list = []
#Reading failed tests names
file = open('failures')
for line in file:
	failure_list.append(line.strip("\n"))
file.close()
#Delete temp file
os.remove('failures')

#test_arg = ' '.join(failure_list)
#print (test_arg)
#Rerun tests (in case of tests fail temp file failures creating)
for test in failure_list:
	retcode = pytest.main(['-v', test])
#rerun = pytest.main(['-v', test_arg])