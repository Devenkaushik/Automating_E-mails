# Automated Job Application System

A Python-based solution for sending personalized job applications to HR contacts via email, with anti-spam protection and deliverability optimization.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)  
![Gmail](https://img.shields.io/badge/Gmail-API%20Compatible-green)  
![License](https://img.shields.io/badge/License-MIT-lightgrey)

## Features

- 📧 **Bulk Email Sending** with personalized templates
- ⏳ **Intelligent Delay System** to mimic human behavior
- 📎 **Resume Sharing** via password-protected Google Drive links
- 🛡️ **Safety Features** to prevent account suspension
- 📊 **Daily Limits** configurable through a simple INI file
- ✅ **CAN-SPAM Compliance** with unsubscribe links

## Prerequisites

- Python 3.8+
- Gmail account with [App Password](https://myaccount.google.com/apppasswords)
- Resume PDF uploaded to Google Drive

## Installation

1. **Clone repository:**
   ```bash
   git clone https://github.com/yourusername/job-application-automation.git
   cd job-application-automation
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

### Email Setup (`config.ini`):
```ini
[EMAIL]
EMAIL_ADDRESS = your.email@domain.com
EMAIL_PASSWORD = your-app-password
DAILY_LIMIT = 20
```

### Contacts File (`contacts.csv`):
```csv
SNo,Name,Email,Title,Company
1,John Doe,john@company.com,HR Manager,Tech Corp
```

### Email Template (`email_template.txt`):
```txt
Subject: {Your Name} - {University} Grad for {Company} Roles

Hi {First Name},

[Your personalized message]
```

### Resume Setup:
1. Upload PDF to Google Drive.
2. Share with "Anyone with link".
3. Set password in code (`RESUME_PASSWORD`).

## Usage

- **Test with your personal email:**
  ```bash
  python main.py --test your@email.com
  ```

- **Full run (after testing):**
  ```bash
  python main.py
  ```

## Safety Considerations

- 🔐 **Never commit `config.ini` to version control**
- ⏰ **Minimum 45-second delay between emails**
- 📆 **Daily limit recommendations:**
  - First Week: **15 emails/day**
  - Subsequent Weeks: **30 emails/day**
- 🕒 **Best sending times:** Weekdays **10:30 AM - 3 PM** (recipient's timezone)

## Customization

Modify these components as needed:

### Email Template (`email_template.txt`):
- Add **personal achievements**.
- Include **specific skills**.
- Customize **call-to-action**.

### Safety Settings (`config.ini`):
```ini
[SAFETY]
MIN_DELAY = 45
MAX_DELAY = 120
MAX_RETRIES = 2
```

## Troubleshooting

| Error                  | Solution                                      |
|------------------------|-----------------------------------------------|
| Authentication Failed  | Verify App Password setup                    |
| Emails in Spam        | Check email content with [Mail-Tester](https://www.mail-tester.com/) |
| Resume Link Broken    | Re-upload PDF & update config                 |
| SMTP Connection Refused | Check firewall/antivirus settings           |

## Contributing

1. **Fork the repository**.
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/improvement
   ```
3. **Commit changes:**
   ```bash
   git commit -m 'Add new feature'
   ```
4. **Push to branch:**
   ```bash
   git push origin feature/improvement
   ```
5. **Open a Pull Request**.

## License

Distributed under the **MIT License**. See `LICENSE` for details.

## Disclaimer

This tool is for **educational purposes**. Ensure compliance with:

- **CAN-SPAM Act**
- **GDPR regulations**
- **Local anti-spam laws**

Use responsibly and respect recipients' privacy.
