node {
    def app

    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */
        checkout scm
    }

    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        docker.build("jenkin-docker:tag1")
    }

    stage('Test image') {
        /* Ideally, we would run a test framework against our image.
         * For this example, we're using a Volkswagen-type approach ;-) */

        docker.image("jenkin-docker:tag1").withRun(){
            docker.image("jenkin-docker:tag1").inside {
                sh 'echo "Executing test"'
                sh 'python test.py'
            }
        }
    }
}