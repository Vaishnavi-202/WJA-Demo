pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    PYTHON_EXE = "C:\\Users\\vaishnavi.m\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
    VENV_DIR = ".venv"
    ALLURE_RESULTS = "reports\\allure-results"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Verify tools') {
      steps {
        bat '''
          "%PYTHON_EXE%" --version
          "%PYTHON_EXE%" -m pip --version
        '''
      }
    }

    stage('Set up venv') {
      steps {
        bat '''
          if exist %VENV_DIR% rmdir /s /q %VENV_DIR%
          "%PYTHON_EXE%" -m venv %VENV_DIR%
          call %VENV_DIR%\\Scripts\\activate.bat
          python -m pip install --upgrade pip
        '''
      }
    }

    stage('Install dependencies') {
      steps {
        bat '''
          call %VENV_DIR%\\Scripts\\activate.bat
          python -m pip install -r requirements.txt
        '''
      }
    }

    stage('Run tests') {
      steps {
        bat '''
          call %VENV_DIR%\\Scripts\\activate.bat
          if exist %ALLURE_RESULTS% rmdir /s /q %ALLURE_RESULTS%
          python -m pytest --alluredir=%ALLURE_RESULTS%
        '''
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/**', allowEmptyArchive: true
    }
  }
}
