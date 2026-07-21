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

        stage('Deploy Container') {
            steps {
                script {
                    // stop and remove existing container if it exists
                sh "docker stop my-flask-app || true"
                sh "docker rm my-flask-app || true"
                // Run new container
                sh "docker run -d -p 5000:5000 --name my-flask-app ${DOCKER_IMAGE}:latest"
            }
        }
    }
}