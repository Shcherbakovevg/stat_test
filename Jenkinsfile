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
      echo '${TEST_STDERR}'
      echo '${TEST_OVERVIEW}'
      sh 'pytest --last-failed -v'
    }
    always{
      junit (
       testResults: '**/surefire-reports/*.xml',
       testDataPublishers: [
         jiraTestResultReporter(
           configs: [
             jiraStringField(fieldKey: 'summary', value: '${DEFAULT_SUMMARY}'),
             jiraStringField(fieldKey: 'description', value: '${DEFAULT_DESCRIPTION}'),
             jiraStringArrayField(fieldKey: 'labels', values: [jiraArrayEntry(value: 'Jenkins'), jiraArrayEntry(value:'Integration')])
           ],
           projectKey: 'J2J',
           issueType: '1',
           autoRaiseIssue: false,
           autoResolveIssue: false,
           autoUnlinkIssue: false,
         )
       ]
      )
    }
  }
}
