pipeline{
    agent any
    stages {
        stage('Docker Image Build'){
            steps{
            bat 'docker build -t src .'
            }
        }
        stage('Docker Run Container'){
            steps{
                bat 'docker run --rm -i -p 5000:5000 src'
            }
        }
    }
}