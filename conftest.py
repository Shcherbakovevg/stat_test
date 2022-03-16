import pytest
import os.path

#Fixture to gathering information about failed tests
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    #Gathering information about tests
    outcome = yield
    rep = outcome.get_result()
    #Checking test result 
    if rep.when == "call" and rep.failed:
        #Set file open mode
        mode = "a" if os.path.exists("failures") else "w"
        #Wright failed test name (path(optional)module::class_name::function_name)
        with open("failures", mode) as f:
            if "tmpdir" in item.fixturenames:
                extra = " ({})".format(item.funcargs["tmpdir"])
            else:
                extra = ""
            f.write(rep.nodeid + extra + "\n")