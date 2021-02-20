pipeline {
  agent {
    dockerfile {
      filename 'jenkins.Dockerfile'
      additionalBuildArgs (
        '--build-arg PYTHON_VERSION=3.7 '
      )
      args (
        '-ti ' +
        '-u jenkins:jenkins ' +
        '-v /var/run/docker.sock:/var/run/docker.sock '
      )
    }
  }
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
