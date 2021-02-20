pipeline {
  agent any
  stages {
    stage('test-py36') {
      steps {
        sh 'tox -e py36'
      }
    }
    stage('distribute') {
      steps {
        sh 'echo hello'
      }
    }
    stage('deploy') {
      steps {
        sh 'echo jenkins'
      }
    }
  }
}
