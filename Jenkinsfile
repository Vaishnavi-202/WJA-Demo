pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    // Use double backslashes OR use forward slashes.
    PYTHON_EXE = "C:\\Users\\vaishnavi.m\\AppData\\Local\\Programs\\Python\\Python314\\python.exe"
    VENV_DIR = ".venv"
    ALLURE_RESULTS = "reports\\allure-results"
    ALLURE_REPORT  = "reports\\allure-report"
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
          python -m pytest
        '''
      }
    }

    stage('Install Allure CLI (Windows)') {
      steps {
        bat '''
          where allure >nul 2>nul
          if %ERRORLEVEL%==0 (
            echo Allure already installed
            allure --version
          ) else (
            echo Allure not found. Installing via Scoop...
            powershell -NoProfile -ExecutionPolicy Bypass -Command "if (-not (Get-Command scoop -ErrorAction SilentlyContinue)) { iwr -useb get.scoop.sh | iex }"
            powershell -NoProfile -ExecutionPolicy Bypass -Command "scoop install allure"
            allure --version
          )
        '''
      }
    }

    stage('Generate Allure HTML') {
      steps {
        bat '''
          if not exist %ALLURE_RESULTS% (
            echo Allure results folder not found: %ALLURE_RESULTS%
            exit /b 0
          )
          allure generate %ALLURE_RESULTS% -o %ALLURE_REPORT% --clean
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
