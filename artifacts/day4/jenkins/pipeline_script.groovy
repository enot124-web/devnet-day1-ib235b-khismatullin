pipeline {
    agent any

    stages {
        stage('Preparation') {
            steps {
                echo 'Preparation'
                git 'https://github.com/enot124-web/devnet-day1-ib235b-khismatullin'
            }
        }

        stage('Build') {
            steps {
                echo 'Build'
                sh 'cd "$WORKSPACE" && test -f sample-app/sample_app.py && grep -n "TOKEN_HASH8" sample-app/templates/index.html'
            }
        }

        stage('Results') {
            steps {
                echo 'Results'
                sh 'cd "$WORKSPACE" && ls -la && test -f src/day4_summary_builder.py'
            }
        }
    }
}
