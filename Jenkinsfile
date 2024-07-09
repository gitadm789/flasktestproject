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

        
    }

    post {
        success {
            echo 'Docker image built and container started successfully.'
        }
    }
}



