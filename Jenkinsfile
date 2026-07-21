cd ~/devops_learning

# Create the jenkinsfile
cat > jenkinsfile << 'EOF'
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
                sh "docker rm -f ${CONTAINER_NAME} || true"
                sh "docker run -d -p 5000:5000 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}:latest"
            }
        }
    }
}
EOF

# Add, commit, and push to GitHub
git add jjenkinsfile
git commit -m "Add jenkinsfile for CI/CD pipeline"
git push origin main