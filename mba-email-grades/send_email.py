"""
Email Script

This script sends personalized messages to a list of recipients using a Gmail account.
It retrieves a list of unique email addresses from a contact list, and then sends the
same message to each recipient. The script uses the smtplib library for sending emails,
dotenv for loading email credentials from a .env file, and a custom 'contact_list' module
to get recipient information.

Libraries required:
- pip install smtplib
- pip install python-dotenv

Author: Suresh Paul
Date: October 15, 2023
"""

# Required Libraries
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from list import contact_list

# Load environment variables from a .env file
load_dotenv()

def get_unique_emails(contact_list):
    """Get a set of unique email addresses from the contact list."""
    return {email for _, email in contact_list.values()}

def send_email(email_user, email_password, recipient, subject, message):
    """Send an email."""
    try:
        # Create SMTP connection object
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            # Start TLS encryption on connection
            server.starttls()
            # Login to SMTP server with email and password
            server.login(email_user, email_password)
            # Create and configure the email message
            msg = MIMEMultipart()
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))
            # Send email
            server.sendmail(email_user, recipient, msg.as_string())
            print(f"Email sent to: {recipient}")
    except Exception as e:
        print(f"Error sending email to {recipient}: {e}")

def notify_by_email(contact_list,subject,message):
    # Sender's email credentials
    email_user = os.environ.get("EMAIL_USER")
    email_password = os.environ.get("EMAIL_PASSWORD")
    # Get unique recipient emails
    unique_emails = get_unique_emails(contact_list)
    # Email subject
    subject = f"{subject}"
    # Message
    message = message
    # Send email to each recipient
    for recipient in unique_emails:
        send_email(email_user, email_password, recipient, subject, message)