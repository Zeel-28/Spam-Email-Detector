# Spam-Email-Detector
The Spam Email Detector is a simple machine learning project that classifies text messages or emails as Spam or Not Spam (Ham). It demonstrates the end-to-end workflow of a real-world AI system — from training a model to deploying it through a web interface.

---

## 🧩 Overview

The **Spam Email Detector** uses Natural Language Processing (NLP) and Machine Learning to analyze text and classify it as spam or safe.  
It consists of:
- A **Python backend** using Flask for real-time predictions.
- A **Machine Learning model** trained using the Naive Bayes algorithm.
- A **frontend** made with pure HTML and CSS for user interaction.

---

## ⚙️ Features

✅ Classifies email text as **Spam** or **Not Spam**  
✅ End-to-end ML workflow (train → save → serve → predict)  
✅ Lightweight **Flask REST API** backend  
✅ Simple, clean **HTML/CSS frontend** (no frameworks)  
✅ Works locally on Windows, Mac, or Linux

---

## 🧠 How It Works

1. **Text Preprocessing & Vectorization**
   The text is transformed into numerical data using **TF-IDF Vectorization**, which measures how important each word is within the message.

2. **Model Training**
   A **Multinomial Naive Bayes** classifier is trained on a labeled dataset of thousands of messages (spam vs. ham).

3. **Prediction API**  
   The trained model is saved as `model.pkl` and served through a Flask API endpoint `/predict`.

4. **Frontend Integration**  
   Users can paste an email message into the web interface and click **“Check”**.  
   The app sends the text to the backend and displays:
   - 🚨 “This looks like SPAM!”  
   - ✅ “This email seems safe.”

---

## 🧰 Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3 |
| ML Library | scikit-learn |
| Backend | Flask + Flask-CORS |
| Frontend | HTML5, CSS3, JavaScript |
| ML Algorithm | TF-IDF Vectorizer + Naive Bayes |

---

