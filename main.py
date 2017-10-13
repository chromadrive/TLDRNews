from newspaper import Article
from post import Post
from summary import *

from flask import Flask, request, render_template, redirect

api_key = '9a61551efd114daca1c08c9b65620bf4'
host = 'http://localhost:5000/' # Change for deployment

app = Flask(__name__)
summarize = Summary()

urls = ["http://www.latimes.com/nation/la-na-boy-scouts-girls-20171011-story.html",
		"https://www.washingtonpost.com/news/post-nation/wp/2017/10/10/pure-devastation-at-least-15-dead-as-firefighters-struggle-to-weaken-california-fires/",
		"https://www.washingtonpost.com/politics/trump-expected-to-tap-kirstjen-nielsen-to-lead-department-of-homeland-security/2017/10/11/21770f8e-aeaf-11e7-9e58-e6288544af98_story.html",
		"https://www.nytimes.com/2017/10/11/business/economy/nafta-trump.html"]
posts = []

def generate_posts(urls):
	for url in urls:
		article = Article(url)
		article.download()
		article.parse()
		post = Post(url, article.title, article.authors, article.top_image, 
					summarize.reduce(article.text.replace('\n', ' '), 0.035))
		posts.append(post)
generate_posts(urls)


@app.route('/', methods=['GET'])
def index():
	return render_template('index.html', posts = posts)

if __name__ == '__main__':
    app.run(debug=True)

