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
    failure{
      sh 'pytest --lf, --last-failed -v'
    }
  }
}
