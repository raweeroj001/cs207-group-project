import sys
from pathlib import Path
import streamlit as st
from services.stats import calculate_statistics

parent_dir = Path(__file__).resolve().parent.parent
if str(parent_dir) not in sys.path:
    sys.path.append(str(parent_dir))

st.subheader("📊 Statistics Calculation")
st.write("Calculate statistics using the `services/stats.py` service.")

input_str = st.text_input(
    "Enter numbers (separated by commas ,):",
    placeholder="e.g., 10, 20, 20, 30, 40",  
)

st.markdown("---")

if input_str.strip():
    try:
        data = [
            float(x.strip()) for x in input_str.split(",") if x.strip() != ""
        ]

        if not data:
            st.warning("กรุณากรอกตัวเลขอย่างน้อย 1 ตัว")
            st.stop()

        results = calculate_statistics(data)

        st.subheader("📈 ผลการคำนวณ")

        col1, col2, col3, col4 = st.columns(4)
        col1.metric(
            "ค่าเฉลี่ย (Mean)",
            (
                f"{results['mean']:.2f}"
                if results["mean"] is not None
                else "N/A"
            ),
        )
        col2.metric(
            "ค่ามัธยฐาน (Median)",
            (
                f"{results['median']:.2f}"
                if results["median"] is not None
                else "N/A"
            ),
        )
        col3.metric(
            "ส่วนเบี่ยงเบนมาตรฐาน (SD)",
            (
                f"{results['std']:.2f}"
                if results["std"] is not None
                else "N/A"
            ),
        )
        col4.metric(
            "ความแปรปรวน (Variance)",
            (
                f"{results['variance']:.2f}"
                if results["variance"] is not None
                else "N/A"
            ),
        )

        mode_val = results["mode"]
        if mode_val == 0:
            mode_display = "ไม่มีฐานนิยม (Mode)"
        elif isinstance(mode_val, list):
            mode_display = f"Multi Mode: {mode_val}"
        else:
            mode_display = f"Single Mode: {mode_val}"

        st.warning(f"**ฐานนิยม (Mode):** {mode_display}")


    except ValueError:
        st.error("Invalid Inputs: please specify only numbers and commas. Example: 10, 20, 20, 30, 40")
else:
    st.info("💡 Please enter numbers above to start calculation")