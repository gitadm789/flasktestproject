




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

        stage('Save Docker Image as Tar') {
            steps {
                // Save Docker image as tar file in Jenkins workspace
                script {
                    sh "docker save -o ${WORKSPACE}/my-flask-app-image.tar my-flask-app-image"
                }
            }
        }
    }

    post {
        success {
            echo 'Docker image saved as tar file successfully.'
        }
    }
}
