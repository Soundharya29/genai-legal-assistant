import streamlit as st
import os

from utils.text_extractor import extract_text
from utils.clause_splitter import split_into_clauses, split_into_subclauses
from utils.clause_type_detector import detect_clause_type
from utils.ner_extractor import extract_entities
from utils.contract_classifier import classify_contract
from utils.risk_detector import (
    detect_risks,
    risk_level,
    explain_risk,
    suggest_alternatives,
    contract_risk_score
)
from utils.gpt_explainer import explain_clause
from utils.contract_summary import generate_contract_summary
from utils.pdf_generator import generate_pdf_report
from utils.language_normalizer import normalize_to_english
from utils.audit_logger import log_audit_event


# ---------------- Page Config ----------------
st.set_page_config(page_title="GenAI Legal Assistant", layout="wide")

st.title("📄 GenAI Legal Assistant")
st.subheader("Upload a Contract for Analysis")

DATA_DIR = "data"
os.makedirs(DATA_DIR, exist_ok=True)

# ---------------- File Upload ----------------
uploaded_file = st.file_uploader(
    "Upload contract file",
    type=["pdf", "docx", "txt"]
)

if uploaded_file:
    file_path = os.path.join(DATA_DIR, uploaded_file.name)

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("File uploaded and saved securely ✅")

    # ---------------- Text Extraction ----------------
    raw_text = extract_text(file_path)

    with st.spinner("🔄 Normalizing contract language..."):
        text = normalize_to_english(raw_text)

    # ---------------- Contract Type ----------------
    contract_type = classify_contract(text)
    st.info(f"📄 Contract Type Detected: {contract_type}")

    # ---------------- Clause Extraction ----------------
    clauses = split_into_clauses(text)

    st.subheader("📑 Contract Clauses")
    st.write(f"Total clauses found: {len(clauses)}")

    all_clause_risks = []

    # ---------------- Clause Analysis ----------------
    for idx, clause in enumerate(clauses, start=1):
        clause_type = detect_clause_type(clause)
        entities = extract_entities(clause)
        risks = detect_risks(clause)
        level = risk_level(risks)

        all_clause_risks.append(level)

        with st.expander(f"Clause {idx} — {clause_type} — {level}"):
            st.write(clause)

            # -------- Sub-Clauses --------
            subclauses = split_into_subclauses(clause)
            if len(subclauses) > 1:
                st.markdown("**📌 Sub-Clauses Detected:**")
                for i, sub in enumerate(subclauses, start=1):
                    st.write(f"{i}. {sub}")

            # -------- Entities --------
            st.markdown("**🔍 Extracted Entities**")
            st.write(entities)

            # -------- Risks --------
            st.markdown("**⚠️ Detected Risks**")
            st.write(risks if risks else "No major risks detected")

            # -------- Risk Explanation --------
            if risks:
                st.markdown("**❗ Why this clause is unfavorable**")
                for exp in explain_risk(risks):
                    st.write(f"- {exp}")

                st.markdown("**💡 Suggested Safer Alternatives**")
                for s in suggest_alternatives(risks):
                    st.write(f"- {s}")

            # -------- GPT Explanation --------
            if st.button(f"🧠 Explain Clause {idx}", key=f"explain_{idx}"):
                with st.spinner("Explaining clause using GPT..."):
                    explanation = explain_clause(clause)
                    st.markdown("### 🧠 GPT Explanation")
                    st.write(explanation)

    # ---------------- Overall Contract Risk ----------------
    st.markdown("---")
    st.subheader("📊 Overall Contract Risk Assessment")

    overall_risk = contract_risk_score(all_clause_risks)
    st.success(f"Overall Contract Risk Level: {overall_risk}")

    # ---------------- Plain-English Summary ----------------
    st.markdown("---")
    st.subheader("📝 Plain-English Contract Summary")

    summary = generate_contract_summary(
        contract_type,
        overall_risk,
        clauses,
        all_clause_risks
    )

    st.info(summary)

    # ---------------- PDF Export ----------------
    st.markdown("---")
    st.subheader("📄 Export Legal Risk Report")

    if st.button("⬇️ Download PDF Report"):
        pdf_path = os.path.join(DATA_DIR, "contract_risk_report.pdf")

        generate_pdf_report(
            pdf_path,
            contract_type,
            overall_risk,
            summary,
            clauses,
            all_clause_risks
        )

        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📥 Click to Download",
                data=pdf_file,
                file_name="Contract_Risk_Report.pdf",
                mime="application/pdf"
            )

    # ---------------- Audit Log (STEP 19) ----------------
    log_audit_event(
        uploaded_file.name,
        contract_type,
        overall_risk,
        len(clauses)
    )
