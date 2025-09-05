pipeline {
    agent any

    environment {
        SONAR_TOKEN = credentials('SonarQubeToken')
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/ikonda-gosala/hal_mitra.git'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('sonarqube') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=friday-project \
                          -Dsonar.sources=. \
                          -Dsonar.host.url=http://13.220.244.70:9000 \
                          -Dsonar.python.version=3.8 \
                          -Dsonar.login=$SONAR_TOKEN
                    '''
                }
            }
        }
    }
}
