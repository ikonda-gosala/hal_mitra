pipeline {
    agent {
        docker {
            image 'konda33/jenkins-python-docker-agent' // Custom image with Docker CLI
            args '-v /var/run/docker.sock:/var/run/docker.sock'
        }
    }

    environment {
        IMAGE_NAME = "konda33/hal_mitra"
    }

    stages {
        stage('Checkout from GitHub') {
            steps {
                git branch: 'main', url: 'https://github.com/ikonda-gosala/hal_mitra.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${IMAGE_NAME}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withDockerRegistry([credentialsId: 'dockerhub-creds', url: '']) {
                    script {
                        docker.image("${IMAGE_NAME}").push()
                    }
                }
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker rmi ${IMAGE_NAME}'
            }
        }
    }

    post {
        always {
            sh 'docker system prune -f'
        }
    }
}
