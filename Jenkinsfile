pipeline {
    agent any

    environment {
        SCANNER_HOME = tool 'SonarQube'
        DOCKER_IMAGE = 'konda33/friday'
    }

    stages {
        stage('Checkout the code') {
            steps {
                git branch: 'main', url: 'https://github.com/ikonda-gosala/hal_mitra.git'
            }
        }

        stage('Install dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install --upgrade pip'
                sh 'venv/bin/pip install -r requirements.txt || true'
            }
        }

        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv(credentialsId: 'SonarQube', installationName: 'SonarQube') {
                    sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=new-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://13.220.244.70:9000
                    """
                }
            }
        }

        stage('Build Docker Image') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    dockerImage = docker.build("${DOCKER_IMAGE}:${env.BUILD_NUMBER}")
                }
            }
        }

        stage('Push to Docker Hub') {
            when {
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        dockerImage.push()
                        //dockerImage.push('latest')
                    }
                }
            }
        }

        stage('Update the deployment YAML'){
            when{
                expression { currentBuild.result == null || currentBuild.result == 'SUCCESS' }
            }
            steps{
                script {
                    git branch: 'main', url: 'https://github.com/ikonda-gosala/k8s.git'

                    sh """
                        sed -i 's|image: .*|image: ${DOCKER_IMAGE}:${env.BUILD_NUMBER}|g' k8s/deployment.yaml
                    """
                    sh """
                        git config user.email "gosalakonda2000@gmail.com"
                        git config user.name "ikonda-gosala"
                        git add "k8s/deployment.yaml"
                        git commit -m "Updted image with new build number:${env.BUILD_NUMBER}"
                    """
                }
            }
        }
    }
}
