pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                input {
                	message "Folder Name:"
                	ok "Done"
	                parameters {
        	            string(name: 'DIR', defaultValue: 'abc', description: 'Folder name')
                	}
            	}	
		sh 'echo "Hello World"'
                sh '''
                    echo "Multiline shell steps works too"
		    touch /Users/artwang2/Documents/GitHub/Jenkins/${DIR}
                    ls -lah
                '''
            }
        }
    }
}
