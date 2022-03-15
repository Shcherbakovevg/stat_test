import pytest
import os.path


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # выполняем все остальные хуки, чтобы получить report object
    outcome = yield
    rep = outcome.get_result()

    # мы ищем только вызовы упавших тестов, а не setup/teardown
    if rep.when == "call" and rep.failed:
        mode = "a" if os.path.exists("failures") else "w"
        with open("failures", mode) as f:
            # давайте ради прикола посмотрим на фикстуру
            if "tmpdir" in item.fixturenames:
                extra = " ({})".format(item.funcargs["tmpdir"])
            else:
                extra = ""

            f.write(rep.nodeid + extra + "\n")