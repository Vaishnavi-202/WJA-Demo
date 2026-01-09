pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    VENV_DIR = ".venv"
    ALLURE_RESULTS = "reports/allure-results"
    ALLURE_REPORT = "reports/allure-report"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Set up Python venv') {
      steps {
        sh '''
          python3 --version
          python3 -m venv ${VENV_DIR}
          . ${VENV_DIR}/bin/activate
          python -m pip install --upgrade pip
        '''
      }
    }

    stage('Install dependencies') {
      steps {
        sh '''
          . ${VENV_DIR}/bin/activate
          pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        sh '''
          . ${VENV_DIR}/bin/activate
          pytest
        '''
      }
    }

    stage('Install Allure CLI') {
      steps {
        sh '''
          sudo apt-get update
          sudo apt-get install -y default-jre curl tar
          curl -fsSL -o allure.tgz https://github.com/allure-framework/allure2/releases/download/2.27.0/allure-2.27.0.tgz
          tar -xzf allure.tgz
          sudo rm -rf /opt/allure
          sudo mv allure-2.27.0 /opt/allure
          sudo ln -sf /opt/allure/bin/allure /usr/local/bin/allure
          allure --version
        '''
      }
    }

    stage('Generate Allure HTML') {
      steps {
        sh '''
          allure generate ${ALLURE_RESULTS} -o ${ALLURE_REPORT} --clean || true
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/allure-results/**', allowEmptyArchive: true
      archiveArtifacts artifacts: 'reports/allure-report/**', allowEmptyArchive: true
    }
  }
}
