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
            step('build one'){
                sh 'python setup.py bdist_wheel'
                sh 'rm -rf .coverage'
            }
            step{
                try{
                    sh 'echo EOF | coverage run --source=./hafweb/ -m hafweb run -ss=root:mengwei@localhost:3306/haf_publish'
                }catch(Exception e){
                    print(e.toString())
                }
            }
            step{
                sh 'coverage report'
            }
        }
    }
    stage('check') {
      steps {
        sh 'ls dist'
      }
    }
  }
}
