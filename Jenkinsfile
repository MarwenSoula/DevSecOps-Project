pipeline {
  agent any 
  tools {
    maven 'maven'
  }
  
  environment {
      DEPARTMENT_IMAGE = "deparment-service"
      EMPLOYEE_IMAGE = "employee-service"
      ORGANIZATION_IMAGE = "organization-service"
      GATEWAY_IMAGE = "gateway-service"
      DOCKER_REPO = "soulamarwen"
      DOCKERHUB_PWD = "Soula&20403411"
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
    stage ('Unit Test') {
      steps {
          sh 'mvn test -Dmaven.test.failure.ignore=true '
      }   
    }
    stage ('Build Maven') {
      steps {
          sh 'mvn clean package -Dmaven.test.failure.ignore=true '    
       }
    }
   stage ('Docker Build ') {
     steps {
       script{
         sh "docker rmi ${DOCKER_REPO}/${DEPARTMENT_IMAGE}:1.2 || true "
         sh "docker  build -f department-service/Dockerfile -t ${DOCKER_REPO}/${DEPARTMENT_IMAGE}:1.2 department-service  "
         
         sh "docker rmi ${DOCKER_REPO}/${EMPLOYEE_IMAGE}:1.2 || true "
         sh "docker  build -f employee-service/Dockerfile -t ${DOCKER_REPO}/${EMPLOYEE_IMAGE}:1.2 employee-service  "
         
         sh "docker rmi ${DOCKER_REPO}/${ORGANIZATION_IMAGE}:1.2 || true "
         sh "docker  build -f organization-service/Dockerfile -t ${DOCKER_REPO}/${ORGANIZATION_IMAGE}:1.2 organization-service  " 
         
         sh "docker rmi ${DOCKER_REPO}/${GATEWAY_IMAGE}:1.2 || true "
         sh "docker  build -f gateway-service/Dockerfile -t ${DOCKER_REPO}/${GATEWAY_IMAGE}:1.2 gateway-service  " 
         
        
      } 
     }
   }  
   stage ('Scan Docker Image Trivy') {
      steps {
          sh " trivy image --format json -o trivy-${DEPARTMENT_IMAGE}.json   ${DOCKER_REPO}/${DEPARTMENT_IMAGE}:1.2 "
          sh " trivy image --format json -o trivy-${EMPLOYEE_IMAGE}.json     ${DOCKER_REPO}/${EMPLOYEE_IMAGE}:1.2 "
          sh " trivy image --format json -o trivy-${ORGANIZATION_IMAGE}.json ${DOCKER_REPO}/${ORGANIZATION_IMAGE}:1.2 "
          sh " trivy image --format json -o trivy-${GATEWAY_IMAGE}.json   ${DOCKER_REPO}/${GATEWAY_IMAGE}:1.2 "
          
      }
    }
   stage ('DockerHub Push Image') {
      steps {
          withCredentials([usernamePassword(credentialsId: 'DOCKERHUB', passwordVariable: 'password', usernameVariable: 'dockerhub')]) {
            sh " docker login --username soulamarwen --password "Soula&20403411" "
          } 
          
      }
     }
    
    stage ('Kubernetes Deployment') {
      steps {
        sh " ls "
      } 
    }
      
  
  }
}
