pipeline{
    agent any
    environment {
        SCANNER_HOME = tool 'SonarQube'
    }

    stages{
        stage('Checkout the code'){
            steps{
                git branch: 'main', url: 'https://github.com/ikonda-gosala/hal_mitra.git'
            }
        }

        stage('Install dependies'){
            steps{
                sh 'python3 -m venv venv'
                sh 'venv/bin/pip install --upgrade pip'
                sh 'venv/venv/pip install -r requirements.txt || true'
            }
        }

        stage('SonarQube Analysis'){
            steps{
                withSonarQubeEnv('SonarQube'){
                    sh """
                        ${SCANNER_HOME}/bin/sonar-scanner \
                        -Dsonar.projectKey=new-project \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://13.220.244.70:9000 \
                        -Dsonar.login=sqp_238d822254dd235eec968b219c0ef7bf7a2d6cd1
                    """
                }
            }
        }

    }
    
}
