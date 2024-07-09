


pipeline {
    agent any

    stages {


        stage('stop and remove container') {
            steps {
                script {
                    // stop
                    sh 'docker stop loving_williamson || true'
                    sh 'docker rm loving_williamson || true'
                }
            }
        }



        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    def dockerImage = docker.build('loving_williamson')
                }
            }
        }


        


        stage('Run Docker Container') {
            steps {
                script {
                    // Run Docker container
                    def dockerImage = docker.build('loving_williamson')
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
