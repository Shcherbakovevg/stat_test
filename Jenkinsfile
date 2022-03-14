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
      pytest --lf, --last-failed -v
    }
  }
}
