node {
    stage('Clone repository') {
        checkout scm
    }
    stage('Build image') {
        docker.build("jenkin-docker:tag1")
    }
    /*
    stage('Test image') {
        docker.image("jenkin-docker:tag1").withRun('-w /flask-app/'){
            docker.image("jenkin-docker:tag1").inside {
                sh 'echo "Executing test"'
                sh 'echo $PWD'
                sh 'python test.py'
            }
        }
    } */
    stage('Test image') {
    output = sh 'docker run -t -d jenkin-docker:tag1 python test.py'
    echo $output
    }
}
