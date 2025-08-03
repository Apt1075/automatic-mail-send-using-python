# 📧 Automatic Email Sender using Python

This project is a simple Python script to automate sending emails to multiple recipients using [Yagmail](https://github.com/kootenpv/yagmail), with support for:

- ✅ Multiple To/CC/BCC recipients
- 📎 Attachments (e.g., images, PDFs)
- 🧾 Custom subject and message
- 🔁 Sending emails in bulk using a loop

---

## 🚀 Features

- Send emails via Gmail using App Password
- Supports multiple recipients per email
- Individual customization per email job (to, cc, bcc, subject, contents, attachments)
- Attach any file type
- Easy-to-modify Python dictionary

---

## 📂 Folder Structure

automation-mail/

- main.py # Core email sending script
- main_1.py # Older version or alternate test script
- 1_old.jpeg # Sample attachment 1
- 2_new.jpeg # Sample attachment 2
- README.md # Project description
- .gitignore # Ignores virtualenv, etc.

## ⚙️ Setup

1. **Clone the repo**:

   git clone https://github.com/Apt1075/automatic-mail-send-using-python.git
   cd automatic-mail-send-using-python

2. **Install dependencies:**   
    pip install yagmail

3. **Enable Gmail App Password:**  
    Go to Google Account Security
    Enable 2-step verification
    Generate an App Password for “Mail” and “Windows Computer”
    Use this app password in main.py
4. **🔐 Configure Email Details**   
    sender_email = "your-email@gmail.com"
app_password = "your-app-password"

email_jobs = [
    {
        "to": ["recipient1@example.com"],
        "cc": ["cc@example.com"],
        "bcc": [],
        "subject": "Test Email",
        "contents": [
            "Hello,",
            "This is a test email from the automated Python script.",
        ],
        "attachments": ["1_old.jpeg", "2_new.jpeg"]
    },
    ...
]


5. **🧪 Run the Script**

   python main.py

6. **📧 Check Email**

   Check your inbox for the sent emails.

7. **🙋‍♂️ Author**
    Made with ❤️ by Arpit Kumar 