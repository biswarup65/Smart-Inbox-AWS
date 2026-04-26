# ☁️ Serverless Smart Inbox with Real-Time Sentiment Analysis


## 📌 Project Overview

XYZ Company, a fast-growing e-commerce company, receives hundreds of customer messages daily. Manually reviewing and prioritizing these messages leads to delayed responses and poor customer experience.

To solve this, I built a **Serverless Smart Inbox System** using AWS that automatically:

* Analyzes customer message sentiment (Positive, Negative, Neutral)
* Routes messages to priority queues
* Displays results in a real-time dashboard

---

## 🚀 Project Architecture

This project follows an **event-driven, serverless architecture**:

![Project Banner]()

---

## 🛠️ AWS Services Used

* **Amazon S3** – Stores incoming message files
* **AWS Lambda** – Processes messages automatically
* **Amazon Comprehend** – Performs sentiment analysis
* **Amazon SQS** – Routes messages based on priority
* **Amazon API Gateway** – Exposes backend API
* **Amazon CloudFront** – Hosts frontend dashboard
* **Amazon CloudWatch** – Logs & monitoring
* **AWS IAM** – Secure access control

---

## ⚙️ Workflow

1. User uploads a `.txt` file to S3 (`/incoming/`)
2. S3 event triggers Lambda function
3. Lambda reads file and calls Amazon Comprehend
4. Sentiment is detected (Positive, Negative, Neutral)
5. Messages are routed:

   * 🔴 Negative → High Priority Queue
   * 🟢 Positive/Neutral → Normal Queue
6. API Gateway + Lambda fetch messages
7. Dashboard displays results in real time via CloudFront

---

## 💻 Features

* ✅ Fully serverless architecture
* ✅ Real-time sentiment classification
* ✅ Intelligent message routing
* ✅ Live dashboard with auto-refresh
* ✅ Sentiment confidence scores
* ✅ Timestamp tracking
* ✅ Secure access using IAM

---


## 💻 Frontend Dashboard

![Frontend Dashboard UI]()
---

## 🧪 How to Test

1. Upload a `.txt` file into:

   ```
   /incoming/
   ```

2. Example:

   ```
   The delivery was delayed and I am unhappy with the service
   ```

3. Expected:

   * Sentiment → NEGATIVE
   * Routed → HighPriorityQueue
   * Visible on dashboard

---

## 🔥 Key Learnings

* Built event-driven architecture using AWS
* Integrated AI service (Amazon Comprehend)
* Designed scalable and serverless workflows
* Implemented real-time dashboard using CloudFront
* Applied IAM security best practices

---


## 🔚 Conclusion

This project demonstrates how a fully serverless, event-driven architecture on AWS can be used to solve real-world business problems efficiently. By integrating services like S3, Lambda, Comprehend, and SQS, the system automates message classification and prioritization in real time. The addition of a CloudFront-hosted dashboard provides clear visibility into operations, making the solution both practical and scalable for modern customer support workflows.

