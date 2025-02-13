import streamlit as st
import requests
import re

# Meditron-7B server URL
LLAMA_API_URL = "http://localhost:8000/completion"

def remove_duplicate_symptoms(text):
    symptoms = [
        "frequent urination", "increased thirst", "excessive hunger",
        "numbness or tingling", "blurred vision", "fatigue",
        "unexplained weight loss", "frequent infections", "dry skin",
        "slow healing wounds", "tiredness", "slow-healing sores"
    ]
    
    seen = set()
    for symptom in symptoms:
        pattern = re.compile(rf'\b{re.escape(symptom)}\b', re.IGNORECASE)
        if pattern.search(text):
            if symptom.lower() in seen:
                text = pattern.sub("", text) 
            else:
                seen.add(symptom.lower())

    return text

# Function for the cleaning of responses 
def clean_response(response_text):
   
    sentences = response_text.split(". ")
    unique_sentences = list(dict.fromkeys(sentences))  # Remove duplicates
    return ". ".join(unique_sentences[:7])  # Limit to 5 key sentences

# Function to classify the query, call the model, extract and process the response
def query_meditron(user_input):
    disclaimer = "\n\n**Note:** This is general information only. Please consult a healthcare professional for medical advice."
    EMERGENCY_RESPONSE = "⚠️ **Emergency detected!** If you are experiencing a heart attack or a medical emergency, call emergency services immediately (112 or your local emergency number). If someone is with you, ask them for help. Perform CPR if necessary: 30 chest compressions followed by 2 rescue breaths. Stay Calm"

    greetings = ["hi", "hello", "hey", "good morning", "good evening", "what's up", "how are you"]
    emergency_keywords = ["heart attack", "chest pain", "severe pain", "unconscious", "difficulty breathing"]
    appointment_keywords = ["appointment", "schedule", "book a doctor", "see a doctor", "visit a clinic"]
       
    if any(greet in user_input.lower() for greet in greetings):
        return "Hello! How can I assist you with medical information today? 😊"
    
    if any(emergency in user_input.lower() for emergency in emergency_keywords):
        return EMERGENCY_RESPONSE
    
    if user_input.lower() in greetings:
        return "Hello! How can I assist you with medical information today? 😊"
    if any(appointment in user_input.lower() for appointment in appointment_keywords):
        return "Would you like to schedule an appointment? I can guide you through the process."

    try:
        payload = {
            "prompt": f"Answer concisely: {user_input}",
            "n_predict": 150,
            "temperature": 0.2,
            "top_p": 0.85,
            "repeat_penalty": 1.2

        }

        response = requests.post(LLAMA_API_URL, json=payload)
        response_data = response.json()

        #print("🔍 API Response:", response_data)  

        if "content" in response_data:
            model_response = response_data["content"].strip()
        elif "error" in response_data:
            return f"Error from API: {response_data['error']}"
        else:
            return "Error: Unexpected response format."

        model_response = clean_response(model_response)
        model_response = remove_duplicate_symptoms(model_response)
        model_response = re.sub(r"<EOD>.*", "", model_response)
        return model_response + disclaimer

    except Exception as e:
        return f"Error: {str(e)}"


def main():
    st.set_page_config(page_title="AI Healthcare Assistant", page_icon="⚕️", layout="wide")

    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    st.title("⚕️ AI Healthcare Assistant (Powered by Meditron-7B)")

    user_input = st.chat_input("Ask a medical question...")

    if user_input:
        with st.chat_message("user"):
            st.write(user_input)
        st.session_state.chat_history.append(("user", user_input))

        with st.chat_message("assistant"):
            with st.spinner("Processing..."):
                response = query_meditron(user_input)
                st.write(response)
        st.session_state.chat_history.append(("assistant", response))

if __name__ == "__main__":
    main()
