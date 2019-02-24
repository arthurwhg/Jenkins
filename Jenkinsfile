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
                sh '''
                	pwd
			touch /Users/artwang2/Documents/GitHub/Jenkins/${DIR}
                    	ls -lah > /Users/artwang2/Documents/GitHub/Jenkins/${DIR}
                    	echo "Hello World! " ${DIR} >> /Users/artwang2/Documents/GitHub/Jenkins/${DIR}
                '''
            }
        }
    }
}
