# 🧠 IntelliScholar.AI

IntelliScholar is an AI-powered research assistant designed to automate and enhance the academic research workflow. From literature review to paper generation, example code creation, and even pronunciation evaluation for presentations — IntelliScholar streamlines it all.

---

## 🚀 Features

- 📄 **Research Paper Generation**  
  Input your topic and let IntelliScholar search relevant papers and summarize them using multiple AI agents.

- 💻 **Code Snippet Creation**  
  Automatically generate example code based on your paper's content using LLMs.

- 🧾 **PDF Export**  
  One-click export to well-formatted, professional-looking PDF files.

- 🎙️ **Pronunciation Feedback** *(coming soon)*  
  Record your voice, get feedback on pronunciation, and evaluate academic presentation skills using speech analysis.

- 🎥 **Presentation Video Generator** *(in development)*  
  Turn your research into a narrated, auto-generated presentation video.

---

## 🧩 Architecture

```bash
📦 intellischolar
├── app.py                    # Streamlit app entry
├── requirements.txt
├── .gitignore
├── paper_output.pdf
├── utils/
│   ├── summarizer.py         # GPT-based summarization agent
│   ├── code_gen.py           # LLM code generation
│   ├── pdf_gen.py            # Report formatting/export
│   ├── image_gen.py          # Diagram/image generation
│   └── speech_eval.py        # Speech-to-text & evaluation
└── assets/                   # Image and audio resources
````

---

## 🔧 Installation

```bash
git clone https://github.com/Shosei-Abe/intellischolar.git
cd intellischolar
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
streamlit run app.py
```

---

## 📌 Use Case Example

> “I input the topic *'Blockchain for Food Supply Chain Transparency'*, and IntelliScholar generated:
>
> * A structured paper with summary
> * Matching Python code using smart contracts
> * A PDF-ready academic document.”

---

## 👨‍💻 Developer

* **Shosei Abe**
  [LinkedIn](https://www.linkedin.com/in/yourprofile) | [Portfolio](https://your-website.com)

---

## 🌱 Future Work

* AI-based citation manager
* GPT critique/revision loop for improving generated papers
* Presentation evaluation and improvement via audio analysis
* Full app deployment with user authentication

---

## 📄 License

MIT License

````

---
