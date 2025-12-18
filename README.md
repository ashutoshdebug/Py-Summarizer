# Python Summarizer

* A summarizer built using Python. It can be used to extract text from a website (even a React one), and provides a summary over the extracted text using Google's Gemini

* Current version holds the capability of extracting the first page only


### It includes various Python modules:
```bash
google-genai
```

```bash
python-dotenv
```

```bash
beautifulsoup4
```

```bash
selenium
```

```bash
webdriver-manager
```

```bash
requests
```

## Getting started

* Clone the repository:
```bash
git clone https://github.com/ashutoshdebug/Py-Summarizer.git
cd Py-Summarizer
```

* Create a virtual env
```bash
python -m venv .venv
```

* Setup the Gemini API Key
```bash
echo GEMINI_API_KEY=YOUR_API_KEY_HERE > .env
```

* Install the required modules
```bash
pip install -r .\requirements.txt
```

## Contributing:

Feel free to contribute to this repository by raising issues!