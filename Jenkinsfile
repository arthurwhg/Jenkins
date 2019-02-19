pipeline {
    agent any
    stages {
        stage('Build') {
           input {
             	message "Folder Name:"
               	ok "Done"
                parameters {
       	            string(name: 'DIR', defaultValue: 'abc', description: 'Folder name')
               	}
    	   }	
            steps {
		sh 'echo "Hello World" ${DIR}'
                sh '''
                    echo "Multiline shell steps works too"
		    touch /Users/artwang2/Documents/GitHub/Jenkins/${DIR}
                    ls -lah
                '''
            }
        }
    }
}
