node {
    stage('Clone repository') {
        properties([pipelineTriggers([[$class: 'GitHubPushTrigger'], pollSCM('H/15 * * * *')])])
        checkout scm
    }
    stage('Build image') {
        docker.build("jenkin-docker:tag1")
    }
    
    stage('Test image') {
        sh 'docker run -t -d --name test-container -u 492:482 -v /var/lib/jenkins/workspace/jenkins-docker-integration:/var/lib/jenkins/workspace/jenkins-docker-integration:rw,z -v /var/lib/jenkins/workspace/jenkins-docker-integration@tmp:/var/lib/jenkins/workspace/jenkins-docker-integration@tmp:rw,z jenkin-docker:tag1 python test.py'
        sh 'docker logs --follow test-container'
        sh 'docker rm test-container'
    }
    
    /*
    stage('Test image compose') {
    sh 'docker-compose -f docker-compose.yaml -d run'
    sh 'docker logs --follow test-container'
    } */
}
