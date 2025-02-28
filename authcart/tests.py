import smtplib

EMAIL_HOST = "smtp.office365.com"
EMAIL_PORT = 587
EMAIL_USER = "your-email@outlook.com"  # Replace with your email
EMAIL_PASS = "your-app-password"  # Replace with the App Password

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()  # Secure connection
    server.login(EMAIL_USER, EMAIL_PASS)
    print("✅ Login successful!")
    server.quit()
except Exception as e:
    print("❌ Error:", e)


