node {
    stage('Clone Repository') {
        checkout scm
    }
    stage('Build Image') {
        /*docker.build("jenkin-docker:tag1")*/
        sh '/usr/local/bin/docker-compose build'
    }
    
    /*
    stage('Test image') {
        sh 'docker run -t -d --name test-container -u 492:482 -v /var/lib/jenkins/workspace/jenkins-docker-integration:/var/lib/jenkins/workspace/jenkins-docker-integration:rw,z -v /var/lib/jenkins/workspace/jenkins-docker-integration@tmp:/var/lib/jenkins/workspace/jenkins-docker-integration@tmp:rw,z jenkin-docker:tag1 python test.py'
        sh 'docker logs --follow test-container'
        sh 'docker rm test-container'
    }*/
    
    
    stage('Test Image') {
        try{
            sh 'echo $PWD'
            sh '/usr/local/bin/docker-compose up -d'
            sh 'docker exec test_container python test.py'
        }
        finally{
            sh 'docker rm -f test_container'
        }
    }
    
    stage('Notify') {
        emailext attachLog: true, body: 'Jenkins Build Logs', recipientProviders: [developers()], subject: 'Jenkins Build Logs', to: 'nebidkar@in.ibm.com'
    }
}
