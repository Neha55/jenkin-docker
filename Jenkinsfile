node {
    stage('Clone repository') {
        /* Let's make sure we have the repository cloned to our workspace */
        checkout scm
        sh 'echo $PWD'
    }
    stage('Build image') {
        /* This builds the actual image; synonymous to
         * docker build on the command line */

        docker.build("jenkin-docker:tag1")
    }
    stage('Test image') {
        /* docker.image("jenkin-docker:tag1").run{c -> */
            docker.image("jenkin-docker:tag1").inside {
                sh 'echo "Executing test"'
                sh 'echo $PWD'
                sh 'python test.py'
            }
        /* } */
    }
}