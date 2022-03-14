pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'pytest --reruns 5 -v'
      }   
    }
  }
}
