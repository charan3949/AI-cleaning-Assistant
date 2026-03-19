import os
import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="AI Cleaning Operations Assistant", page_icon="🧹")

st.title("AI Cleaning Operations Assistant")
st.write("Analyze cleaning and facility service issues, assign priority, and generate a professional response.")

api_key = st.text_input("Enter OpenAI API Key", type="password")

issue = st.text_area(
    "Enter issue",
    placeholder="Example: Cleaning was missed on 2nd floor and client complained twice"
)

if st.button("Analyze Issue"):
    if not api_key:
        st.error("Please enter your OpenAI API key.")
    elif not issue.strip():
        st.error("Please enter an issue.")
    else:
        try:
            client = OpenAI(api_key=api_key)

            prompt = f"""
You are an operations assistant for a building services company.

Analyze the issue below and return:
1. Issue Category
2. Priority (Low, Medium, High)
3. Suggested Action
4. Short professional response for manager/team

Issue: {issue}
"""

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You help service operations teams classify and prioritize issues."},
                    {"role": "user", "content": prompt}
                ]
            )

            result = response.choices[0].message.content

            st.subheader("AI Analysis")
            st.write(result)

        except Exception as e:
            st.error(f"Error: {e}")
