pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'rm -r .pytest_cache'
        echo '+++++++++++++Run test suite+++++++++++++'
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          sh 'pytest -v test_stat.py'
          }
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
}
