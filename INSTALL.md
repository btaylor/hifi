Installing hifi
===============

1. Create a local `virtualenv` environment and activate it:

		virtualenv --no-site-packages virtualenv/
		source virtualenv/bin/activate

2. Install required packages from pip:

		pip install < requirements.txt

3. Set up `nltk`:

		python
		>>> import nltk
		>>> nltk.download()
