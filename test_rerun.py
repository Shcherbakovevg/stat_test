import pytest
import os

failure_list = []

file = open('failures')
for line in file:
	failure_list.append(line.strip("\n"))
file.close()
os.remove('failures')

#test_arg = ' '.join(failure_list)
#print (test_arg)
for test in failure_list:
	retcode = pytest.main(['-v', test])
#rerun = pytest.main(['-v', test_arg])