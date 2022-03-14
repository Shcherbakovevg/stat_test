pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'python3 -m pytest --reruns 5 test_stat.py'
      }   
    }
  }
}
