pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'pytest -v'
      }   
    }
  }
  post{
    always{
      sh 'pytest --last-failed -v'
    }
  }
}
