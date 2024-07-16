pipeline {
    agent any

    environment {
        AWS_DEFAULT_REGION = 'ap-south-1'
        AWS_CREDENTIALS_ID = 's3Test'
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/teshchaudhary/jenkins-sandbox'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    bat 'pip install boto3'
                }
            }
        }

        stage('Run Python Script') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', credentialsId: env.AWS_CREDENTIALS_ID]]) {
                    bat 'python create_glue_crawler.py'
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: '**/create_glue_crawler.py', allowEmptyArchive: true
            cleanWs()
        }
    }
}
