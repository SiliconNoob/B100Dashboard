pipeline {
    agent any

    stages {
        stage('Get Data') {
            steps {
                echo 'Running scraping script'
                bat 'python Scraping/scrap.py'
            }
        }

        stage('Upload Data') {
            steps {
                echo 'Uploading....'
            }
        }
    }
}