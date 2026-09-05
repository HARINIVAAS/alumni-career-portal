pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('SonarQube Analysis') {
            steps {
                script {
                    def scannerHome = tool 'SonarScanner'

                    withSonarQubeEnv('SonarQube') {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=alumni-career-portal \
                            -Dsonar.sources=.
                        """
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t alumni-portal .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker stop alumni-portal-container || true'
                sh 'docker rm alumni-portal-container || true'
                sh 'docker run -d --name alumni-portal-container -p 5000:5000 alumni-portal'
            }
        }
    }
}
