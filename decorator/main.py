from decorator.EmailNotifier import EmailNotifier
from decorator.SmsNotifier import SmsNotifier
from decorator.WhatsAppNotifier import WhatsAppNotifier

sms_notifier = SmsNotifier(
    EmailNotifier()
    )

whatspp = WhatsAppNotifier(
    SmsNotifier(
        EmailNotifier()
    )
)
whatspp.send()


