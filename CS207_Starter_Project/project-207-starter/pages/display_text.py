import json
import sys
from pathlib import Path
import pandas as pd
import streamlit as st

parent_dir = Path(__file__).resolve().parent.parent
json_path = parent_dir / "data" / "raw_data.json"

st.subheader("📄 Raw Text Data Corpus")
st.write("display data from: `data/raw_data.json`")

# ฟังก์ชันอ่านไฟล์ JSON
def load_json_data(path):
    if not path.exists():
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading JSON: {e}")
        return None

data = load_json_data(json_path)

if data is None:
    st.error("file not found: `data/raw_data.json` or contains no data.")
else:
    corpus = data.get("corpus", [])

    total_sentences = len(corpus)
    all_words = " ".join(corpus).lower().split()
    total_words = len(all_words)
    unique_words = len(set(all_words))

    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total sentences", total_sentences)
    col2.metric("Total words", total_words)
    col3.metric("Unique vocabulary", unique_words)

    st.markdown("---")

    col_left, col_right = st.columns([2, 1])

    with col_left:
        st.subheader("📋 รายการประโยคทั้งหมด (Sentence List)")
        df_sentences = pd.DataFrame(
            {"No.": range(1, len(corpus) + 1), "Sentence": corpus}
        )
        st.dataframe(df_sentences, use_container_width=True, hide_index=True)
