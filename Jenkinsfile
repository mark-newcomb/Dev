// pipeline {
//     agent any
//
//     stages {
//         stage('Build') {
//             steps {
//                 echo 'Building..'
//             }
//         }
//         stage('Test') {
//             steps {
//                 echo 'Testing..'
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying....'
//             }
//         }
//     }
// }

        pipeline {
            agent any
            stages {
//                 stage('Checkout') {
//                     steps {
//                         git 'https://www.github.com/mark-newcomb/Dev' // Replace with your repo URL
//                     }
//                 }
                stage('Build with PyBuilder') {
                    steps {
                        sh '''
                            python3 -m venv pybuilder_env
                            source pybuilder_env/bin/activate
                            pip install pybuilder
                            pyb
                        '''
                    }
                }
            }
        }
