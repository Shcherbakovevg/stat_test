pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        echo '====Run test suite===='
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          sh 'cat failures'
          sh 'pytest -v test_stat.py'
          }
      }
    }  
    stage('Collect failed tests'){
      steps{
        sh 'cat failures'
      }

    }
    stage('rerun failed tests'){
      steps{
        script{
          if (fileExists ('failures')){
            echo '====Rerun failed tests===='
            sh 'python3 test_rerun.py'
            sh 'cat failures'
          }
          else{
            echo '====All tests are passed===='
          }

        }
      }  
    }
  }
}
