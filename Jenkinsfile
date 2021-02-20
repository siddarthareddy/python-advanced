pipeline {
  agent any
  stages {
    stage('set up') {
      steps {
        sh 'python3 -m venv venv'
        sh 'venv/bin/pip3 install --upgrade pip'
        sh 'venv/bin/pip3 install -e '.[all]''
      }
    }    
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
