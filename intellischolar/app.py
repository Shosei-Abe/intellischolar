import streamlit as st
from utils.summarizer import summarize_topic
from utils.pdf_gen import generate_pdf
from utils.code_gen import generate_code
from utils.speech_eval import evaluate_pronunciation
from utils.image_gen import generate_image

st.set_page_config(page_title="IntelliScholar.AI", layout="wide")
st.title("📚 IntelliScholar.AI – Your AI Research Companion")

# Step 1: Topic Input
topic = st.text_input("🔍 Enter your research topic:", placeholder="e.g., Neural Networks in Healthcare")

if topic:
    st.subheader("🧠 AI Summary")
    summary = summarize_topic(topic)
    st.write(summary)

    st.subheader("📄 Download Paper")
    if st.button("Generate Paper PDF"):
        generate_pdf(topic, summary)
        st.success("✅ Paper saved as paper_output.pdf")
        with open("paper_output.pdf", "rb") as pdf_file:
            st.download_button(label="📥 Download PDF",
                       data=pdf_file,
                       file_name="intellischolar_paper.pdf",
                       mime="application/pdf")


    st.subheader("💻 Generated Code")
    code = generate_code(topic)
    st.code(code, language="python")
    if st.button("Run Code (Preview)"):
        exec(code)

    st.subheader("🖼️ Image Generation")
    image_url = generate_image(topic)
    st.image(image_url, caption="Generated Image", use_column_width=True)

    st.subheader("🎤 Pronunciation Evaluation")
    uploaded_file = st.file_uploader("Upload your voice (.wav)", type=["wav"])
    if uploaded_file:
        score, feedback = evaluate_pronunciation(uploaded_file)
        st.subheader(f"Pronunciation Score")
        st.write(f"{score}/10")
        st.text(feedback)


