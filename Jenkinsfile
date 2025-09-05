pipeline {
    agent any

    tools {
        // This must match the name of the SonarQube Scanner configured in Jenkins
        sonarQubeScanner 'SonarQube'
    }

    environment {
        // Replace with your actual SonarQube token ID stored in Jenkins credentials
        SONAR_TOKEN = credentials('SonarQubeToken')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ikonda-gosala/hal_mitra.git' // Replace with your actual repo
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') { // This must match the name of the SonarQube server in Jenkins
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=friday-project \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://13.220.244.70:9000 \
                          -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }
    }
}
