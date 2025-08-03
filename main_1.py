import yagmail

to_email = input("Enter recipient email: ").strip()
cc_email = input("Enter CC email (optional, press Enter to skip): ").strip()
bcc_email = input("Enter BCC email (optional, press Enter to skip): ").strip()
subject = input("Enter email subject: ")
contents = input("Enter email contents: ")
if not to_email:
    print("Recipient email is required.")
    exit(1)
    
kwargs = {}
if cc_email:
    kwargs["cc"] = cc_email
if bcc_email:
    kwargs["bcc"] = bcc_email

try:
    yag = yagmail.SMTP("arpit.kumar1075@gmail.com", "dakwriyxkgnxqzcz")
    yag.send(to=to_email, subject=subject, contents=contents, **kwargs)
    print("Email sent successfully!")
except Exception as e:
    print("Failed to send email.")
    print("Error:", e)
