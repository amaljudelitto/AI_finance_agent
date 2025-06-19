import warnings
warnings.filterwarnings('ignore')

%pip install openai  langchain langchain-openai yfinance agno

from google.colab import files
uploaded = files.upload()  # Upload secret.env manually

