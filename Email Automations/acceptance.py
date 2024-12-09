import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os  # To access environment variables

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
your_email = "your_email@gmail.com"  # Replace with your email
your_password = "your_password"  # Replace with your email password

# Load the CSV file
df = pd.read_csv('email_data.csv')

# CC email list
cc_email_list = ["a@gmail.com", "b@gmail.com"]

# Email sending function
def send_email(recipient_email, recipient, message, sender):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Warmest Regards from the Computer Engineers of Tomorrow! 🎉"
    msg['From'] = "ICPEP SE - PUP Manila"
    msg['To'] = recipient_email
    msg['Cc'] = ', '.join(cc_email_list)

    # HTML content for the email
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <title>ICPEP SE - PUP Manila Email Template</title>
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
        />
        <style>
          @import url("https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;700&display=swap");

          body {{
            margin: 0;
            font-family: "IBM Plex Sans", sans-serif;
            background-color: #07003e;
            color: #000;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
          }}

          .container {{
            max-width: 600px;
            background: #ffffff;
            box-shadow: inset 0px 4px 4px rgba(0, 0, 0, 0.25);
            text-align: center;
          }}

          .header-image {{
            width: 100%;
            height: auto;
            display: block;
            margin: 0;
            padding: 0;
            border: none;
          }}

          .body {{
            padding: 20px;
          }}

          .title {{
            font-weight: 700;
            font-size: 16px;
            line-height: 24px;
            color: #07003e;
            margin: 20px 0;
          }}

          .message {{
            font-weight: 400;
            font-size: 14px;
            line-height: 20px;
            color: #000;
            margin: 20px 0;
            text-align: left;
          }}

          .title,
          .message {{
            padding-left: 40px;
            padding-right: 40px;
          }}

          .tagline {{
            font-style: italic;
            font-weight: 500;
            font-size: 16px;
            line-height: 24px;
            color: #07003e;
            margin: 20px 0;
          }}

          .divider {{
            width: 100%;
            height: 2px;
            background: #000;
            margin: 20px 0;
          }}

          .footer {{
            font-size: 13px;
            line-height: 19px;
            text-align: center;
            color: #000;
            margin: 20px 0;
          }}

          .social-container {{
            display: flex;
            justify-content: center;
            gap: 20px;
          }}

          .social-container img {{
            width: 24px;
            height: 24px;
          }}

          i {{
            color: black;
          }}

          .footer-image {{
            width: 102px;
            height: 112px;
            margin: 0;
          }}
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
          Dear {recipient}, <br /><br />
          {message}
          <br /><br />
          Best Regards, <br />
          <br />
          {sender}
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

    msg.attach(MIMEText(html_content, 'html'))

    # Combine recipient and CC addresses
    to_addresses = [recipient_email] + cc_email_list

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(your_email, your_password)
            server.sendmail(your_email, to_addresses, msg.as_string())
        print(f"Email sent successfully to {recipient} and CC'd to {', '.join(cc_email_list)}!")
    except Exception as e:
        print(f"Failed to send email to {recipient}: {e}")

# Iterate through the dataframe and send emails
for index, row in df.iterrows():
    send_email(row['Email'], row['First_Name'], row['Message'], row['Sender'])
