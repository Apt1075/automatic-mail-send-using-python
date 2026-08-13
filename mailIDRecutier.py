import os
import yagmail
from dotenv import load_dotenv

load_dotenv()

sender_email = os.getenv("SENDER_EMAIL", "")
app_password = os.getenv("APP_PASSWORD", "")

recipients = [
    "arpit.kumar@theingen.com"
]

subject = "Application for Backend Developer | Python & FastAPI - Arpit Kumar"

# Clean HTML template without extra linebreaks
html_email_body = """
<div style="font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #333333; line-height: 1.5; max-width: 620px; margin: 0 auto; padding: 15px; border: 1px solid #e0e0e0; border-radius: 6px; background-color: #ffffff;">
  <p style="margin: 0 0 12px 0;">Dear Hiring Team,</p>
  <p style="margin: 0 0 12px 0;">I hope this email finds you well.</p>
  <p style="margin: 0 0 12px 0;">I am writing to express my interest in <strong>Backend Developer</strong> opportunities within your engineering team. I bring <strong>3.5+ years of experience</strong> building high-performance, scalable backend systems and REST APIs with expertise in <strong>Python, FastAPI, MongoDB, Redis, Docker, and AWS</strong>.</p>
  <p style="margin: 0 0 12px 0;">In my current role, I architect telemetry ingestion pipelines and microservices for enterprise logistics platforms—processing data from <strong>80,000+ active vehicles</strong> and <strong>150K+ daily GPS records</strong>, successfully reducing API processing latency by <strong>40%</strong>. I have also integrated LLM-powered conversational interfaces and computer vision inspection systems (YOLOv8).</p>
  
  <!-- Featured AI Project Callout Card -->
  <div style="background-color: #f7fafc; border-left: 4px solid #3182ce; border-radius: 5px; padding: 12px 16px; margin: 14px 0;">
    <div style="font-weight: bold; color: #1a202c; font-size: 14px; margin-bottom: 4px;">🤖 Featured AI Project: HireMe AI Assistant</div>
    <div style="color: #4a5568; font-size: 13px; margin-bottom: 8px;">An interactive ChatGPT-style portfolio AI trained directly on my backend experience and resume.</div>
    <a href="https://hire-me-ai-front-end-six.vercel.app/" target="_blank" style="display: inline-block; background-color: #3182ce; color: #ffffff; text-decoration: none; font-weight: bold; padding: 6px 12px; border-radius: 4px; font-size: 12px;">Try HireMe AI Assistant Live &rarr;</a>
  </div>

  <p style="margin: 0 0 12px 0;">Please find my resume attached for your review. I would welcome the opportunity to discuss how my technical background can add value to your team.</p>
  <p style="margin: 0 0 16px 0;">Thank you for your time and consideration.</p>
  
  <!-- Signature -->
  <div style="border-top: 1px solid #e0e0e0; padding-top: 12px; margin-top: 16px;">
    <div style="font-size: 15px; font-weight: bold; color: #1a202c;">Arpit Kumar</div>
    <div style="font-size: 13px; color: #555555; margin-bottom: 4px;">Backend & AI Engineer</div>
    <div style="font-size: 13px; color: #555555; margin-bottom: 4px;">📞 Phone: <strong>+91 80095 69030</strong></div>
    <div style="font-size: 13px; color: #555555;">
      🔗 <a href="https://www.linkedin.com/in/apt1075" style="color: #3182ce; text-decoration: none; font-weight: bold;">LinkedIn</a> &nbsp;|&nbsp; 
      💻 <a href="https://github.com/Apt1075" style="color: #3182ce; text-decoration: none; font-weight: bold;">GitHub</a>
    </div>
  </div>
</div>
""".replace('\n', '').replace('\r', '')  # Strips all Python newlines so yagmail doesn't add <br> tags

attachments = [
    "D:/python/automation mail/arpit-cloud-2.pdf"
]

try:
    yag = yagmail.SMTP(user=sender_email, password=app_password)

    for email in recipients:
        print(f"Sending formatted email to {email}...")
        yag.send(
            to=email,
            subject=subject,
            contents=html_email_body,
            attachments=attachments
        )
        print(f"✅ Email sent cleanly to {email}")

except Exception as e:
    print("❌ Error sending email:", e)