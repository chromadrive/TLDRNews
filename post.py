try:
    from urllib.parse import urlparse  # Python 3
except ImportError:
    from urlparse import urlparse  # Python 2 (ugh)

class Post():
	def __init__(self, link, title, authors, image, summary):
		self.link = link
		self.title = title
		self.authors = self.author_str(authors)
		self.image = image
		self.summary = self.summary_str(summary)
		self.publisher = urlparse(link).hostname.split('.')[1]

	def author_str(self, authors):
		auth_string = ""
		for author in authors:
			auth_string += (author + ", ")
		return auth_string[:-2]

	def summary_str(self, summary):
		summ_string = ""
		for sentence in summary:
			summ_string += (sentence + ' ')
		if summ_string[0] == '”':
			return summ_string[1:]
		return summ_string

	def print_post(self):
		#For debugging purposes
		print(self.link)
		print(self.title.upper())
		print(self.authors)
		print(self.image)
		print('================')
		print(self.summary)
		print('\n\n')
