import sys
from pathlib import Path
import streamlit as st

# Setup Path สำหรับเรียกใช้บริการในโฟลเดอร์ services
parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

st.subheader("🎲 Bayes' Theorem Calculator")
st.write(
    "คำนวณความน่าจะเป็นแบบมีเงื่อนไข: $P(A|B) = \\frac{P(B|A) \\cdot P(A)}{P(B)}$"
)

st.markdown("---")

# 1. รับค่าความน่าจะเป็นพื้นฐานจากผู้ใช้ (กำหนด value=None เพื่อไม่ให้มีค่า Default)
col1, col2 = st.columns(2)

with col1:
    prior = st.number_input(
        "P(A) - Prior Probability (ความน่าจะเป็นเริ่มต้น):",
        min_value=0.0,
        max_value=1.0,
        value=None,  # ไม่มี Default
        placeholder="กรอกค่าระหว่าง 0.0 - 1.0 (เช่น 0.01)",
        step=0.01,
        help="เช่น โอกาสที่ John โกหกว่าป่วย = 1%",
    )

    likelihood = st.number_input(
        "P(B|A) - Likelihood (ความน่าจะเป็นที่จะเกิด B เมื่อ A เกิด):",
        min_value=0.0,
        max_value=1.0,
        value=None,  # ไม่มี Default
        placeholder="กรอกค่าระหว่าง 0.0 - 1.0 (เช่น 0.95)",
        step=0.01,
        help="เช่น คนที่โกหกส่วนใหญ่จะพูดตระกุกตระกัก = 95%",
    )

with col2:
    false_alarm = st.number_input(
        "P(B|not A) - False Positive Rate (โอกาสเกิด B ทั้งที่ไม่ได้เป็น A):",
        min_value=0.0,
        max_value=1.0,
        value=None,  # ไม่มี Default
        placeholder="กรอกค่าระหว่าง 0.0 - 1.0 (เช่น 0.05)",
        step=0.01,
        help="เช่น คนที่ไม่ได้โกหกก็อาจพูดตระกุกตระกักได้ = 5%",
    )

st.markdown("---")

# 2. เพิ่มปุ่มคำนวณ และตรวจสอบว่าผู้ใช้กรอกข้อมูลครบถ้วนหรือยัง
calculate_btn = st.button("Calculate Bayes' Theorem", use_container_width=True)

if calculate_btn:
    # ตรวจสอบว่ากรอกข้อมูลครบทั้ง 3 ช่องหรือไม่
    if prior is not None and likelihood is not None and false_alarm is not None:
        # TODO 2A: Calculate P(B) using prior, likelihood and false_alarm.
        # P(B) = P(B|A)P(A) + P(B|not A)P(not A)
        p_b = (likelihood * prior) + (false_alarm * (1 - prior))

        if p_b is None:
            st.warning("TODO 2A: Complete the calculation of P(B).")
        elif p_b > 0:
            # TODO 2B: Calculate P(A|B) using Bayes' theorem.
            posterior = (likelihood * prior) / p_b

            if posterior is None:
                st.warning("TODO 2B: Complete the posterior calculation.")
            else:
                st.subheader("📈 Posterior Probability")
                st.metric(
                    label="P(A|B) - ความน่าจะเป็นจริงเมื่อมีหลักฐาน B เกิดขึ้น:",
                    value=f"{posterior * 100:.2f}%",
                )

                st.info(
                    f"**Interpretation:** เมื่อพบหลักฐาน B เกิดขึ้น โอกาสจริงที่เหตุการณ์ A จะเกิดขึ้นคือ **{posterior * 100:.2f}%**"
                )
        else:
            st.error("❌ ไม่สามารถคำนวณได้เนื่องจาก P(B) มีค่าเป็น 0")
    else:
        st.warning("⚠️️ please fill in all three probability values (P(A), P(B|A), P(B|not A)) to perform the calculation.")
else:
    st.info("💡 กรอกข้อมูลความน่าจะเป็นด้านบน แล้วกดปุ่ม **Calculate Bayes' Theorem** เพื่อดูผลลัพธ์")