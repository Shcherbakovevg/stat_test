pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'python3 -m pytest test_stat.py'
      }   
    }
  }
}
