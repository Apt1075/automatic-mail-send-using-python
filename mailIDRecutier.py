import yagmail

sender_email = "arpit.kumar1075@gmail.com"
app_password = ""  # Use App Password only

# List of recipient email IDs
recipients = [
    "arpit.kumar.101196@gmail.com",
]

subject = "Application for Cloud & DevOps Engineer"

email_body = [
    "Dear Hiring Team,",
    "",
    "I hope you are doing well.",
    "",
    "I am writing to apply for the Cloud & DevOps Engineer position. I have hands-on experience in designing and managing AWS infrastructure, building CI/CD pipelines, and automating infrastructure using Terraform. I have also worked extensively with Docker, Kubernetes, and Linux-based systems.",
    "",
    "My experience includes monitoring production systems, implementing security best practices, troubleshooting issues, and optimizing cloud costs. I am passionate about building reliable, scalable, and secure cloud platforms.",
    "",
    "Please find my resume attached for your review. I would welcome the opportunity to discuss how my skills and experience can add value to your team.",
    "",
    "Thank you for your time and consideration.",
    "",
    "Best regards,",
    "Arpit Kumar",
    "Cloud & DevOps Engineer",
    "+91 80095 69030",
    "LinkedIn: https://www.linkedin.com/in/apt1075",
    "Portfolio: https://arpit-portfolio-tau.vercel.app"
]

attachments = [
    "D:/python/automation mail/arpit-cloud-2.pdf"
]

try:
    yag = yagmail.SMTP(user=sender_email, password=app_password)

    for email in recipients:
        print(f"Sending email to {email}...")
        yag.send(
            to=email,
            subject=subject,
            contents=email_body,
            attachments=attachments
        )
        print(f"Email sent successfully to {email}")

except Exception as e:
    print("Error sending emails:", e)
