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
//        sh 'python3 /usr/src/app/scripts/distribute.py'
      }
    }
    stage('deploy') {
      steps {
//        sh 'python3 /usr/src/app/scripts/deploy.py'
      }
    }
  }
}
