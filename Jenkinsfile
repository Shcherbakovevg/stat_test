pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'pytest --reruns 5 -v'
      }   
    }
    stage('test_2') {
      steps {
        testcompletetest suite: 'https://github.com/Shcherbakovevg/stat_test.git'
      }   
    }
  }
  post{
    always{
      allure includeProperties: false, jdk: '', results: [[path: 'allure-results']]
    }
  }
}
