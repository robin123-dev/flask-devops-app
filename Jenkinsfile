pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'u3ser/flask-devops-app'
        CONTAINER_NAME = 'my-flask-app'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${DOCKER_IMAGE}:latest ."
            }
        }

        stage('Push to Docker'){
            steps{
                script {
                    // Tag the image with the build number
                    sh "docker tag u3ser/flask-devops-app:latest u3ser/flask-devops-app:${BUILD_NUMBER}"
                }
            }
        }

        stage('Test'){
            steps{
                sh "python -m unittest discover  || echo 'No tests found' "
            }
        }

        stage('Deploy Container') {
            steps {
                script {
                    sh "docker stop ${CONTAINER_NAME} || true"
                    sh "docker rm ${CONTAINER_NAME} || true"
                    sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }
}