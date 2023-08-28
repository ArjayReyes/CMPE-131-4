from textblob import TextBlob

def sentiment_analysis(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the polarity of the text (ranging from -1 to 1)
    polarity = blob.sentiment.polarity
    
    # Determine sentiment based on polarity
    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"
    
    return sentiment, polarity

# Take input from the user
text_input = input("Enter a text string: ")

# Perform sentiment analysis
result_sentiment, result_polarity = sentiment_analysis(text_input)

# Output the result
print("Sentiment:", result_sentiment)
print("Polarity:", result_polarity)