
# PassGuard - Web Password Manager + Security Scanner

PassGuard is a web-based password manager built with Flask, SQLite, and Python. It securely stores user passwords with Fernet encryption and provides basic security testing against common vulnerabilities like SQL Injection. This project is designed to help users safely manage their passwords while showcasing basic web security practices.

## Key Features

- **User Registration:** Users can create accounts by registering their username and password.
- **Password Encryption:** User passwords are securely encrypted using Fernet encryption before being stored in the database.
- **SQLite Database:** User data and encrypted passwords are stored in a simple, serverless SQLite database.
- **Responsive UI:** The interface is built using Bootstrap, making it mobile-friendly and easy to navigate.
- **Basic Security Testing:** Includes a module to test for SQL Injection vulnerabilities to help ensure the application is secure.

## Technologies Used

- **Flask:** A lightweight web framework for Python used to build the backend.
- **SQLite:** A simple, serverless database used for storing user data.
- **Python:** The backend logic is written in Python.
- **Bootstrap:** Used to create a responsive and modern frontend interface.
- **Fernet Encryption:** Ensures passwords are securely encrypted before being stored.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/PassGuard.git
   cd PassGuard
   ```

2. Set up a virtual environment (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/Mac
   venv\Scripts\activate     # For Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up your environment variables by creating a `.env` file in the root directory with the following content:
   ```
   FLASK_APP=app.py
   FLASK_ENV=development
   ```

5. Run the application:
   ```bash
   flask run
   ```

6. Open your browser and go to `http://127.0.0.1:5000/` to start using the application.

## Usage

- **Register:** Users can create an account by entering a username and password.
- **Store Passwords:** After logging in, users can store and retrieve their encrypted passwords.
- **Security Testing:** The application includes basic security features, such as testing for SQL Injection vulnerabilities.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository, make your changes, and submit a pull request. Contributions and improvements are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Made with ❤️ for learners by [Erfan](https://github.com/Erphs)
