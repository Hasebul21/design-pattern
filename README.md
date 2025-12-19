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


## Decorator Pattern — Questions

### 1️⃣ Notification Features

You have a basic **Email notification system**.
New requirements keep coming:

* Sometimes add **SMS**
* Sometimes add **Push notification**
* Sometimes add **WhatsApp**
* Combinations can vary per user at runtime

**Question:**
How would you design this so that you can add or remove notification features **dynamically** without modifying existing classes?

**Question:**
How would you design the request handling so that these behaviors can be **chained, reordered, or skipped at runtime**?

## Facade Pattern — Questions

### 3️⃣ E-commerce Order Placement

Placing an order requires:

* Checking inventory
* Charging payment
* Creating order record
* Generating invoice
* Sending notification

The controller is becoming too complex.

**Question:**
How would you simplify the controller so it interacts with **one entry point** while hiding all internal service coordination?


**Question:**
How would you design a single, clean interface so the client only calls something like `pay(amount)`?