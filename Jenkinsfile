pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'loving_williamson'
    }

    stages {
        stage('stop and remove container') {
            steps {
                script {
                    // Stop and remove container if it exists
                    sh 'docker stop loving_williamson || true'
                    sh 'docker rm loving_williamson || true'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build("${env.DOCKER_IMAGE}")
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container
                    def dockerImage = docker.image("${env.DOCKER_IMAGE}")
                    dockerImage.run('-d -p 5000:5000 --name loving_williamson')
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image built and container started successfully.'
        }
    }
}
