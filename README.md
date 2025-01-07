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

## Embedding in Microsoft Teams

1. **Host Your Flask App**: Ensure your Flask app is hosted and accessible over the internet.

2. **Create a Teams App Package**:
   - Update the `manifest.json` file with your app details and hosted URL.
   - Create a zip file containing `manifest.json`, `color.png`, and `outline.png`.

3. **Upload to Teams**:
   - Go to Microsoft Teams.
   - Click on "Apps" in the left sidebar.
   - Click on "Upload a custom app" and upload your zip file.

## Usage

- The application will display the time remaining until key events.
