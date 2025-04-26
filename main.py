import os
import smtplib
from dotenv import load_dotenv
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import shutil
import schedule
import time

load_dotenv()

# Mail config
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
APP_PASSWORD = os.getenv("APP_PASSWORD")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")

# Backup config
BACKUP_FOLDER = "backup"
DB_FILES = [os.path.join(os.getcwd(), "database", "opencart.sql")]


def send_email(subject, body):
    message = MIMEMultipart()
    message['From'] = SENDER_EMAIL
    message['To'] = RECEIVER_EMAIL
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain', 'utf-8'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, APP_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, message.as_string())
        print(f"Email đã được gửi đến {RECEIVER_EMAIL}")
        server.quit()
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")

def backup_sql():
    try:
        os.makedirs(BACKUP_FOLDER, exist_ok=True) 
        for db_file in DB_FILES:
            if os.path.exists(db_file):
                dst = os.path.join(BACKUP_FOLDER, os.path.basename(db_file))
                shutil.copy2(db_file, dst)     
        send_email("Sao lưu thành công", "Database đã được sao lưu.")
    except Exception as e:
        send_email("Sao lưu thất bại", f"Lỗi: {str(e)}")
        print("Lỗi khi sao lưu:", e)

schedule.every().day.at("14:12").do(backup_sql)
print("Bắt đầu lịch trình sao lưu. Các đợt sao lưu sẽ bắt đầu vào nửa đêm mỗi ngày.")
while True:
    schedule.run_pending()
    time.sleep(60)
