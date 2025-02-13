import smtplib
import csv
import configparser
import time
import random
from email.utils import formataddr

# Configuration
RESUME_LINK = "https://drive.google.com/your-resume-link"
RESUME_PASSWORD = "2024"
UNSUBSCRIBE_LINK = "https://bit.ly/your-unsubscribe"
YOUR_NAME = "Your Name"
YOUR_PHONE = "+1234567890"
YOUR_FIELD = "Software Development"  # Change to your field

def load_template():
    with open('email_template.txt', 'r') as f:
        return f.read()

def send_email(sender, password, receiver, first_name, company_name, position):
    template = load_template()
    
    # Personalize email
    email_content = template.format(
        first_name=first_name,
        company_name=company_name,
        position=position,
        resume_link=RESUME_LINK,
        resume_password=RESUME_PASSWORD,
        your_name=YOUR_NAME,
        your_phone=YOUR_PHONE,
        unsubscribe_link=UNSUBSCRIBE_LINK
    )
    
    # Split subject and body
    subject, body = email_content.split('\n\n', 1)
    subject = subject.replace('Subject: ', '').strip()
    
    # Create email
    msg = f"Subject: {subject}\n\n{body}"
    
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender, password)
            server.sendmail(
                from_addr=formataddr((YOUR_NAME, sender)),
                to_addrs=receiver,
                msg=msg.encode('utf-8')
            )
        return True
    except Exception as e:
        print(f"Error sending to {receiver}: {str(e)}")
        return False

def main():
    # Load config
    config = configparser.ConfigParser()
    config.read('config.ini')
    email_cfg = config['EMAIL']
    
    sent_count = 0
    daily_limit = int(email_cfg['DAILY_LIMIT'])
    
    with open('contacts.csv', 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if sent_count >= daily_limit:
                print(f"Stopped: Reached daily limit of {daily_limit} emails")
                break
                
            # Extract first name
            first_name = row['Name'].split()[0]
            
            # Random delay between 45-120 seconds
            delay = random.randint(45, 120)
            print(f"Waiting {delay} seconds before next email...")
            time.sleep(delay)
            
            # Send email
            if send_email(
                email_cfg['EMAIL_ADDRESS'],
                email_cfg['EMAIL_PASSWORD'],
                row['Email'],
                first_name,
                row['Company'],
                row['Title']
            ):
                sent_count += 1
                print(f"Sent to {row['Email']} ({sent_count}/{daily_limit})")
            else:
                print(f"Failed {row['Email']} - waiting 5 minutes")
                time.sleep(300)  # Wait 5 minutes on errors

if __name__ == "__main__":
    main()