import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker" , page_icon="🔒")
st.title("🔐 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate Password Strength Checker! 👋
Use this simple tool to check the strength of your password and get suggestions to make it stronger.
We will give you helpful tips to create a **strong password** 🔒""")

password = st.text_input("Enter your password: 🔑", type="password")

feedback = []

score = 0

if password: 
    if len(password) >= 8:
        score += 1
    else:    
        feedback.append("📏 Password should be at least 8 characters long.")
 
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("🔠 Password should contain both uppercase and lowercase letters.")
        
    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("🔢 Password should contain at least one digit.")
        
    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("🔣 Password should contain at least one special character (!@#$%&*).")
    
    if score == 4:
        feedback.append("💪 Your password is strong!")
    elif score == 3:
        feedback.append("🏋️ Your password is moderately strong! It could be stronger.")
    else:
        feedback.append("😰 Your password is weak! Please make it stronger.")

    if feedback:
        st.markdown("## 🚀 Improvement suggestions")
        for message in feedback:
            st.write(message)
else:
    st.info("🔍 Please enter a password to check its strength.")