pipeline {
  agent any 
  tools {
    maven 'maven'
  }
  
  environment {
      DEPARTMENT_IMAGE = "deparment-service"
      REPO_NAME = "soulamarwen"
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
    stage ('Secret Detection'){
      steps {
        sh 'docker run --rm -v "$PWD:/pwd" trufflesecurity/trufflehog:latest github --repo https://github.com/MarwenSoula/DevSecOps-Project --json > trufflehog_report.json'
      }
    }
    stage ('Depencencies Check'){
      steps {
        dependencyCheck additionalArguments: '--format XML', odcInstallation: 'DP-Check'
      }
    }
    stage ('SAST SonarQube') {
      steps {
         withSonarQubeEnv('SonarQube') {
          sh 'mvn clean package sonar:sonar -Dmaven.test.failure.ignore=true'
        }
      }
    }
   stage ('Docker Build ') {
     steps {
       script{
         
         sh "docker rmi ${REPO_NAME}/${DEPARTMENT_IMAGE}:1.2 || true "
         sh "docker  build . -t ${REPO_NAME}/${DEPARTMENT_IMAGE}:1.2 -f ./department-service/Dockerfile
       
      }
     }
   }    
 
  }
}
