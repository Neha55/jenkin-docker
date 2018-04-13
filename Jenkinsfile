pipeline {
    agent none
    stages {
        stage('build') {
             steps {
            echo 'This is a minimal pipeline.'
            }
        }
        stage('build') {
            agent {
                    docker { image 'jenkin-docker:latest' }
                  }
        }
    }
}
