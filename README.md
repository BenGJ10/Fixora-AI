# 🚀 FixoraAI - AI-Powered Debugging Assistant  

FixoraAI is an AI-powered debugging assistant that helps you analyze and fix code errors efficiently. Built using **Streamlit** for the frontend and **FastAPI** for the backend, it integrates **Google Gemini 1.5 Pro API** to provide intelligent debugging insights.  

---

## **🔧 Features**
- **📌 Debug Any Programming Language** – Identify and fix syntax errors, logical errors, and optimizations.  
- **⚡ Text-by-Text Generation** – ChatGPT-like typing effect for an engaging UI.  
- **💾 Chat History** – View past debugging sessions.  
- **🎨 Professional UI** – Dark-themed interface with dynamic chat alignment.  
- **🌍 FastAPI Backend** – Efficient handling of debugging requests.  

---

## **🛠️ Tech Stack**
- **Frontend** – [Streamlit](https://streamlit.io/)  
- **Backend** – [FastAPI](https://fastapi.tiangolo.com/)  
- **AI Model** – [Google Gemini 1.5 Pro API](https://ai.google.dev/)  
- **Web Server** – [Uvicorn](https://www.uvicorn.org/)  

---

## **🚀 Installation & Setup**

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/BenGJ10/Fixora-AI.git
cd FixoraAI
```

### **2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables
Create a .env file in the backend/ directory and add your Google Gemini API Key:
```bash
GEMINI_API_KEY=your_google_gemini_api_key
```

### **4️⃣ Run the FastAPI Backend
```bash
uvicorn fastapi_backend:app --reload
```
It should run on http://127.0.0.1:8000

### **5️⃣ Run the Streamlit Frontend
```bash
streamlit run frontend.py
```
The frontend should be accessible at http://localhost:8501

## **🤝 Contributing**
Feel free to contribute! Fork the repo, create a new branch, and submit a pull request.

