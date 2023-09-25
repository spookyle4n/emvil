import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from getpass import getpass

# Email configuration
sender_email = "slimprowallet@gmail.com"
receiver_email = "wyattjgierer@gmail.com"
subject = "Test Email"
message = "This is a test email sent from Python."

# Get the sender's password securely
password = getpass("Enter your email password: ")

# Create a MIME message
msg = MIMEMultipart()
msg["From"] = sender_email
msg["To"] = receiver_email
msg["Subject"] = subject

# Attach the message to the email
msg.attach(MIMEText(message, "plain"))

# Connect to the SMTP server (in this case, Gmail's SMTP server)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()  # Start TLS encryption
    server.login(sender_email, password)  # Login to the email account

    # Send the email
    server.sendmail(sender_email, receiver_email, msg.as_string())

    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    server.quit()  # Quit the SMTP server
