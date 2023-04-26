pipeline {
  agent any 
  tools {
    maven 'maven'
  }

  stages {
    stage ('Initialize') {
      steps {
        sh '''
                    echo "PATH = ${PATH}"
                    echo "M2_HOME = ${M2_HOME}"
            ''' 
        }
      }
    stage ('Unit Test') {
      steps {
          sh 'mvn test  -Dmaven.test.failure.ignore=true'
      }   
    }
    
  }
}
