pipeline {
    agent none
    stages {

        stage('Clone repository')
            /* Let's make sure we have the repository cloned to our workspace */

            checkout scm
        }
        stage('Build image') {
            /* This builds the actual image; synonymous to
             * docker build on the command line */

            app = docker.build("jenkin-docker")
        }
        stage('Test image') {
            agent {
                    docker { image 'jenkin-docker:latest' }
                  }
            /* Ideally, we would run a test framework against our image.
             * For this example, we're using a Volkswagen-type approach ;-) */

            app.inside {
                sh 'echo "Executing test"'
                sh 'python /flask-app/test.py'
            }
        }
    }
}