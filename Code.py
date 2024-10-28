import os
from openai import OpenAI
import streamlit as st

# Set up the OpenAI client using the API key from environment variables
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

# Wrapper function to get personalized tips based on user responses
def get_water_saving_tips(responses):
    prompt = (
        "Provide water-saving tips tailored to a person located in"+location,
        "They live in a"+housing_type+"type of house",
        "They rate their current water usage awareness as"+awareness_level,
        "Their main interest in saving water is because"+reason
    )
    
    # Generate a response from the API
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are an environmental expert providing water-saving tips."},
                  {"role": "user", "content": prompt}],
        max_tokens=300,
    )
    return completion.choices[0].message.content

# Streamlit app to collect user information
st.title("Personalized Water-Saving Tips")

# Create a form for user input
with st.form(key="user_info_form"):
    location = st.text_input("What city and state are you located in?")
    housing_type = st.text_input("What type of home do you live in?")
    awareness_level = st.radio("How would you rate your awareness of water usage?", ["Low", "Medium", "High"])
    reason = st.text_input("Why are you interested in saving water?")

    # Submit button
    submitted = st.form_submit_button("Get Tips")

    if submitted:
        # Collect responses
        user_responses = {
            "location": location,
            "housing_type": housing_type,
            "awareness_level": awareness_level,
            "reason": reason,
        }
        
        # Get water-saving tips based on responses
        tips = get_water_saving_tips(user_responses)
        
        # Display the tips
        st.subheader("Personalized Water-Saving Tips")
        st.write(tips)
