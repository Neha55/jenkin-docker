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
    sh 'docker run -t -d --name test-container -u 492:482 -v /var/lib/jenkins/workspace/jenkins-docker-integration:/var/lib/jenkins/workspace/jenkins-docker-integration:rw,z -v /var/lib/jenkins/workspace/jenkins-docker-integration@tmp:/var/lib/jenkins/workspace/jenkins-docker-integration@tmp:rw,z -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** -e ******** jenkin-docker:tag1 python test.py'
    sh 'docker logs --follow test_c'
    }
}
