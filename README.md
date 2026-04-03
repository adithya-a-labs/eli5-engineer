# 🧠 ELI5 Engineer

> Turn complex engineering concepts into simple, intuitive explanations — instantly.

---

## 🚀 Overview

**ELI5 Engineer** is an AI-powered tool that helps you understand difficult engineering topics in seconds.

Just enter any topic (e.g., *MOSFET*, *Fourier Transform*, *Backpropagation*), and the system generates:

* 🧒 **Explain Like I'm 5 (ELI5)** → Simple analogy-based explanation
* 🎓 **Technical Explanation** → Accurate and structured breakdown
* ⚙️ **Real-World Applications** → Where and how it’s actually used

---

## 💡 Why This Exists

Engineering concepts are often:

* too abstract
* poorly explained
* disconnected from real-world intuition

This tool bridges that gap by combining:

> **Intuition + Theory + Application**

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit** (UI)
* **OpenAI API** (LLM)
* **dotenv** (env management)

---

## ⚙️ How It Works

1. User enters a topic
2. A structured prompt is sent to the LLM
3. The model generates a 3-part explanation:

   * ELI5
   * Technical
   * Applications
4. Results are rendered in a clean UI

---

## 📂 Project Structure

```
eli5-engineer/
│
├── app.py              # Streamlit UI
├── utils.py            # LLM interaction
├── prompts.py          # Prompt templates
├── requirements.txt
├── .env
├── .gitignore
└── README.md
```

---

## 🧪 Example

### Input:

```
MOSFET
```

### Output:

* 🧒 Like a water tap controlling flow
* 🎓 Field-effect transistor controlling current via voltage
* ⚙️ Used in processors, amplifiers, switching circuits

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/eli5-engineer.git
cd eli5-engineer
```

### 2. Create virtual environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Add API Key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

### 5. Run the app

```bash
streamlit run app.py
```

---

## 🌱 Future Improvements

* 🎤 Voice-based explanations
* 📊 Visual diagrams & graphs
* 🧠 Personalized learning paths
* 📚 Save & revisit past topics
* 🔗 Integration with textbooks / notes

---

## 🧠 Vision

This is a step toward building:

> **An AI-powered engineering tutor that thinks like a great teacher**

---

## 🤝 Contributing

Contributions, ideas, and improvements are welcome.
Feel free to fork and build on top of it.

---

## 📜 License

MIT License

---

## ⚡ Built by

**Adithya A**
ECE @ NIT Calicut
Builder | AI + Hardware | Future Systems

---
