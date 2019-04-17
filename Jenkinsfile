pipeline {
  agent any
  stages {
    stage('update') {
      steps {
        sh 'ls'
      }
    }
    stage('build') {
        steps{
            sh 'python setup.py bdist_wheel'
            sh 'rm -rf .coverage'
            sh """coverage run --source=./hafweb/ -m hafweb run -ss=root:mengwei@localhost:3306/haf_publish -p=8803 &"""
            //sh """ps aux | grep 8083 | awk '{print \$2}' | tail -n 1 | xargs kill -9"""
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
