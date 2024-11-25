# oim3640
This is the process and reflection for assignment 2:

Link to a word doc. with paragraphs and screenshots of the results:
https://babson-my.sharepoint.com/:w:/g/personal/ybensaid1_babson_edu/ESYrkXqKzO5Ei0RlRN64mmkBzP5ARRuRa-IBw4hzVSKnnw?e=fKCxEQ



---------------------------------------------------------------------------------------------------
In this project, I used News API as my primary data source to retrieve recent news articles based on specific keywords. I explored the different sources that were provided, and I knew I wanted something that I would use more often than analyzing a book for example. That was the reasoning behind choosing to analyze recent news articles.  

The goal was to analyze and understand what some common themes and trends in news articles were, depending on a topic that someone is interested in, by processing the text in the title and the description of certain articles. The advantage of News API is that the free tiers give access to a lot of different data sources across many topics, and it gives the option to filter by keywords. To achieve this, I used some techniques such as a word frequency analysis, which allowed me to identify the most frequently occurring words. I took the inspiration from the histogram function we built in class to visualize what words appear the most depending on the theme I chose, and I decided to show it as a word cloud to make it visually appealing. Additionally, I visualized some of the word frequencies over time for the top keywords, to enable me to observe changes in topic focus.   

My project has three main components:   
1. Retrieving data form the news articles including the title and description to analyze, but also the date and source  
2. Text processing to analyze the text, for example extracting titles and descriptions to analyze them, and removing stopwords. 
3. Visualization to make the results easier to see and interpret with a line chart and a word cloud.   

I started by using News API to fetch recent articles based on a specified keyword (I experimented with “War” - “Politics” - “Elections” - “International” - “Trump” ...) and date range. Each article was structured as a dictionary containing information such as the title, description, source, and publication date. This structured data was then stored in lists and dictionaries to make manipulation and analysis easier.  

For text processing, I focused on calculating word frequencies to identify the most common words in article titles and descriptions. I started with the histogram function we built in class, but AI suggested Python’s Counter class from the collections module. I used it to efficiently count words. After running my first scripts, I noticed that “the” and other stop words were always the most frequently used ones, so I added lines to ignore common stop words by filtering them out with nltk's stopword list. I decided to include both titles and descriptions in the word frequency analysis to capture a broader context and to have enough data for my analysis and for visualizations. Then, I came across an issue where some words were only used during some dates but not others. Because of that they would not appear on my line chart. ChatGPT explained that the error came from the way the chart words, if it is only a single occurrence or dates that are not back-to-back, they are “single points” and the line won’t be traced. After asking Ai for help to solve this,  I employed a “defaultdict structure” to track word occurrences by date, which then helped visualize how the top words’ frequencies changed over time even when not used for certain dates. When choosing my visualization approach, I initially considered both line and bar charts.  

After testing with line charts, I observed that they provided a clearer picture of trends over time, particularly when tracking multiple words across dates.   

Through my project, I successfully retrieved and processed recent news articles, uncovering insightful patterns in the content. By analyzing word frequencies in article titles and descriptions, I identified the three most frequently mentioned words within my dataset. I visualized the occurrence of these words over time, allowing us to observe trends and fluctuations in their coverage. For example, I ran my script using the word “Trump.” I was surprised to see occurrence of words like “Elon Musk” or “authoritarian” in the word cloud which was interesting to me. This analysis highlighted the intensity of media focus on certain themes, depending on current events, and also highlights some patterns between things that are intrinsically related; which was insightful for understanding how specific topics gain or lose prominence in the news cycle.  

The visualization of word frequencies over time revealed several interesting patterns. For instance, there were noticeable spikes in certain words on specific dates, suggesting that these days had significant events related to those terms. By plotting these trends, I was able to see how the media narrative around keywords evolved over the week. For example, when I used the term "election," I saw a consistent presence but spiked in coverage on specific dates, likely tied to breaking news or significant political events. Such patterns give a clear picture of how news coverage shifts in response to real-world developments.  

Furthermore, I explored options for sentiment analysis, which I initially implemented using the NTLK library, but then switched to the OpenAI API to perform the sentiment analysis. It gives another dimension, for example when analyzing the overall sentiment around the articles related to “Trump” or to “Politics.” Overall, the project gave me some interesting insights into media trends, helping to understand not only the prominent topics in the news but also the way these topics are discussed over time. The combination of word frequency analysis and time-based visualization ended up being a good way for revealing patterns in how the media covers current events.  

Throughout the project, I had a lot of issues that I solved using previous codes that we wrote and ChatGPT. For example: 

- Handling the dates for the line chart 
- Accessing the API keys from my env. Folder 
- Implementing the ChatGPT API for sentiment analysis 
- OpenAI returning text which can’t be processed for sentiment analysis scoring 

ChatGPT would often give some results but it would be based on previous versions of the API for example which would not help. I would get errors and ChatGPT would say “The error indicates that the code is using an outdated API method (openai.ChatCompletion.create), which is no longer supported in the latest version of the OpenAI Python library. Since you’re on a newer version, we’ll need to update the code to be compatible with the new interface. If you want to avoid modifying your code and are okay with using the older version of the openai library, you can downgrade it” which would not work.  
Something good that I did this time was testing each part of my code progressively. For example, I made sure that my entire article retrieving process worked, so whenever I had an error, I knew it was not in this part of the code. I think it made my progress faster.  
Throughout the assignment, even if ChatGPT would often give outdated solutions or suggest some code that did not always fit my project, it was very helpful in identifying errors and understanding where they come from. Sometime the code it gave worked well but I would not understand it, so I engaged in conversation to understand exactly what it meant or if it could be simplified.  