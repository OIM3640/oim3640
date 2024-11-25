## To import the API:
import os  ### To interact with the system
from dotenv import (
    load_dotenv,
)  ### To read the .env file, in order to keep the API Key hidden
from newsapi import (
    NewsApiClient,
)  ### To interact with newsapi and make requests (1,000 per day)

from collections import Counter, defaultdict
import matplotlib.pyplot as plt
import re
import nltk
from nltk.corpus import (
    stopwords,
)  ### Used the assignment prompt and search on https://www.geeksforgeeks.org/removing-stop-words-nltk-python/#removing-stop-words-with-nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer

from wordcloud import WordCloud

nltk.download("vader_lexicon")

# Download the stopwords list to be removed from the search
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))


load_dotenv()  ### To read .env file
newsapi_KEY = os.getenv(
    "newsapi_KEY"
)  ### newsapi_KEY as a variable is associated with the actual key which can stay hidden

Key = NewsApiClient(
    api_key=newsapi_KEY
)  ### Use the key to authenticate my API requests


### Retrieve the articles using newsAPI


def get_recent_articles(keyword, from_date, to_date, language="en", page_size=15):
    """
    This function searches for recent news articles for some specific keyword within a date range between from_date (start) and to_date (end).

    The following parameters have to be specified when running the main function:

    keyword (Requires a string):  keyword to search for.
    from_date (Requires a string): in 'YYYY-MM-DD' format.
    to_date (Requires a string): in 'YYYY-MM-DD' format.
    language (Requires a string): the default is set to 'en' (English).
    page_size: It is set to 15 by default just for practicality and readability.

    Using these parameters, the function will return a list of dictionaries, each containing the article title, description, and publication date.
    """
    try:
        # Fetch news articles with the specified keyword and date range
        all_articles = Key.get_everything(
            q=keyword,
            from_param=from_date,
            to=to_date,
            language=language,
            page_size=page_size,
        )
        articles = all_articles.get("articles", [])

        # Extract and return relevant information
        results = [
            {
                "title": article["title"],
                "description": article["description"],
                "published_at": article["publishedAt"],
                "source": article["source"]["name"],
            }
            for article in articles
        ]
        return results
    except Exception as e:
        print(f"An error occurred: {e}")
        return []


# Main block to fetch articles and print results. The parameters are specified here
# It prints the article title, source, date, and description
if __name__ == "__main__":
    keyword = "War"
    from_date = "2024-10-25"
    to_date = "2024-10-30"
    recent_news = get_recent_articles(keyword, from_date, to_date)
    for i, article in enumerate(recent_news, 1):
        print(
            f"Article {i}: {article['title']}\nSource: {article['source']}\nPublished on: {article['published_at']}\nDescription: {article['description']}\n"
        )

######################################################################################################
### Processing:


# Combine titles and descriptions to get all words, ignoring stop words
def get_word_frequencies(articles):
    word_count = Counter()
    for article in articles:
        # Combine title and description text, convert to lowercase, and split into words to make the processing on this
        text = (
            article["title"] + " " + (article["description"] or "")
        ).lower()  # I chose to include both title and description when counting the words just to get a higher count of data. The title can be removed
        words = re.findall(r"\b\w+\b", text)  # Extract words only

        # Filter out stop words
        filtered_words = [
            word for word in words if word not in stop_words
        ]  ### Words is the list we defined earlier with all the words form titles and descriptions and stop_words is provided by the library that was imported
        word_count.update(
            filtered_words
        )  ## After research and asking chatgpt, Instead of a += word count, I used the counter from the collections module
    return word_count


# Get word frequencies and find the top 3 words (ignoring stop words)
word_count = get_word_frequencies(recent_news)
top_words = word_count.most_common(3)
print("Top 3 most frequent words:", top_words)


### Asked chat gpt to help solve this part. When i tested the script, some words were in the top 3 most frequent but didn't appear in the graph.
### It seemed that this was because they only appeared in certain dates, meaning not continuous line could be drawn.
### So the solution was identifying all dates and inputting "0" when the word didn't appear


# Initialize a dictionary to store counts for each top word by date
top_words_dates = {word: defaultdict(int) for word, _ in top_words}
# Get all dates in the range
all_dates = sorted({article["published_at"][:10] for article in recent_news})
# Ensure each top word has an entry for every date
for word in top_words_dates:
    for date in all_dates:
        if date not in top_words_dates[word]:
            top_words_dates[word][date] = 0  # Fill missing dates with 0 frequency

# Populate top_words_dates with occurrences by date
for article in recent_news:
    text = (article["title"] + " " + (article["description"] or "")).lower()
    date = article["published_at"][
        :10
    ]  # Needed to Extract 10 characters for the date format YYYY-MM-DD

    for word, _ in top_words:
        if word in text:
            top_words_dates[word][date] += 1

# Plot each of the top 3 words' frequencies over time ---- https://matplotlib.org/stable/tutorials/pyplot.html#plotting-with-categorical-variables
# I used the library documentation for plotting categorical variables and asked chat gpt to help solve my mistakes
for word, date_counts in top_words_dates.items():
    dates, counts = zip(*sorted(date_counts.items()))
    plt.plot(dates, counts, label=word)

plt.xlabel("Date")
plt.ylabel("Frequency")
plt.title("Frequency of Top 3 Words Over Time (Excluding Stop Words)")
plt.legend()
plt.xticks(rotation=45)
plt.show()


#########################################################################################################

### More advanced processing
## Used ChatGPT for ideas and tips on getting started

# 1 - Sentiment Analysis

# Load OpenAI API key
import openai
import os

# Load OpenAI API key
import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def get_openai_response(system_prompt, user_prompt):
    client = OpenAI(api_key=OPENAI_API_KEY)
    completion = client.chat.completions.create(
        model="gpt-4",  # Use the appropriate model, e.g., gpt-4 or gpt-3.5-turbo
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )
    return completion.choices[0].message.content.strip()

def analyze_sentiment_openai(articles):
    sentiments = []
    for article in articles:
        # Combine title and description for sentiment analysis
        text = article["title"] + " " + (article["description"] or "")
        
        # Define prompts
        system_prompt = "You are a helpful assistant that evaluates the sentiment of text."
        user_prompt = f"Please provide only a sentiment score as a number between -1 and 1, where -1 is very negative, 0 is neutral, and 1 is very positive:\n\n{text}\n\nSentiment score only:"
        
        # Get sentiment score
        response = get_openai_response(system_prompt, user_prompt)
        
        # Attempt to parse response as a float
        try:
            sentiment_score = float(response)
        except ValueError:
            # In case of non-numeric response, handle or log as 0 (neutral) or skip
            print(f"Non-numeric response for text '{text}': '{response}'")
            sentiment_score = 0.0
        
        sentiments.append(sentiment_score)
    
    return sentiments

# Example usage
# Assuming `recent_news` contains your articles
sentiment_scores = analyze_sentiment_openai(recent_news)

# Calculate average sentiment score
average_sentiment = sum(sentiment_scores) / len(sentiment_scores)
print("Average sentiment score:", average_sentiment)



# 2 - Creating a word Cloud

# Combine all filtered words into a single string
text_data = " ".join(
    [
        word
        for article in recent_news
        for word in re.findall(
            r"\b\w+\b",
            (article["title"] + " " + (article["description"] or "")).lower(),
        )
        if word not in stop_words
    ]
)
# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(
    text_data
)
# Display the word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
