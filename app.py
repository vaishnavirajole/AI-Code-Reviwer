import streamlit as st
import google.generativeai as genai  # Google Generative AI API

# Configure the API with your key
API_KEY = "YOUR_API_KEY"  # Replace with your actual API key
genai.configure(api_key=API_KEY)

# Define the system instruction for the AI
instruction_message = (
    "Only review the code if input is provided; otherwise, politely inform the user."
)

# Streamlit User Interface
st.title("AI-Powered Code Review")
st.write("Paste your code below to receive AI feedback on potential bugs or improvements.")

# Text area for code input
user_code = st.text_area("Enter your code here:", height=250)

def review_code(code_text):
    """
    Send the provided code to the Google Generative AI API and return the analysis.
    """
    prompt = (
        f"{instruction_message}\n\n"
        f"Please analyze the following code snippet and suggest any improvements or identify bugs:\n\n"
        f"{code_text}"
    )
    result = genai.generate_text(prompt=prompt, model="models/gemini-2.0-flash-exp")
    return result.result  # Return the AI's response

# When the user clicks the button, process the code
if st.button("Submit Code for Review"):
    if user_code.strip():
        st.info("Reviewing your code, please wait...")
        try:
            feedback = review_code(user_code)
            st.subheader("AI Feedback:")
            st.write(feedback)
        except Exception as error:
            st.error("An error occurred while reviewing your code. Please check your input and try again.")
    else:
        st.warning("Please enter some code before submitting.")
