# 📧 Automatic Email Sender using Python

This repository contains Python scripts to automate sending emails to multiple recipients using [Yagmail](https://github.com/kootenpv/yagmail) with Gmail App Password authentication and environment variable support via `python-dotenv`.

---

## ✨ Features

- 🔐 **Secure Credential Management**: Sensitive credentials stored safely in `.env` file (ignored by `.gitignore` so they won't be pushed to GitHub).
- 📧 **Multiple Sending Modes**:
  - `mailIDRecutier.py`: Styled HTML cold email template targeting recruiters with resume attachments and interactive callouts.
  - `main.py`: Batch automated email jobs sending grouped emails with attachments.
  - `main_1.py`: Interactive CLI tool to prompt for recipient, subject, content, CC, and BCC.
- 📎 **Attachments Support**: Easily attach images, PDFs, or documents.
- 🎨 **HTML Support**: Send responsive, clean HTML formatted emails.

---

## 📂 Project Structure

```text
automation-mail/
├── .env                # Secret environment variables (ignored by Git)
├── .env.example        # Template for environment configuration
├── .gitignore          # Git ignore rules for environment files, venv, and cache
├── README.md           # Documentation
├── mailIDRecutier.py   # Recruiter outreach script with HTML email template
├── main.py             # Bulk batch email sender script
├── main_1.py           # Interactive terminal CLI script
├── 1_old.jpeg          # Sample image attachment
├── 2_new.jpeg          # Sample image attachment
└── arpit-cloud-2.pdf   # Sample resume PDF attachment
```

---

## ⚙️ Prerequisites & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Apt1075/automatic-mail-send-using-python.git
cd automatic-mail-send-using-python
```

### 2. Install Dependencies
Ensure you have `yagmail` and `python-dotenv` installed:
```bash
pip install yagmail python-dotenv
```

### 3. Generate Gmail App Password
1. Go to your **[Google Account Security Settings](https://myaccount.google.com/security)**.
2. Enable **2-Step Verification**.
3. Under *2-Step Verification*, search for or navigate to **App passwords**.
4. Generate a new App Password (e.g. for "Mail" / "Python App").

---

## 🔐 Environment Configuration

Create a `.env` file in the root directory (or copy `.env.example`):

```env
SENDER_EMAIL=your-email@gmail.com
APP_PASSWORD=your-16-character-app-password
```

> ⚠️ **Security Note**: Never upload your `.env` file or credentials to GitHub. The `.gitignore` file is already configured to prevent `.env` from being tracked or committed.

---

## 🚀 Usage

### Option 1: Send Cold Emails / Recruiter Outreach
Runs `mailIDRecutier.py` which sends a styled HTML email with attached resume:
```bash
python mailIDRecutier.py
```

### Option 2: Run Batch Job Emailing
Runs `main.py` to iterate over configured email job dictionaries and dispatch batch messages with attachments:
```bash
python main.py
```

### Option 3: Interactive CLI Emailer
Runs `main_1.py` to enter recipient details, subject, content, CC, and BCC interactively in the terminal:
```bash
python main_1.py
```

---

## 🙋‍♂️ Author

Made with ❤️ by **Arpit Kumar**
- 🔗 **LinkedIn**: [linkedin.com/in/apt1075](https://www.linkedin.com/in/apt1075)
- 💻 **GitHub**: [github.com/Apt1075](https://github.com/Apt1075)