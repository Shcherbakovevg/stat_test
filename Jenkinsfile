pipeline {
  agent { dockerfile true}
  stages {
    stage('test') {
      steps {
        echo '====Run test suite===='
        sh 'pytest -v test_stat.py'
      }
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
