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
      echo ${TEST_STDERR}
      echo ${TEST_OVERVIEW}
      sh 'pytest --last-failed -v'
    }
  }
}
