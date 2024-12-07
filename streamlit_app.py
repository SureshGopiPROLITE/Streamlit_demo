# import streamlit as st
# import requests

# # Streamlit UI
# st.title("🧮 Calculator")

# num1 = st.number_input("Enter first number", value=0.0)
# num2 = st.number_input("Enter second number", value=0.0)

# operation = st.radio("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# if st.button("Calculate"):
#     # Prepare the payload
#     payload = {"num1": num1, "num2": num2}
    
#     # Make API requests based on the selected operation
#     if operation == "Add":
#         response = requests.post("http://127.0.0.1:5000/api/add", json=payload)
#     elif operation == "Subtract":
#         response = requests.post("http://127.0.0.1:5000/api/subtract", json=payload)
#     elif operation == "Multiply":
#         response = requests.post("http://127.0.0.1:5000/api/multiply", json=payload)
#     elif operation == "Divide":
#         response = requests.post("http://127.0.0.1:5000/api/divide", json=payload)

#     if response.status_code == 200:
#         result = response.json().get("result")
#         st.success(f"Result: {result}")
#     else:
#         error_message = response.json().get("error", "Unknown error")
#         st.error(f"Error: {error_message}")

# import streamlit as st
# import requests

# # Custom CSS for theming
# custom_css = """
# <style>
#     /* Background and text colors */
#     body {
#         background-color: #2C3E50; /* Dark blue-gray */
#         color: #ECF0F1; /* Light gray */
#     }

#     /* Title styling */
#     h1 {
#         color: #F39C12; /* Orange */
#         text-align: center;
#     }

#     /* Input styling */
#     .stNumberInput > div {
#         background-color: #34495E; /* Slightly lighter background */
#         color: #ECF0F1; /* Light text */
#         border: 2px solid #95A5A6; /* Border color */
#         border-radius: 5px;
#     }

#     /* Button styling */
#     button {
#         background-color: #1ABC9C; /* Turquoise */
#         color: white;
#         border: none;
#         border-radius: 5px;
#         padding: 10px;
#         font-size: 16px;
#         cursor: pointer;
#     }

#     button:hover {
#         background-color: #16A085; /* Darker turquoise on hover */
#     }

#     /* Radio buttons styling */
#     div[role="radiogroup"] > label {
#         color: #F39C12;
#         font-weight: bold;
#     }
# </style>
# """

# # Inject custom CSS into the Streamlit app
# st.markdown(custom_css, unsafe_allow_html=True)

# # Streamlit UI
# st.title("🧮 Calculator")

# # Number inputs
# num1 = st.number_input("Enter first number", value=0.0)
# num2 = st.number_input("Enter second number", value=0.0)

# # Operation selection
# operation = st.radio("Choose operation", ("Add", "Subtract", "Multiply", "Divide"))

# # Button to calculate
# if st.button("Calculate"):
#     # Prepare the payload
#     payload = {"num1": num1, "num2": num2}

#     # Make API requests based on the selected operation
#     if operation == "Add":
#         response = requests.post("http://127.0.0.1:5000/api/add", json=payload)
#     elif operation == "Subtract":
#         response = requests.post("http://127.0.0.1:5000/api/subtract", json=payload)
#     elif operation == "Multiply":
#         response = requests.post("http://127.0.0.1:5000/api/multiply", json=payload)
#     elif operation == "Divide":
#         response = requests.post("http://127.0.0.1:5000/api/divide", json=payload)

#     # Display the result
#     if response.status_code == 200:
#         result = response.json().get("result")
#         st.success(f"Result: {result}")
#     else:
#         error_message = response.json().get("error", "Unknown error")
#         st.error(f"Error: {error_message}")



# import streamlit as st
# import requests

# # Custom CSS for a vibrant theme
# custom_css = """
# <style>
#     /* General app styling */
#     body {
#         background-color: #F4F4F4; /* Light gray */
#         color: #2C3E50; /* Dark gray-blue */
#         font-family: 'Arial', sans-serif;
#     }

#     /* Title styling */
#     h1 {
#         color: #FF5733; /* Bright orange */
#         text-align: center;
#         font-size: 3em;
#         margin-bottom: 10px;
#     }

#     /* Input box styling */
#     .stNumberInput > div {
#         background-color: #FFFFFF; /* White background */
#         border: 2px solid #FF5733; /* Bright orange border */
#         border-radius: 10px; /* Rounded corners */
#         color: #2C3E50;
#         padding: 10px;
#         font-size: 1.2em;
#     }

#     /* Radio buttons styling */
#     div[role="radiogroup"] > label {
#         color: #2C3E50; /* Dark gray-blue */
#         font-weight: bold;
#         font-size: 1.2em;
#         margin-right: 10px;
#         cursor: pointer;
#     }
#     div[role="radiogroup"] > label:hover {
#         color: #FF5733; /* Highlight on hover */
#     }

#     /* Button styling */
#     .stButton > button {
#         background-color: #FF5733; /* Bright orange */
#         color: white;
#         border: none;
#         border-radius: 8px;
#         padding: 12px 20px;
#         font-size: 1.2em;
#         cursor: pointer;
#         transition: 0.3s ease-in-out;
#     }
#     .stButton > button:hover {
#         background-color: #C0392B; /* Darker red-orange on hover */
#     }

#     /* Success box styling */
#     .stAlert {
#         background-color: #D4EDDA; /* Light green for success messages */
#         color: #155724; /* Dark green text */
#         border: 1px solid #C3E6CB; /* Success border */
#         border-radius: 10px;
#         padding: 15px;
#     }

#     /* Error box styling */
#     .stAlert[data-baseweb="alert-error"] {
#         background-color: #F8D7DA; /* Light pink for error messages */
#         color: #721C24; /* Dark red text */
#         border: 1px solid #F5C6CB; /* Error border */
#         border-radius: 10px;
#         padding: 15px;
#     }
# </style>
# """

# # Inject the CSS into the Streamlit app
# st.markdown(custom_css, unsafe_allow_html=True)

# # Streamlit UI
# st.title("🎨 Vibrant Calculator")

# # Number inputs
# num1 = st.number_input("Enter the first number", value=0.0)
# num2 = st.number_input("Enter the second number", value=0.0)

# # Operation selection
# operation = st.radio("Choose an operation:", ("Add", "Subtract", "Multiply", "Divide"))

# # Button to calculate
# if st.button("Calculate"):
#     # Prepare the payload
#     payload = {"num1": num1, "num2": num2}

#     # Make API requests based on the selected operation
#     if operation == "Add":
#         response = requests.post("http://127.0.0.1:5000/api/add", json=payload)
#     elif operation == "Subtract":
#         response = requests.post("http://127.0.0.1:5000/api/subtract", json=payload)
#     elif operation == "Multiply":
#         response = requests.post("http://127.0.0.1:5000/api/multiply", json=payload)
#     elif operation == "Divide":
#         response = requests.post("http://127.0.0.1:5000/api/divide", json=payload)

#     # Display the result
#     if response.status_code == 200:
#         result = response.json().get("result")
#         st.success(f"Result: {result}")
#     else:
#         error_message = response.json().get("error", "Unknown error")
#         st.error(f"Error: {error_message}")



import streamlit as st
import requests

# Define custom CSS for themes and layout
custom_css = """
<style>
    body {
        font-family: 'Arial', sans-serif;
    }

    /* Light theme */
    .light-theme {
        background-color: #F4F4F4; /* Light gray */
        color: #2C3E50; /* Dark gray-blue */
    }

    /* Dark theme */
    .dark-theme {
        background-color: #1E1E1E; /* Dark background */
        color: #FFFFFF; /* White text */
    }

    /* Title styling */
    h1 {
        color: #FF5733; /* Bright orange */
        text-align: center;
        font-size: 2.5em;
    }

    /* Input box styling */
    .stNumberInput > div {
        background-color: #FFFFFF;
        border: 2px solid #FF5733;
        border-radius: 10px;
        padding: 10px;
        font-size: 1.2em;
    }

    /* Button styling */
    .stButton > button {
        border-radius: 10px;
        padding: 10px 15px;
        font-size: 1em;
        font-weight: bold;
    }

    /* History box styling */
    .history-box {
        background-color: #FFFFFF;
        border: 2px solid #FF5733;
        border-radius: 10px;
        padding: 10px;
        margin-top: 20px;
        font-size: 1em;
        overflow-y: auto;
        max-height: 150px;
    }
</style>
"""

# Inject the CSS into the app
st.markdown(custom_css, unsafe_allow_html=True)

# Theme selection
theme = st.radio("Choose a theme:", ["Light", "Dark"], horizontal=True)

# Apply the chosen theme
if theme == "Light":
    st.markdown('<div class="light-theme">', unsafe_allow_html=True)
else:
    st.markdown('<div class="dark-theme">', unsafe_allow_html=True)

# Title
st.title("🔢 Advanced Calculator")

# Two-column layout
col1, col2 = st.columns(2)

# Initialize session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# Column 1: Inputs and operations
with col1:
    st.header("Inputs")
    num1 = st.number_input("Enter the first number", value=0.0, key="num1")
    num2 = st.number_input("Enter the second number", value=0.0, key="num2")

    st.subheader("Choose an operation:")
    operation = st.radio(
        "Operation:",
        ["Add", "Subtract", "Multiply", "Divide"],
        index=0,
        horizontal=True,
    )

    # Clear button to reset inputs
    if st.button("Clear Inputs"):
        st.session_state.num1 = 0.0
        st.session_state.num2 = 0.0

# Column 2: Results and history
with col2:
    st.header("Result")
    if st.button("Calculate"):
        # Prepare payload for API
        payload = {"num1": num1, "num2": num2}

        # Make API requests based on operation
        if operation == "Add":
            response = requests.post("http://127.0.0.1:5000/api/add", json=payload)
        elif operation == "Subtract":
            response = requests.post("http://127.0.0.1:5000/api/subtract", json=payload)
        elif operation == "Multiply":
            response = requests.post("http://127.0.0.1:5000/api/multiply", json=payload)
        elif operation == "Divide":
            response = requests.post("http://127.0.0.1:5000/api/divide", json=payload)

        # Display the result
        if response.status_code == 200:
            result = response.json().get("result")
            st.success(f"The result is: {result}")
            # Add calculation to history
            st.session_state.history.append(
                f"{num1} {operation} {num2} = {result}"
            )
        else:
            error = response.json().get("error", "Unknown error")
            st.error(f"Error: {error}")

    # History of calculations
    st.subheader("History")
    if st.session_state.history:
        st.markdown('<div class="history-box">', unsafe_allow_html=True)
        for item in st.session_state.history:
            st.write(item)
        st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.info("No history available yet.")

# End of theme div
st.markdown("</div>", unsafe_allow_html=True)
