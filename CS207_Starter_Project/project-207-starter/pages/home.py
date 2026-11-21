import streamlit as st

st.subheader("CS & ST 207: Statistics & Probability for AI", anchor=False)
st.write("Welcome to our Mathelligence project")

st.markdown("---")

col1, col2, col3 = st.columns(3)

# Option 1: Statistics Calculation
with col1:
    with st.container(border=True):
        st.subheader("📊 Statistics", anchor=False)
        st.write("Calculate basic statistical values such as  \n Mean, Median, Mode, SD & Variance")
        if st.button("Go to Statistics Page", key="btn_stats", use_container_width=True):
            st.switch_page("pages/statistics.py")

# Option 2: Bayes Calculation
with col2:
    with st.container(border=True):
        st.subheader("🎲 Bayes' Theorem", anchor=False)
        st.write("Calculate conditional probabilities  \n(Conditional Probability)")
        if st.button("Go to Bayes Page", key="btn_bayes", use_container_width=True):
            st.switch_page("pages/bayes.py")

# Option 3: Text-Prediction
with col3:
    with st.container(border=True):
        st.subheader("🔮 Text Prediction", anchor=False)
        st.write("Simulate text prediction using  \n Markov Chain")
        if st.button("Go to Text Prediction Page", key="btn_text", use_container_width=True):
            st.switch_page("pages/markov.py")


_,col4,_ = st.columns([1,2,1])
with col4:
    with st.container(border=True):
        st.subheader("📄 Custom App", anchor=False)
        st.write("Create your own math/AI-related application feature")
        if st.button("Go to Custom app", key="btn_custom", use_container_width=True):
            st.switch_page("pages/custom.py")