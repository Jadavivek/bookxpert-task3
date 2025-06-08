---
noteId: "f5aa0a40446611f0b07249019a23fbc8"
tags: []

---

# 🍳 BookXpert Recipe Chatbot

A full-stack AI-powered chatbot that generates recipes based on ingredients and servings using Google Gemini LLM via LangChain. Built with FastAPI (backend) and React (frontend).

---

## 🔧 Project Structure

```
bookxpert/
├── backend/               # FastAPI backend
│   ├── app/
│   │   ├── main.py
│   │   └── model_handler.py
├── frontend/              # React frontend
│   ├── public/
│   └── src/
│       ├── App.jsx
│       ├── App.css
│       └── index.js
```

---

## ⚙️ Backend Setup (FastAPI)

### 1. Install Dependencies

```bash
cd backend
pip install fastapi uvicorn langchain langchain-google-genai python-dotenv
```

> Make sure your `GOOGLE_API_KEY` is set in `os.environ` inside `model_handler.py`.

### 2. Run the Backend Server

```bash
uvicorn app.main:app --reload --port 8000
```

The API will be live at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 💡 API Endpoint

- **POST** `/query`

**Request Body:**
```json
{
  "query": "give me a recipe using onion egg tomato for 5 people"
}
```

**Response:**
```json
{
  "response": "Recipe text..."
}
```

---

## 🧑‍🎨 Frontend Setup (React)

### 1. Install Dependencies

```bash
cd frontend
npm install
```

### 2. Start the React App

```bash
npm start
```

The UI will be live at: [http://localhost:3000](http://localhost:3000)

---

## 💬 Features

- 🧠 Integrates Google Gemini LLM via LangChain
- 🍲 Creates recipes from natural language input
- 🔄 Real-time chatbot conversation
- ⚡ FastAPI backend with JSON API
- 🎨 Clean and minimal React UI

---

## 🚀 Future Enhancements

- Add support for more languages
- Save chat history
- Add authentication (optional)
- Deploy to Vercel / Render / EC2

---

## 📜 License

MIT

---

## 👨‍💻 Developed by

**Jada Vivek**

> Reach out for improvements or questions!