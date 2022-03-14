pipeline {
  agent { dockerfile true}
  stages {
    stage('build') {
      steps {
        sh 'pip install --no-cache-dir --upgrade pip --user'
        sh 'pip install --no-cache-dir -r requirements.txt --user'
      }
    }
    stage('test') {
      steps {
        sh 'python3 -m pytest test_stat.py'
      }   
    }
  }
}
