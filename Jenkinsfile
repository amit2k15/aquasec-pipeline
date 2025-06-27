pipeline {
    agent any
    
    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/amit2k15/aquasec-pipeline.git'
            }
        }
        stage('Run Python Script') {
            steps {
                sh 'python3 process_excel.py'
            }
        }
        stage('Commit Results') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'github-creds', usernameVariable: 'GIT_USER', passwordVariable: 'GIT_PASS')]) {
                    sh '''
                        git config user.name "$GIT_USER"
                        git config user.email "amitkumarnayak2k15@gmail.com"
                        git add aquasec_summary.csv
                        git commit -m "Add processed output"
                        git push https://$GIT_USER:$GIT_PASS@github.com/your-username/aquasec-pipeline.git HEAD:main
                    '''
                }
            }
        }
    }
}