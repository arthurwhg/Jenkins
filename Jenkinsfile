pipeline {
    agent { docker { image 'golang' } }
    stages {
        stage('build') {
            steps {
		echo 'Start go ...'
                sh 'go version'
            }
        }
    }
}
