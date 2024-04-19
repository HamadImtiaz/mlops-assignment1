pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from the main branch
                  git branch: 'master', url: 'https://github.com/HamadImtiaz/mlops-assignment1.git'
            }
        }
        
        stage('Build and Push Docker Image') {
            steps {
                script {
                    // Build Docker image
                    docker.build('hamadimtiaz/mlops:v1')
                    
                    // Authenticate with Docker Hub
                    docker.withRegistry('', 'docker-credentials') {
                        // Push Docker image to Docker Hub
                        docker.image('hamadimtiaz/mlops:v1').push()
                    }
                }
            }
        }
    }
    
    post {
        success {
           
            emailext subject: 'Docker Image Notification Email',
                      body: 'The Docker image for your application has been successfully built and pushed to Docker Hub.',
                      to: 'hamadimtiaz015@gmail.com'
        }
        failure {
            
            emailext subject: 'Failed to build and push Docker image',
                      body: 'There was an error while building and pushing the Docker image to Docker Hub.',
                      to: 'hamadimtiaz015@gmail.com'
        }
    }
}