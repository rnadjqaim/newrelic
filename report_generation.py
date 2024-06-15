# report_generation.py
import requests
import json
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

NEW_RELIC_API_KEY = 'your_api_key'
NEW_RELIC_ACCOUNT_ID = 'your_account_id'
NEW_RELIC_API_URL = f'https://api.newrelic.com/v2/applications.json'
SMTP_SERVER = 'smtp.example.com'
SMTP_PORT = 587
SMTP_USERNAME = 'your_email@example.com'
SMTP_PASSWORD = 'your_email_password'
RECIPIENT_EMAIL = 'recipient@example.com'

def fetch_performance_data():
    headers = {'Api-Key': NEW_RELIC_API_KEY}
    response = requests.get(NEW_RELIC_API_URL, headers=headers)
    return response.json()

def generate_report(data):
    report_html = '<html><body>'
    report_html += '<h
