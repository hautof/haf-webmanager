pipeline {
  agent any
  stages {
    stage('update') {
      steps {
        sh 'ls'
      }
    }
    stage('build') {
      steps {
        sh 'python setup.py bdist_wheel'
	sh 'echo EOF | coverage run --source=./hafweb/ -m hafweb run -ss=root:mengwei@localhost:3306/haf_publish'
	sh 'coverage report'
      }
    }
    stage('check') {
      steps {
        sh 'ls dist'
      }
    }
  }
}
