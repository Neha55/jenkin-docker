node {
    stage('Clone Repository') {
        checkout scm
    }
    stage('Build Image') {
        /*docker.build("jenkin-docker:tag1")*/
        sh '/usr/local/bin/docker-compose --verbose build'
    }
    
    stage('Test Image') {
        try{
            sh 'echo $PWD'
            sh '/usr/local/bin/docker-compose up -d'
            sh 'docker exec -i test_container bash -c "python test.py"' > fail_logs.log
        }
        catch (Exception e) {
            emailext attachLog: true,
                     attachmentsPattern: 'fail_logs.log',
                     subject: 'Jenkins Build $BUILD_TAG - FAILURE', 
                     to: 'nebidkar@in.ibm.com',
                     body: 'Build failed. Please check the logs.'
            throw e;
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
