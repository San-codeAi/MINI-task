import requests
from textblob import TextBlob
import pandas as pd

# This is a sample text data we are fetching from a website.
# It's a simple example to show how requests works.
# For a real project, you would fetch data from a social media API.
url = "http://www.gutenberg.org/files/2701/2701-0.txt"

# Use requests to get the content from the URL
try:
    response = requests.get(url)
    # The .text property gives us the content as a string
    text = response.text

    # We only need the first part of the book for this test
    # This line cuts the text down to a manageable size
    first_part = text[1000:5000]

    # Create a TextBlob object from the text
    blob = TextBlob(first_part)

    # Now, let's get the sentiment
    # The .sentiment property returns a named tuple: (polarity, subjectivity)
    # Polarity is a float in the range [-1.0, 1.0] where -1.0 is very negative and 1.0 is very positive.
    # Subjectivity is a float in the range [0.0, 1.0] where 0.0 is very objective and 1.0 is very subjective.
    sentiment = blob.sentiment

    # Let's print the results to the terminal
    print("--- Sentiment Analysis Results ---")
    print(f"Overall Polarity: {sentiment.polarity:.2f}")
    print(f"Overall Subjectivity: {sentiment.subjectivity:.2f}")
except Exception as e:
    print(f"Error fetching or processing data: {e}")
    exit(1)
# ... (keep all the code from before, up to where you get the blob.sentences)

# Create a list to hold our data
data = []

# Now, let's analyze the sentiment for each sentence and store it
print("\n--- Processing Sentences into DataFrame ---")
for i, sentence in enumerate(blob.sentences):
    # Get the sentiment for the current sentence
    sentiment = sentence.sentiment

    # Create a dictionary for this sentence
    row = {
        'sentence_number': i + 1,
        'sentence_text': str(sentence),
        'polarity': sentiment.polarity,
        'subjectivity': sentiment.subjectivity
    }
    
    # Add the dictionary to our data list
    data.append(row)

# Create a pandas DataFrame from our list of dictionaries
df = pd.DataFrame(data)

# Now you can easily display the data in a structured way
print("\n--- DataFrame Results ---")
print(df)

# You can now easily do things like:
# - Find the most positive sentence:
#    most_positive_sentence = df.loc[df['polarity'].idxmax()]
#    print(f"\nMost positive sentence:\n{most_positive_sentence}")

# - Find the most negative sentence:
#    most_negative_sentence = df.loc[df['polarity'].idxmin()]
#    print(f"\nMost negative sentence:\n{most_negative_sentence}")

# - Or even save it to a file
# df.to_csv('sentiment_results.csv', index=False)
# print("\nData saved to sentiment_results.csv")
   