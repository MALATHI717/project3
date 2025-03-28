
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.mail import send_mail
from django.utils import timezone
from .models import ManifestLetter
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def send_scheduled_emails():
    now = timezone.now()
    due_letters = ManifestLetter.objects.filter(
        scheduled_date__lte=now,
        is_sent=False,
        status="scheduled"  # Assuming you update status to "scheduled" when ready
    )

    for letter in due_letters:
        try:
            # Send email (configure your email settings in settings.py)
            send_mail(
                subject=f"Manifest Letter {letter.id}",
                message=letter.content,
                from_email="malathi.t2002@gmail.com",  # Replace with your email
                recipient_list=[letter.user],  # Assuming user field stores email
                fail_silently=False,
            )
            # Update letter status
            letter.is_sent = True
            letter.status = "sent"
            letter.save()
            logger.info(f"Email sent for letter {letter.id} to {letter.user}")
        except Exception as e:
            letter.status = "failed"
            letter.save()
            logger.error(f"Failed to send email for letter {letter.id}: {str(e)}")

def start_scheduler():
    scheduler = BackgroundScheduler()
    # Run the job every minute to check for due emails
    scheduler.add_job(send_scheduled_emails, "interval", minutes=300)
    scheduler.start()
    logger.info("Scheduler started.")