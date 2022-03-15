pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        echo '+++++++++++++Run test suite+++++++++++++'
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          sh 'pytest -v test_stat.py'
          }
        sh 'rm  out_report.xml'
        sh 'rm  reportsout_report.xml '
        sh 'rm  -r allure-results'
        sh 'rm  -r  reports'
        sh 'rm  -r  test-reports'

      }
    }  
    stage('rerun failed tests'){
      steps{
        script{
          while (fileExists ('failures')){
            echo '+++++++++++++FAILED TESTS LIST+++++++++++++'
            sh 'cat failures'
            echo '+++++++++++++Rerun failed tests+++++++++++++'
            sh 'python3 test_rerun.py'
          }
        }
      }  
    }
  }
  post{
    always{
      junit allowEmptyResults: true, testResults: '**/*.xml'
    }
  }
}
