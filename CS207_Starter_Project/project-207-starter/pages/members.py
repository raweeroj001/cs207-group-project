import json
from pathlib import Path
import streamlit as st

# กำหนด Path ไฟล์ data/members.json
path = Path(__file__).resolve().parent.parent
object_path = path / "data" / "members.json"


def load_json_data(file_path):
    if not file_path.exists():
        return None
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        st.error(f"Error loading JSON: {e}")
        return None


# โหลดข้อมูลสมาชิก
data = load_json_data(object_path)

if data is None:
    st.error("❌ File not found: `data/members.json` or contains no data.")
else:
    st.subheader("ℹ️ Group 1 Team Members")
    st.markdown("---")

    for member in data.get("members", []):
        name = member.get("name", "N/A").strip()
        student_id = member.get("student_id", "N/A")
        role = member.get("role", "N/A")
        image_url = member.get("image", None)

        # แบ่งคอลัมน์รูปภาพและข้อมูลสัดส่วน 1:3
        col1, col2 = st.columns([1, 3])

        with col1:
            if image_url and image_url != "N/A":
                # แสดงผลรูปภาพด้วย st.image
                st.image(image_url, width=120)
            else:
                st.info("No Image")

        with col2:
            st.markdown(f"### {name}")
            st.write(f"🆔 **Student ID:** {student_id}")
            st.write(f"📄 **Role:** `{role}`")

        st.markdown("---")