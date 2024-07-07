pipeline {
    agent any
    
    environment {
        // Define the Docker image tag based on Jenkins build number
        DOCKER_IMAGE_TAG = "flaskapp:${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    def dockerImage = docker.build DOCKER_IMAGE_TAG, "--file Dockerfile ."
                    
                    // Save Docker image to Jenkins workspace
                    dockerImage.save("${env.WORKSPACE}/${DOCKER_IMAGE_TAG}.tar")
                }
            }
        }
        
        stage('Copy Docker Image') {
            steps {
                // Copy Docker image tarball to project directory
                sh "cp ${env.WORKSPACE}/${DOCKER_IMAGE_TAG}.tar ./"
            }
        }
    }
}
