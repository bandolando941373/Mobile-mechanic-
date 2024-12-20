from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/api/submit-request', methods=['POST'])
def submit_request():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    # Send an email
    msg = MIMEText(f"You received a new request from {name} ({email}): \n\n{message}")
    msg['Subject'] = 'New Request from Website'
    msg['From'] = 'your_email@example.com'  # Replace with your email
    msg['To'] = 'your_email@example.com'  # Replace with your email

    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
        smtp.starttls()
        smtp.login('your_email@example.com', 'your_password')  # Replace with your email and password
        smtp.sendmail(msg['From'], msg['To'], msg.as_string())

    return jsonify({'message': 'Request submitted successfully!'}), 200
