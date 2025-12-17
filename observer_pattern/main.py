from observer_pattern.OrderSubject import OrderSubject
from observer_pattern.EmailNotifier import EmailNotifier
from observer_pattern.SmsNotifier import SmsNotifier
from observer_pattern.LoggerNotifier import LoggerNotifier
from observer_pattern.INotificationObserver import INotificationObserver


PLACED = "PLACED"
SHIPPED = "SHIPPED"
DELIVERED = "DELIVERED"

dragon_fruit_order = OrderSubject()
email_notifier = EmailNotifier()
dragon_fruit_order.registerObserver(email_notifier)
sms_notifier : INotificationObserver  = SmsNotifier()
dragon_fruit_order.registerObserver(sms_notifier)
loggerNotifier = LoggerNotifier()
dragon_fruit_order.registerObserver(loggerNotifier)

dragon_fruit_order.setstate(PLACED)

dragon_fruit_order.unregisterObserver(loggerNotifier)
dragon_fruit_order.setstate(SHIPPED)

dragon_fruit_order.unregisterObserver(email_notifier)
dragon_fruit_order.setstate(DELIVERED)
