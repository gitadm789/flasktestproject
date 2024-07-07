pipeline {
    agent any
    
    stages {
        stage('Build') {
            steps {
                script {
                    // Build Docker image
                    def dockerImage = docker.build("yourdockerusername/flaskapp:${env.BUILD_NUMBER}")

                    // Push Docker image to Docker Hub (or your Docker registry)
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials') {
                        dockerImage.push()
                    }
                }
            }
        }
    }
}
