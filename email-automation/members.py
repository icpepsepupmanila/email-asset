import smtplib
import pandas as pd
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os  # To access environment variables

# SMTP configuration
smtp_server = 'smtp.gmail.com'
smtp_port = 587
your_email = "email@gmail.com"  # Replace with your email
your_password = "password"  # Replace with your email password

# CC email list
cc_email_list = []
  

# Email sending function
def send_email(recipient_email, recipient):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Welcome to ICPEP SE - PUP Manila, {recipient}! 🎉"
    msg['From'] = "ICPEP SE - PUP Manila"
    msg['To'] = recipient_email
    msg['Cc'] = ', '.join(cc_email_list)

    # HTML content for the email
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
      <table style="border-collapse:collapse;table-layout:fixed;border-spacing:0;vertical-align:top;min-width:320px;Margin:0 auto;background-color:#07003e;width:100%;" cellpadding="0" cellspacing="0">
        <tbody>
          <tr style="vertical-align:top">
            <td style="word-break:break-word;border-collapse:collapse!important;vertical-align:top">
              <div style="padding:0;background-color:transparent;width:100%;max-width:650px;margin:0 auto;word-wrap:break-word;background-color:#ffffff">
                <table role="presentation" cellpadding="0" cellspacing="0" width="100%" style="font-family:'Source Sans Pro',sans-serif">
                  <tr>
                    <td align="center" style="padding:0;">
                      <img src="https://raw.githubusercontent.com/icpepsepupmanila/email-asset/main/header.png" alt="Header" style="display:inline-block;width:100%;max-width:650px;border:none;height:auto;">
                    </td>
                  </tr>
                </table>
              </div>

              <div style="padding:0px;background-color:transparent">
                <div style="margin:0 auto;min-width:320px;max-width:650px;word-wrap:break-word;word-break:break-word;background-color:#ffffff">
                  <div style="border-collapse:collapse;display:table;width:100%;height:100%;background-color:transparent">
                    <div style="max-width:650px;min-width:320px;display:table-cell;vertical-align:top;background-color:#ffffff;height:100%;width:100%!important;">
                      <table style="font-family:'IBM Plex Sans', sans-serif; width:100%; border:0;" role="presentation" cellpadding="0" cellspacing="0">
                        <tr>
                          <td style="padding-top:24px; text-align:center; word-break:break-word;">
                            <h2 style="margin:0; font-size:16px; font-weight:400; color:#07003E; line-height:140%;"><strong>Warmest Regards from the Computer Engineers of Tomorrow!</strong></h2>
                          </td>
                        </tr>
                      </table>

                      <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td style="word-break:break-word;padding-top:24px;padding-right:40px;padding-left:40px;color:#07003E;font-family:'IBM Plex Sans',sans-serif;" align="left">
                              <div style="font-size:14px;line-height:160%;text-align:center;word-wrap:break-word">
                                <p style="line-height:160%;text-align:justify"><strong>Dear {recipient},</strong></p>
                              </div>
                              <div style="font-size:14px;line-height:160%;text-align:center;word-wrap:break-word">
                                <p style="line-height:160%;text-align:justify">Welcome to the <strong>Institute of Computer Engineers of the Philippines Student Edition - PUP Manila Chapter</strong> for the 2024-2025 school year! As a new member, you are now part of a community dedicated to providing a home for all computer engineering students—one that offers not just opportunities for academic and professional growth, but also a place where you will find a sense of belonging.</p>
                              </div>
                              <div style="font-size:14px;line-height:160%;text-align:center;word-wrap:break-word">
                                <p style="line-height:160%;text-align:justify"><strong>ICPEP SE - PUP Manila</strong> began in 2024 when we proudly affiliated with the ICPEP network, the national organization for computer engineers. This partnership opens up exciting opportunities for both students and professionals alike, and we are thrilled to be part of a larger community that fosters growth, collaboration, and progress within the field of computer engineering.</p>
                              </div>
                              <div style="font-size:14px;line-height:160%;text-align:center;word-wrap:break-word">
                                <p style="line-height:160%;text-align:justify">We are excited to have you with us and can’t wait to see all the amazing things we will accomplish together in the coming year. Should you have any questions or need support, please feel free to reach out to any of us.</p>
                              </div>
                              <div style="font-size:14px;line-height:160%;text-align:center;word-wrap:break-word">
                                <p style="line-height:160%;text-align:justify">To get started, we invite you to join our Facebook group and Discord channel. These platforms are great ways to stay updated on announcements, events, and opportunities, and to engage with fellow members of the community.</p>
                              </div>  
                              <div style="font-size:14px;line-height:100%;text-align:center;word-wrap:break-word">
                                <p>
                                    <strong>Facebook Group:</strong> <a href="https://www.facebook.com/groups/icpepsepupmanila" style="text-decoration: none; font-weight: bold;" target="_blank">Join here</a>
                                </p>
                                <p>
                                    <strong>Discord Channel:</strong> <a href="https://discord.gg/Bwdz3UhhXR" style="text-decoration: none; font-weight: bold;" target="_blank">Join here</a>
                                </p>
                              </div>
                              <div style="font-size:14px;line-height:160%;text-align:center;word-wrap:break-word">
                                <p style="line-height:160%;text-align:justify">Best Regards,</p>
                                <p style="line-height:10%;text-align:justify"><strong>Your ICPEP SE - PUP Manila Family</strong></p>
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td style="word-break:break-word;padding-top:24px;align:center">
                              <h2 style="margin:0px;line-height:140%;text-align:center;word-wrap:break-word;font-size:18px;font-weight:500;color:#07003E">
                                <i>Engineering Tomorrow, One Student at a Time</i>
                              </h2>
                            </td>
                          </tr>
                        </tbody>
                      </table>

                      <table role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
                        <tbody>
                          <tr>
                            <td style="word-break:break-word;padding-top:24px;align:center">
                              <div style="width:80%;height: 2px;background: #282424;margin:20px;padding-left:40px;padding-right:40px;"></div>
                              <div style="text-align: center;">
                                <img src="https://github.com/icpepsepupmanila/email-asset/blob/main/icpep-logo.png?raw=true" style="width: 140px; height: 156px;" />
                              </div>
                              <div style="text-align: center; margin: 20px 0;">
                                <a href="https://www.facebook.com/icpepse.pupmanila" style="display: inline-block; width: 18px; height: 18px; padding: 0 10px;">
                                  <img src="https://github.com/icpepsepupmanila/email-asset/blob/main/facebook.png?raw=true" alt="Facebook" style="width: 18px; height: 18px;"/>
                                </a>
                                <a href="https://www.instagram.com/icpep.se_pup?igsh=cThzcHptZ2ZmaWRx" style="display: inline-block; width: 18px; height: 18px; padding: 0 10px;">
                                  <img src="https://github.com/icpepsepupmanila/email-asset/blob/main/instagram.png?raw=true" alt="Instagram" style="width: 18px; height: 18px;"/>
                                </a>
                                <a href="https://www.linkedin.com/company/icpepse-pupmanila" style="display: inline-block; width: 18px; height: 18px; padding: 0 10px;">
                                  <img src="https://github.com/icpepsepupmanila/email-asset/blob/main/linkedin.png?raw=true" alt="LinkedIn" style="width: 18px; height: 18px;"/>
                                </a>
                              </div>

                              <div style="padding-left: 72px;padding-right: 72px;font-size: 12px;font-weight: 600;line-height: 18px;text-align: center;color: #07003E;margin: 20px 0;">
                                Share your excitement with us, feel free to post this welcome message on your social media and tag us!
                              </div>
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
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

if __name__ == "__main__":
  # Load the CSV file
  df = pd.read_csv('form2.csv')
  print(df)

  # Iterate through the dataframe and send emails
  for index, row in df.iterrows():
    send_email(row['Email'], row['First_Name'])
