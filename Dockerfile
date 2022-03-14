FROM python
MAINTAINER shcherbakoveugeniy@gmail.com
COPY . /python-test
WORKDIR /python-test
RUN pip install --no-cache-dir -r requirements.txt && pip install pytest-rerunfailures
