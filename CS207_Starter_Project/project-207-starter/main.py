import streamlit as st

st.set_page_config(page_title="Statistics for AI", page_icon=":material/function:", layout="wide")

pg = st.navigation(
    [
        st.Page("pages/home.py", title="Home", icon="🏠", default=True),
        st.Page("pages/statistics.py", title="Statistics Calculation", icon="📊"),
        st.Page("pages/bayes.py", title="Bayes Calculation", icon="🎲"),
        st.Page("pages/markov.py", title="Text Prediction", icon="🔮"),
        st.Page("pages/display_text.py", title="Raw Text", icon="📄"),
        st.Page("pages/members.py", title="Members", icon="ℹ️"),
        st.Page("pages/custom.py", title="Custom App", icon="🛠️")
    ]
)

pg.run()