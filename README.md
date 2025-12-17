Scenario: Order Status Notification (Small & Realistic)

Problem

You have an Order

When order status changes (PLACED → SHIPPED → DELIVERED)

Multiple systems must react:

Email service

SMS service

Analytics / Logger

You don’t want Order to know how notifications are sent

This is exactly Observer Pattern.