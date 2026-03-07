# 🧠 GenAI Legal Assistant for Indian SMEs

## 📌 Problem Statement
Small and Medium Enterprises (SMEs) often struggle to understand complex legal contracts due to legal jargon, hidden risks, and lack of expert guidance. This project builds a **GenAI-powered Legal Assistant** that helps business owners analyze contracts, identify legal risks, and receive clear, actionable explanations in simple business language.

---

## 🎯 Solution Overview
The GenAI Legal Assistant automatically analyzes uploaded contracts and provides:
- Clause-by-clause explanations
- Legal risk identification and scoring
- Unfavorable clause detection
- Suggested safer alternatives
- Plain-English contract summaries
- Downloadable legal risk reports (PDF)

The system supports **English and Hindi contracts**, maintains confidentiality, and creates audit logs for legal traceability.

---

## ⚙️ Key Functional Features

### 🔹 Core Legal NLP Tasks
- Contract Type Classification
- Clause & Sub-Clause Extraction
- Named Entity Recognition (Parties, Dates, Jurisdiction, Amounts)
- Risk & Compliance Detection
- Ambiguity & Unfavorable Clause Detection
- Clause Similarity Matching to Standard Templates

### 🔹 Risk Assessment
- Clause-level Risk Scores (Low / Medium / High)
- Overall Contract Risk Score
- Detection of:
  - Indemnity clauses
  - Penalty clauses
  - Unilateral termination
  - Arbitration & jurisdiction clauses
  - Auto-renewal & lock-in periods
  - Non-compete & IP transfer clauses

### 🔹 User-Facing Outputs
- Simplified contract summary
- Clause-by-clause plain-language explanation
- Suggested renegotiation alternatives
- PDF export for legal review

---

## 🌐 Multilingual Support
- English + Hindi contract parsing
- Hindi → English internal normalization for NLP
- Output summaries in simple business English

---

## 🛠️ Technology Stack
- **Language:** Python
- **LLM:** GPT-4 (used only for legal reasoning & explanations)
- **NLP:** spaCy, Regex-based parsing
- **UI:** Streamlit
- **Storage:** Local files & JSON-based audit logs
- **Deployment:** Streamlit Cloud
- **External Legal APIs:** ❌ Not used (as per constraints)

---

## 📂 Input File Formats
- PDF (text-based)
- DOC / DOCX
- Plain Text (.txt)

---

## 📊 Output Artifacts
- Interactive web-based contract analysis
- Legal risk explanations
- Downloadable PDF legal report
- Audit logs for traceability

---

## 🚀 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Set OpenAI API key (Windows PowerShell):
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

---

## 🔐 Confidentiality & Compliance
- Contracts are processed locally
- No external legal databases or case laws used
- Clause-level LLM calls only (minimal data exposure)
- Audit logs maintained in JSON format

---

## 🎥 Demo Video
https://drive.google.com/file/d/1ToYVUICIessAtj9H2m6F5YjN4wm4ghm6/view?usp=sharing

---

## 🌍 Live Application
https://share.streamlit.io/user/soundharya29

---

## 👨‍💻 Author
**Your Name**  
SOUNDHARYA D 



