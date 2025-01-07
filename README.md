# DaysUntil Project

## Installation

1. **Install Python**: Download and install Python from [python.org](https://www.python.org/downloads/).

2. **Install Requirements**: Open your terminal, navigate to the project directory, and run:
   ```sh
   pip install -r requirements.txt
   ```

## Setup

1. **Project Structure**:
   ```
   DaysUntil/
   ├── app.py
   ├── requirements.txt
   ├── templates/
   │   └── index.html
   └── manifest/
       └── manifest.json
   ```

2. **Run the Application**:
   - Navigate to the project directory in the terminal.
   - Run the application using:
     ```sh
     python app.py
     ```

3. **Access the Application**:
   - Open your web browser and go to `http://127.0.0.1:5000/`.


## Deploying to Heroku

1. **Create a `Procfile`**: In the root directory of your project, create a file named `Procfile` with the following content:
   ```
   web: python app.py
   ```

2. **Create a `requirements.txt`**: Ensure you have a `requirements.txt` file in your project directory with all the dependencies listed.

3. **Create a `runtime.txt`**: In the root directory of your project, create a file named `runtime.txt` with the following content:
   ```
   python-3.8.10
   ```

4. **Initialize a Git Repository**:
   ```sh
   git init
   git add .
   git commit -m "Initial commit"
   ```

5. **Create a Heroku App**:
   ```sh
   heroku create your-app-name
   ```

6. **Deploy to Heroku**:
   ```sh
   git push heroku master
   ```

7. **Open the App**:
   ```sh
   heroku open
   ```

## Usage

- The application will display the time remaining until key events.
