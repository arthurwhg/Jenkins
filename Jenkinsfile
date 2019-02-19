pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
		    touch /Users/artwang2/Documents/GitHub/Jenkins/abc
                    ls -lah
                '''
            }
        }
    }
}
