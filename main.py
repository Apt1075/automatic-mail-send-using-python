import yagmail

sender_email = "arpit.kumar1075@gmail.com"
app_password = "dakwriyxkgnxqzcz"

email_jobs = [
    {
        "to": ["arpit.kumar.101196@gmail.com", "gauravkumaraura7@gmail.com","sau150997k@gmail.com"],
        "cc": ["sau150997k@gmail.com"],
        "bcc": [],
        "subject": "Automated Email - Group 1",
        "contents": [
            "Hello Team,",
            "This is a test email for Group 1 sent from a Python script.",
        ],
        "attachments": [
            "D:/python/automation mail/1_old.jpeg",
             "D:/python/automation mail/2_new.jpeg"
        ]
    },
    {
        "to": ["gauravkumaraura7@gmail.com"],
        "cc": ["sau150997k@gmail.com"],
        "bcc": [],
        "subject": "Automated Email - Group 2",
        "contents": [
            "Hi,",
            "This is another automated email for Group 2.",
        ],
        "attachments": [
            "D:/python/automation mail/2_new.jpeg"
        ] 
    },

]

try:
    yag = yagmail.SMTP(user=sender_email, password=app_password)

    for idx, job in enumerate(email_jobs, start=1):
        try:
            print(f" Sending email to group {idx}...")
            yag.send(
                to=job["to"],
                subject=job["subject"],
                contents=job["contents"],
                cc=job.get("cc", []),
                bcc=job.get("bcc", []),
                attachments=job.get("attachments", [])
            )
            print(f"Group {idx} email sent successfully!")
        except Exception as e:
            print(f"Failed to send email to group {idx}.")
            print("Error:", e)

except Exception as e:
    print("Failed to send one or more emails.")
    print("Error:", e)
