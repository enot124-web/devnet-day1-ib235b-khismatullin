pipeline { stages { stage('Preparation'){steps{echo 'Preparation'}} stage('Build'){steps{echo 'Build'}} stage('Results'){steps{echo 'Results'}} } }
