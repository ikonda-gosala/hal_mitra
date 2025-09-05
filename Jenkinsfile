pipeline {
    agent any 
    
    stages { 
        stage('SCM Checkout') {
            steps{
           git branch: 'main', url: 'https://github.com/ikonda-gosala/hal_mitra.git'
            }
        }
        // run sonarqube test
        stage('Run Sonarqube') {
            environment {
                scannerHome = tool 'SonarQube';
            }
            steps {
              withSonarQubeEnv(credentialsId: 'SonarQubeToken', installationName: 'SonarQube') {
                sh "${scannerHome}/bin/sonar-scanner"
              }
            }
        }
    }
}
