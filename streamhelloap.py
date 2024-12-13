import streamlit as st

# Define a simple authentication function
def check_password():
    """Returns true if user has correct username and password"""
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    
    # Check credentials (here, we use hardcoded values for simplicity)
    if username == "admin" and password == "123":
        return True
    else:
        return False

# Set session state to track authentication
if 'authenticated' not in st.session_state:
    st.session_state['authenticated'] = False

# Show login page or content page based on authentication
if not st.session_state['authenticated']:
    # Only show login page if user is not authenticated
    if check_password():
        st.session_state['authenticated'] = True  # Set authentication to True
        st.experimental_rerun()  # Rerun to refresh the page and show the content page
    else:
        st.warning("Please enter the correct username and password.")
else:
    # Show the content page after successful login
    st.title("Secure Streamlit App")
    st.write("Welcome to the app!")
    st.write("Hello!")
    # You can add more content here as needed
