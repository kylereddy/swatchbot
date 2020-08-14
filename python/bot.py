from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import swatch_image
import credentials
import traceback
import schedule
import smtplib
import tweepy
import time
import ssl

def main():
    # Send status email
    text = "SwatchBot started on " + \
    time.strftime("%b %d %Y at %H:%M:%S", time.localtime()) + "."

    send_status_email("SwatchBot Status", text)

    # Schedules uploadSwatch() to run at 9:00 AM every day
    schedule.every().day.at("09:00").do(uploadSwatch)

    try:
        print("RUNNING LOOP")
        # Runs program indefinitely and posts at 9:00 AM
        while True:
            schedule.run_pending()
            time.sleep(5)
    except:
        # Sends an email with details if the bot encounters an error
        text = "SwatchBot encountered the following error on " + \
                time.strftime("%b %d %Y at %H:%M:%S", 
                              time.localtime()) + \
                ":\n\n" + traceback.format_exc()

        send_status_email("SwatchBot ERROR", text)

def uploadSwatch():
    # Create authorization object
    auth = tweepy.OAuthHandler(credentials.CONSUMER_KEY, 
                               credentials.CONSUMER_SECRET)
    # Set auth object's access tokens
    auth.set_access_token(credentials.ACCESS_TOKEN, 
                          credentials.ACCESS_TOKEN_SECRET)
    # Connect to the Twitter API using the authorization object
    api = tweepy.API(auth, wait_on_rate_limit=True, 
                     wait_on_rate_limit_notify=True)

    # Send status email
    text = "SwatchBot passed Twitter API authentication on " + \
            time.strftime("%b %d %Y at %H:%M:%S", 
                          time.localtime()) + "."

    send_status_email("SwatchBot Status", text)

    print("GENERATING SWATCH")
    # Creates a new swatch image (called 'swatch.png')
    swatch_image.generateSwatch()

    print("ATTEMPTING TO POST")
    # Uploads the new swatch image to Twitter servers
    swatch = api.media_upload("swatch.png")

    # Posts the swatch to the bot's twitter account
    api.update_status(media_ids=[swatch.media_id])

    # Send status email
    text = "SwatchBot posted a new swatch on " + \
            time.strftime("%b %d %Y at %H:%M:%S", 
                          time.localtime()) + "."

    send_status_email("SwatchBot Status", text)

def send_status_email(subject, text):
    # Create email message
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = credentials.STATUS_EMAIL
    message["To"] = credentials.RECIPIENT_EMAIL

    # Create a plaintext version of the supplied string
    p_ptext = MIMEText(text, "plain")

    # Attach the plaintext to the message
    message.attach(p_ptext)

    # Create email server
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, 
                          context=context) as server:
        # Login to STATUS_EMAIL account
        server.login(credentials.STATUS_EMAIL, 
                     credentials.STATUS_EMAIL_PASS)
        # Send the email to RECIPIENT
        server.sendmail(credentials.STATUS_EMAIL, 
                        credentials.RECIPIENT_EMAIL, 
                        message.as_string())

main()