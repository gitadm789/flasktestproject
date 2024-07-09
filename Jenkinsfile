


pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    def dockerImage = docker.build('my-flask-app-image')
                }
            }
        }


        



        stage('stop and remove container') {
            steps {
                script {
                    // stop
                    sh 'docker stop my-flask-app-image || true'
                    sh 'docker rm my-flask-app-image || true'
                }
            }
        }

        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container
                    def dockerImage = docker.build('my-flask-app-image')
                    dockerImage.run('-d -p 5000:5000')
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
