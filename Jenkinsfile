




    pipeline {
    agent any

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    dockerImage = docker.build('my-flask-app-image')
                }
            }
        }

        
    }

    post {
        success {
            echo 'Docker image built successfully enjoy da.'
        }
    }
}
