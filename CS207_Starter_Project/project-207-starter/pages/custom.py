import streamlit as st

st.subheader("🛠️ Custom Application")
st.info("Student task: build your own math/AI-related application here.")

# TODO 4: Add at least one new or extended feature.
# You may extend Statistics, Bayes, or Markov, or choose another topic
# related to Mathematics for AI (e.g., Gradient Descent or Matrix).
# Include: user input, calculation/processing, and output or visualization.
import numpy as np
import pandas as pd

st.title("📐 Linear Algebra: Represent Data Mathematically")
st.write("จำลองการแทนข้อมูลด้วยคณิตศาสตร์ผ่าน **Vector** และ **Matrix** ซึ่งเป็นพื้นฐานสำคัญของ AI และ Machine Learning")

tab1, tab2 = st.tabs(["📊 1. Vector & Cosine Similarity", "🔢 2. Matrix Operations"])

# ==========================================
# TAB 1: VECTOR & COSINE SIMILARITY
# ==========================================
with tab1:
    st.subheader("การแทนข้อมูลด้วย Vector และวัดความคล้ายคลึง (Cosine Similarity)")
    st.caption("ตัวอย่าง: แทนความชอบของผู้ใช้ 2 คนเป็นตัวเลข (เช่น คะแนนหนัง Action, Comedy, Sci-Fi, Horror)")

    col1, col2 = st.columns(2)
    with col1:
        vec_a_str = st.text_input("Vector A (คั่นด้วยลูกน้ำ)", "5, 2, 4, 1")
    with col2:
        vec_b_str = st.text_input("Vector B (คั่นด้วยลูกน้ำ)", "4, 1, 5, 2")

    if st.button("คำนวณค่า Vector", type="primary"):
        try:
            a = np.array([float(x.strip()) for x in vec_a_str.split(",") if x.strip()])
            b = np.array([float(x.strip()) for x in vec_b_str.split(",") if x.strip()])

            if len(a) != len(b) or len(a) == 0:
                st.error("กรุณากรอกจำนวนสมาชิกของ Vector A และ B ให้เท่ากัน")
            else:
                # Processing
                dot_product = float(np.dot(a, b))
                norm_a = float(np.linalg.norm(a))
                norm_b = float(np.linalg.norm(b))
                euclidean_dist = float(np.linalg.norm(a - b))

                if norm_a == 0 or norm_b == 0:
                    cosine_sim = 0.0
                else:
                    cosine_sim = dot_product / (norm_a * norm_b)

                # Output
                st.divider()
                st.subheader("ผลลัพธ์ (Output)")
                m1, m2, m3 = st.columns(3)
                m1.metric("Dot Product (A · B)", f"{dot_product:.2f}")
                m2.metric("Euclidean Distance", f"{euclidean_dist:.4f}")
                m3.metric("Cosine Similarity", f"{cosine_sim:.4f} ({cosine_sim*100:.1f}%)")

                c1, c2 = st.columns(2)
                c1.info(f"**ขนาดของ Vector A (||A||):** {norm_a:.4f}")
                c2.info(f"**ขนาดของ Vector B (||B||):** {norm_b:.4f}")

                # แสดงกราฟเปรียบเทียบข้อมูล
                df_vec = pd.DataFrame({
                    "Vector A": a,
                    "Vector B": b
                }, index=[f"Feature {i+1}" for i in range(len(a))])
                st.bar_chart(df_vec)

        except ValueError:
            st.error("กรุณากรอกเฉพาะตัวเลขคั่นด้วยเครื่องหมายลูกน้ำ (,)")

# ==========================================
# TAB 2: MATRIX OPERATIONS
# ==========================================
with tab2:
    st.subheader("การแทนชุดข้อมูลด้วย Matrix และการคำนวณพื้นฐาน")
    st.caption("กรอกตัวเลขแต่ละแถวขึ้นบรรทัดใหม่ และคั่นแต่ละคอลัมน์ด้วยลูกน้ำ (,)")

    col1, col2 = st.columns(2)
    with col1:
        mat_a_str = st.text_area("Matrix A", "1, 2\n3, 4", height=100)
    with col2:
        mat_b_str = st.text_area("Matrix B", "5, 6\n7, 8", height=100)

    operation = st.selectbox(
        "เลือกการคำนวณ (Operation)",
        ["Matrix Multiplication (A × B)", "Matrix Addition (A + B)", "Transpose (Aᵀ)", "Determinant & Inverse of A"]
    )

    if st.button("คำนวณค่า Matrix", type="primary"):
        try:
            def parse_matrix(text):
                rows = [r.strip() for r in text.strip().split("\n") if r.strip()]
                return np.array([[float(x.strip()) for x in r.split(",")] for r in rows])

            A = parse_matrix(mat_a_str)
            B = parse_matrix(mat_b_str)

            st.divider()
            st.subheader("ผลลัพธ์ (Output)")

            if operation == "Matrix Multiplication (A × B)":
                if A.shape[1] != B.shape[0]:
                    st.error(f"คูณกันไม่ได้: จำนวนคอลัมน์ของ A ({A.shape[1]}) ต้องเท่ากับจำนวนแถวของ B ({B.shape[0]})")
                else:
                    res = np.matmul(A, B)
                    st.write(f"ขนาดผลลัพธ์: {res.shape[0]} × {res.shape[1]}")
                    st.dataframe(pd.DataFrame(res), use_container_width=True)

            elif operation == "Matrix Addition (A + B)":
                if A.shape != B.shape:
                    st.error(f"บวกกันไม่ได้: ขนาดของ A {A.shape} ต้องเท่ากับขนาดของ B {B.shape}")
                else:
                    res = A + B
                    st.dataframe(pd.DataFrame(res), use_container_width=True)

            elif operation == "Transpose (Aᵀ)":
                res = A.T
                st.write(f"ขนาดเดิม: {A.shape} → ขนาดใหม่: {res.shape}")
                st.dataframe(pd.DataFrame(res), use_container_width=True)

            elif operation == "Determinant & Inverse of A":
                if A.shape[0] != A.shape[1]:
                    st.error("Matrix A ต้องเป็นเมทริกซ์จัตุรัส (จำนวนแถวเท่ากับคอลัมน์)")
                else:
                    det = float(np.linalg.det(A))
                    st.metric("Determinant det(A)", f"{det:.4f}")
                    if np.isclose(det, 0):
                        st.warning("ไม่สามารถหา Inverse ได้ เนื่องจาก det(A) = 0 (Singular Matrix)")
                    else:
                        inv = np.linalg.inv(A)
                        st.write("**Inverse Matrix (A⁻¹):**")
                        st.dataframe(pd.DataFrame(inv), use_container_width=True)

        except Exception as e:
            st.error(f"รูปแบบ Matrix ไม่ถูกต้อง: ตรวจสอบจำนวนคอลัมน์ในแต่ละแถวให้เท่ากัน ({e})")