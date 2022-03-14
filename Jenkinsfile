pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'pytest -v set +e'
      }   
    }
  }
  post{
    failure{
      sh 'pytest --last-failed -v'
    }
  }
}
