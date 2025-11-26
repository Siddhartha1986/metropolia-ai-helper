# 📘 Metropolia Nursing AI Helper

A small demo web application built for the **Metropolia Student AI Assistant recruitment assignment**.
The app combines two tools useful for nursing students:

### 🔹 **1. Nursing Finnish Language Helper**

Search nursing terms in Finnish or English and get
**bilingual explanations + clinical examples**.

### 🔹 **2. Nursing Text Summarizer**

Paste patient notes or study material and get a
**short summary** generated via HuggingFace BART model.

---

## 🌐 Live Demo

👉 **[https://metropolia-ai-helper.onrender.com](https://metropolia-ai-helper.onrender.com)**

*(Free instance — may take 30–60 seconds to wake up if inactive)*

---

# 📸 Screenshots

### 🏠 Home Page

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/120746538/519256178-a15dcbf9-aa4c-4373-a147-497592745b53.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNzMwMDgsIm5iZiI6MTc2NDE3MjcwOCwicGF0aCI6Ii8xMjA3NDY1MzgvNTE5MjU2MTc4LWExNWRjYmY5LWFhNGMtNDM3My1hMTQ3LTQ5NzU5Mjc0NWI1My5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQxNTU4MjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZjdjZGExNjllMzViMjA2M2YyYmRlNDhiZmY4YjFjMWI3ZGE4OTY5YWJlZjk1MzNhMjBjZGYzYjhjOTJmODQ0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.ezEvBmKQefg9s4IwNcnTPAKn0oHVOJvXNGomBXa3jMg" width="700">
</p>

### 🔎 Nursing Finnish Language Helper

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/120746538/519259049-e6bc64f4-db7c-484d-9ab2-78c401033423.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNzMwMDgsIm5iZiI6MTc2NDE3MjcwOCwicGF0aCI6Ii8xMjA3NDY1MzgvNTE5MjU5MDQ5LWU2YmM2NGY0LWRiN2MtNDg0ZC05YWIyLTc4YzQwMTAzMzQyMy5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQxNTU4MjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT02M2M4M2Q3NzNmYzUwZGEyOTE4ZGIzMDYxZTc4YThjNWIzMWNhZGRjNzQ0YTg0YTAyMTUzYTI3MTdjNjc3Y2M3JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.Gjf7qQklpBBsSSvWMisVWueyGODkpwDsasDkTB56mQg" width="700">
</p>

### 📝 Nursing Text Summarizer

<p align="center">
  <img src="https://private-user-images.githubusercontent.com/120746538/519259235-cfa1661b-20a4-4e1c-a034-28e05d41083b.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NjQxNzMwMDgsIm5iZiI6MTc2NDE3MjcwOCwicGF0aCI6Ii8xMjA3NDY1MzgvNTE5MjU5MjM1LWNmYTE2NjFiLTIwYTQtNGUxYy1hMDM0LTI4ZTA1ZDQxMDgzYi5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjUxMTI2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI1MTEyNlQxNTU4MjhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04NmU1OTYzZDI2ZjllYjk1ZjY1ZTVmM2Q2ZjJiZmZjOWEwZmFjM2QyOGZmMWJiM2I1MzA1YWM4YjI1NTAxZmY0JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.InCeK8TB7zCkac1W_o_kAPCqjhgbidRaCsTr8OpHOR8" width="700">
</p>

---

# 🛠 Tech Stack

* **Python 3**
* **Flask**
* **Gunicorn** (production server)
* **HTML/CSS (Jinja2 templates)**
* **HuggingFace Inference API (BART summarization model)**
* **Render.com (deployment)**

---

# 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/Siddhartha1986/metropolia-ai-helper
cd metropolia-ai-helper
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create your `.env` file

In the project root, create a file named `.env`:

```
HF_API_TOKEN=your_huggingface_api_token_here
```

💡 **Note:**
You must use your own HuggingFace token (free account is enough).
The backend automatically loads it using `python-dotenv`.

### 5. Run the Flask app

```bash
python app.py
```

The app will be available at:

```
http://127.0.0.1:5000
```

---

# 📂 Project Structure

```
metropolia-ai-helper/
│
├── templates/           # HTML templates
│   ├── base.html
│   ├── index.html
│   ├── nurse_helper.html
│   └── summarize.html
│
├── app.py               # Main Flask server
├── nursing_terms.py     # Finnish-English term helper logic
├── requirements.txt     # Dependencies
├── .env.example         # Example environment variable file
└── README.md
```

---

# 🔗 Related Projects (Your Internship Projects)

## 📌 Image Classification Pipeline Using Cloud Functions

(Developed at **Metropolia AIoT Garage**)
[https://github.com/Siddhartha1986/Image-Classification-Pipeline-Using-Cloud-Function](https://github.com/Siddhartha1986/Image-Classification-Pipeline-Using-Cloud-Function)

## 📌 LiDAR Project – Depth Measurement (for Wizense LTD)

[https://github.com/Siddhartha1986/LIDAR-Project-Depth-Measurement](https://github.com/Siddhartha1986/LIDAR-Project-Depth-Measurement)

---

# 🧑‍💻 Author

**Siddhartha Lama**
Metropolia UAS — Smart IoT Systems / Nursing Student
Helsinki, Finland

---

# 📄 License

MIT License



