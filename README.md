# AutoBackupDatabase

## Yêu cầu:

### Python
Tải Python nếu chưa có tại đây: https://www.python.org/downloads/

### Required Python packages
```bash
pip install -r requirements.txt
```
### Tạo file .env
cần 1 file .env gồm có SENDER_EMAIL, APP_PASSWORD, RECEIVER_EMAIL
Lưu ý: APP_PASSWORD phải được tạo từ SENDER_EMAIL
```ini
SENDER_EMAIL=your_gmail_address@gmail.com
APP_PASSWORD=your_gmail_app_password
RECEIVER_EMAIL=receiver_email@gmail.com
```
