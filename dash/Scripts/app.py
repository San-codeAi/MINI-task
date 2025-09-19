import streamlit as st
import requests
from textblob import TextBlob
import pandas as pd

# This is the function that will perform the sentiment analysis
def analyze_sentiment(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the overall sentiment
    overall_polarity = blob.sentiment.polarity
    overall_subjectivity = blob.sentiment.subjectivity
    
    # Analyze sentiment for each sentence and store it in a DataFrame
    data = []
    for i, sentence in enumerate(blob.sentences):
        sentiment = sentence.sentiment
        row = {
            'Sentence': str(sentence),
            'Polarity': sentiment.polarity,
            'Subjectivity': sentiment.subjectivity
        }
        data.append(row)
    
    # Create the DataFrame
    df = pd.DataFrame(data)
    return overall_polarity, overall_subjectivity, df

# --- Streamlit Web App Interface ---

# Set the title of the app
st.title("Sentiment Analyzer")

# Create a text input box for the user to enter text
user_input = st.text_area("Enter text to analyze sentiment:", "Type or paste some text here...")

# Create a button to trigger the analysis
if st.button("Analyze"):
    # Check if the user has entered some text
    if user_input:
        # Call our function to get the results
        polarity, subjectivity, df = analyze_sentiment(user_input)

        # Display the overall results
        st.subheader("Overall Sentiment")
        st.write(f"*Polarity:* {polarity:.2f} (from -1.0 to 1.0)")
        st.write(f"*Subjectivity:* {subjectivity:.2f} (from 0.0 to 1.0)")
        
        # Display the sentence-by-sentence results in a table
        st.subheader("Sentence-by-Sentence Analysis")
        st.dataframe(df)

    else:
        st.error("Please enter some text to analyze.")