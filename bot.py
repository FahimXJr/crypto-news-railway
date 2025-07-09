import os
import requests
from telegram import Bot

TELEGRAM_BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN')
CHANNEL_ID = os.getenv('CHANNEL_ID')  # e.g. '@yourchannel'
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

bot = Bot(token=TELEGRAM_BOT_TOKEN)

def get_crypto_news():
    url = ('https://newsapi.org/v2/everything?'
           'q=cryptocurrency&'
           'language=en&'
           'sortBy=publishedAt&'
           f'apiKey={NEWS_API_KEY}')
    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])
    news_messages = []
    for article in articles[:3]:
        title = article['title']
        url = article['url']
        news_messages.append(f"{title}\nRead more: {url}")
    return news_messages

def post_news():
    news_list = get_crypto_news()
    for news in news_list:
        bot.send_message(chat_id=CHANNEL_ID, text=news)

if __name__ == '__main__':
    post_news()
