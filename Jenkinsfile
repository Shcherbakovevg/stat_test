pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        sh 'set +e'
        echo '====Run test suite===='
        sh 'pytest -v test_stat.py'
        catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
          sh "exit 1"
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
            echo '====Rerun filed tests===='
            sh 'pytest -v test_rerun.py'
          }
          else{
            echo '====All tests are passed===='
          }

        }
      }  
    }
  }
}
