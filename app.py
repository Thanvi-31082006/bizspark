import streamlit as st

st.title("BizSpark 🚀")
st.write("AI-powered Startup Idea Generator")

# User input
interests = st.text_input("Enter your interests:")
skills = st.text_input("Enter your skills:")

if st.button("Generate Startup Idea"):
    if interests and skills:
        st.success(f"Here’s a startup idea for someone interested in {interests} with skills in {skills}:")
        st.info("👉 Example: EduMentor AI – Personalized learning app connecting students with AI tutors.")
    else:
        st.warning("Please enter both interests and skills.")
