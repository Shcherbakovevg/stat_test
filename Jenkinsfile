pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'set +e'
        sh 'pytest -v'
      }   
    }
  }
  post{
    failure{
      sh 'pytest --last-failed -v'
    }
  }
}
