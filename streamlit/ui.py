
import streamlit as st
import requests

def main():
    # FLASK_API_URL = "http://flask:5000/predict"  # flask is used when running in Docker
    FLASK_API_URL = "http://localhost:5000/predict"  # localhost is used when running locally

    st.title("News Category Classifier")
    
    # Create a text area for article input
    article_text = st.text_area("Enter news article text:", height=200)
    
    if st.button("Predict Category"):
        if article_text:
            # Make API request to the Flask endpoint
            response = requests.post(
                FLASK_API_URL,
                json={"article": article_text}
            )
            
            if response.status_code == 200:
                prediction = response.json()["category"]
                st.success(f"Predicted Category: {prediction}")
                
                # Add some visual elements to display the result
                st.markdown("---")
                st.markdown(f"### Article Classification")
                st.markdown(f"**Category:** {prediction}")
            else:
                st.error("Error getting prediction from API")
        else:
            st.warning("Please enter some text to classify")

if __name__ == "__main__":
    main()