pipeline {
  agent any
  stages {
    stage('Initiate') {
      steps {
        sh 'echo "Start to build server on "'
      }
    }
    stage('Plan') {
      input {
        message 'Approval:'
        id 'Approved'
        parameters {
          string(name: 'DIR', defaultValue: 'Approved', description: 'Approved comments')
        }
      }
      steps {
        sh '''
			cd "/Users/artwang2/Documents/My Jar/terraform-provider-aws/examples/two-tier"
			echo ${DIR} > ./approved 
			terraform init -input=false >./build.log
			terraform plan -input=false >> ./build.log               	
                '''
      }
    }
    stage('Build') {
      steps {
        sh '''
			cd "/Users/artwang2/Documents/My Jar/terraform-provider-aws/examples/two-tier"
			terraform apply "/Users/artwang2/Documents/My Jar/terraform-provider-aws/examples/two-tier/plan" -input=false >> ./build.log
		'''
      }
    }
    stage('Done') {
      steps {
        sh '''
                        cd "/Users/artwang2/Documents/My Jar/terraform-provider-aws/examples/two-tier"
                        terraform show
               '''
      }
    }
  }
}