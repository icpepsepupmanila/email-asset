import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Email configuration
SMTP_SERVER = "smtp.gmail.com"  # Gmail's SMTP server
SMTP_PORT = 587  # Port for TLS
EMAIL_ADDRESS = "your-email@gmail.com"  # Your email address
EMAIL_PASSWORD = "your-email-password"  # Your email password or app password

# HTML email template as a string
EMAIL_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>ICPEP SE - PUP Manila Email Template</title>
    <style>
      /* Same styles as provided earlier */
    </style>
  </head>
  <body>
    <div class="container">
      <img
        src="https://raw.githubusercontent.com/icpepsepupmanila/email-asset/main/header.png"
        class="header-image"
      />
      <div class="body">
        <h1 class="title">Warmest Regards from the Computer Engineers of Tomorrow!</h1>
        <p class="message">
          Dear [recipient], <br /><br />
          [message]
          <br /><br />
          Best Regards, <br />
          <br />
          [sender]
        </p>
        <p class="tagline">Engineering Tomorrow, One Student at a Time</p>
        <div class="divider"></div>
        <img
          src="https://raw.githubusercontent.com/icpepsepupmanila/email-asset/main/ICPEP%20LOGO.png"
          class="footer-image"
        />
        <div class="social-container">
          <a href="https://www.facebook.com/icpepse.pupmanila">
            <i class="bi bi-facebook"></i>
          </a>
          <a href="https://www.instagram.com/icpep.se_pup?igsh=cThzcHptZ2ZmaWRx">
            <i class="bi bi-instagram"></i>
          </a>
          <a href="https://www.linkedin.com/in/gladwindr/">
            <i class="bi bi-linkedin"></i>
          </a>
        </div>
        <div class="footer">Copyright ©2024 ICPEP SE - PUP Manila</div>
      </div>
    </div>
  </body>
</html>
"""

# Function to send email
def send_email(recipient, message, sender):
    try:
        # Replace placeholders in the HTML template
        html_content = (
            EMAIL_TEMPLATE
            .replace("[recipient]", recipient)
            .replace("[message]", message)
            .replace("[sender]", sender)
        )

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = f"ICPEP SE - PUP Manila <{EMAIL_ADDRESS}>"
        msg['To'] = recipient
        msg['Subject'] = "Warmest Regards from the Computer Engineers of Tomorrow!"

        # Attach the HTML content
        msg.attach(MIMEText(html_content, "html"))

        # Connect to the SMTP server and send the email
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print(f"Email sent to {recipient} successfully!")

    except Exception as e:
        print(f"Failed to send email to {recipient}. Error: {e}")

# Read data from CSV
def send_emails_from_csv(csv_file):
    try:
        data = pd.read_csv(csv_file)
        for index, row in data.iterrows():
            send_email(
                recipient=row['recipient'],
                message=row['message'],
                sender=row['sender']
            )
    except Exception as e:
        print(f"Error reading CSV or sending emails: {e}")

# Run the function with your CSV file
send_emails_from_csv("email_data.csv")
