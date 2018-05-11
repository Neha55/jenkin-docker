node {
    stage('Clone Repository') {
        checkout scm
    }
    stage('Build Image') {
        /*docker.build("jenkin-docker:tag1")*/
        sh '/usr/local/bin/docker-compose build'
    }
    
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
        emailext attachLog: true, 
                body: 'Jenkins Build Logs \n BUILD_NUMBER : $BUILD_NUMBER \n BUILD_ID: $BUILD_ID \n BUILD_URL : $BUILD_URL', 
                recipientProviders: [developers()], 
                subject: 'Jenkins Build $BUILD_TAG Logs', 
                to: 'nebidkar@in.ibm.com'
    }
}
