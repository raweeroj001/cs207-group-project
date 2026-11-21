import sys
from pathlib import Path
import pandas as pd
import streamlit as st

parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

from services.textPrediction import (
    build_markov_model,
    generate_sentence,
    load_corpus_from_json,
    predict_next_words,
)

st.subheader("🔮 Text Prediction (Markov Chain)")
st.write(
    "Predict next words and generate sentences using corpus from `data/raw_data.json`."
)

# 1. Load data from JSON
json_path = parent_dir / "data" / "raw_data.json"
corpus_text = load_corpus_from_json(str(json_path))

if not corpus_text:
    st.error(
        "File not found: `data/raw_data.json` not found or contains no data."
    )
    st.stop()

model = build_markov_model(corpus_text)
unique_words = sorted(list(model.keys()))

st.markdown("---")

col1, col2 = st.columns(2)

# --- Feature 1: Predict Next Word ---
with col1:
    with st.container(border=True):
        st.subheader("🎯 Next Word Prediction")

        # index=None เพื่อไม่ให้มีคำถูกเลือกโดยอัตโนมัติ
        selected_word = st.selectbox(
            "Select Current Word:",
            options=unique_words,
            index=None,
            placeholder="Choose a word...",
        )

        if selected_word:
            predictions = predict_next_words(model, selected_word)

            if predictions:
                st.write(
                    f"Probability of next words after **'{selected_word}'**:"
                )
                df_pred = pd.DataFrame(
                    list(predictions.items()),
                    columns=["Next Word", "Probability"],
                )

                # Format probability as percentage
                df_display = df_pred.copy()
                df_display["Probability"] = df_display["Probability"].map(
                    lambda x: f"{x * 100:.1f}%"
                )

                st.dataframe(df_display, use_container_width=True)
                st.bar_chart(df_pred, x="Next Word", y="Probability")
            else:
                st.info(f"No following words found for '{selected_word}'.")
        else:
            st.info("💡 Please select a word above to see predictions.")

# --- Feature 2: Generate Sentences ---
with col2:
    with st.container(border=True):
        st.subheader("🎲 Sentence Generator")

        # index=None เพื่อไม่ให้มีคำถูกเลือกโดยอัตโนมัติ
        start_word = st.selectbox(
            "Start Word:",
            options=unique_words,
            index=None,
            placeholder="Choose a start word...",
            key="gen_start",
        )
        word_count = st.slider("Sentence Length (words):", 3, 10, 5)
        num_sentences = st.slider("Number of Sentences:", 1, 5, 3)

        if st.button("🚀 Generate Sentences", use_container_width=True):
            if start_word:
                st.markdown("**Generated Results:**")
                for i in range(1, num_sentences + 1):
                    generated = generate_sentence(model, start_word, word_count)
                    st.success(f"**Option {i}:** {generated}")
            else:
                st.warning("⚠️ Please select a start word first.")
        else:
            if not start_word:
                st.info("💡 Please select a start word and click Generate.")