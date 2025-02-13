# AI Healthcare Assistant (Powered by Meditron-7B)

A medical chatbot application built with **Streamlit** and **Meditron-7B**, designed to provide general medical information while ensuring safety with appropriate disclaimers and emergency detection.

## Features

- **Real-time medical information assistance**
- **Emergency detection & response guidance**
- **Duplicate symptom removal for clarity**
- **Formatted & concise responses**
- **User-friendly chat interface**
- **Medical disclaimers for safety**

---

## Getting Started

### **Prerequisites**

- Python **3.8 or higher**
- At least **8GB RAM**
- **Meditron-7B GGUF model file**

### **Installation**

*Clone the repository:*
git clone https://github.com/HimanshiC/AI_Health_Assitant_chatbot.git

*Install required dependencies:*
pip install -r requirements.txt

Download the Meditron-7B GGUF model file and place it in the project directory.

##**Running the Application**
1. Start the Backend Server
Run the Llama.cpp server:
./llama-server.exe -m ../../../models/meditron-7b.Q4_K_M.gguf --port 8000 --ctx-size 4096 --host 0.0.0.0    
The server will start at http://localhost:8000

2. Start the Chatbot Interface
streamlit run Healthcarebot.py

Then, open your browser and go to http://localhost:8501


###**Emergency Detection Keywords**
The system detects urgent medical conditions, including:
1. Heart attack
2. Chest pain
3. Severe pain
4. Difficulty breathing
5. Unconsciousness

**Medical Disclaimer**
-> This chatbot DOES NOT replace professional medical advice.
-> In case of a medical emergency, call your local emergency number immediately.
-> The system only provides general information based on available data.

###**Key Functions**
*query_meditron(user_input)*
->Processes user queries
->Detects emergency situations
->Responds to medical questions
->Assists with appointment-related queries
*clean_response(response_text)*
Formats model-generated responses
Removes duplicates
Limits response length for clarity
 
 ##**Usage Examples**

# Example: General medical query
"What are the symptoms of diabetes?"
"How to reduce fever?"

# Example: Emergency detection
"I'm experiencing severe chest pain"
"My friend is having a heart attack"

# Example: Appointment scheduling
"I need to book a doctor’s appointment"
"Schedule me a visit to doctor"

##**Limitations**
This is not a diagnostic tool 
It has Keyword-based emergency detection and may not catch all emergencies.
System performance depends on available RAM & processing power.
Limited response length – avoids excessive outputs.
Model specific limitations
