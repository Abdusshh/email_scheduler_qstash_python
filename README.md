# Email Scheduler

This project is an email scheduler that allows you to schedule and send emails at a later time.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/email-scheduler.git
    ```

2. Navigate to the project directory:

    ```bash
    cd email-scheduler
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    cd venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      .\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Set the required environment variables:

    Replace `QSTASH_TOKEN`, `QSTASH_URL`, `SENDGRID_API_KEY`, and `SENDGRID_SENDER_EMAIL_ADDRESS` with your own values.

## Usage

1. Run the application:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000/scheduler/schedule-email`.

3. Follow the instructions on the web page to schedule and send emails.