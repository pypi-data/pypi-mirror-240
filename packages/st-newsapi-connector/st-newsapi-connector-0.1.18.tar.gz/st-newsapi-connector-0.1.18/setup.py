# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['st_newsapi_connector']

package_data = \
{'': ['*']}

install_requires = \
['pandas==1.5.1', 'pycountry==22.3.5', 'requests==2.31.0', 'streamlit==1.28.1']

setup_kwargs = {
    'name': 'st-newsapi-connector',
    'version': '0.1.18',
    'description': 'A Python package to query data from NewsAPI in Streamlit apps',
    'long_description': '[![Open_inStreamlit](https://img.shields.io/badge/Open%20In-Streamlit-red?logo=Streamlit)](https://newsapi-connector.streamlit.app/)\n[![Python](https://img.shields.io/badge/python-%203.8-blue.svg)](https://www.python.org/)\n[![PyPi](https://img.shields.io/pypi/v/st-newsapi-connector)](https://pypi.org/project/st-newsapi-connector/)\n[![Build](https://img.shields.io/github/actions/workflow/status/dcarpintero/st-newsapi-connector/codecov.yml?branch=main)](https://pypi.org/project/st-newsapi-connector/)\n[![CodeFactor](https://www.codefactor.io/repository/github/dcarpintero/st-newsapi-connector/badge)](https://www.codefactor.io/repository/github/dcarpintero/st-newsapi-connector)\n[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://github.com/dcarpintero/st-newsapi-connector/blob/main/LICENSE)\n\n# 📰 Streamlit-NewsAPI Data Connector\n\n<p align="center">\n  <img src="./assets/st-newsapi-connector.png">\n</p>\n\nConnect to [NewsAPI](https://newsapi.org/) from your Streamlit app. Powered by ```st.experimental_connection()```. Works with Streamlit >= 1.22. Read more about Streamlit Connections in the [official docs](https://blog.streamlit.io/introducing-st-experimental_connection/). \n\nContributions to this repo are welcome. If you are interested in helping to maintain it, reach out to us. \n\n## 🚀 Quickstart\n\n1. Clone the repository:\n```\ngit clone git@github.com:dcarpintero/st-newsapi-connector.git\n```\n\n2. Create and Activate a Virtual Environment:\n\n```\nWindows:\n\npy -m venv .venv\n.venv\\scripts\\activate\n\nmacOS/Linux\n\npython3 -m venv .venv\nsource .venv/bin/activate\n```\n\n3. Install dependencies:\n\n```\npip install -r requirements.txt\n```\n\n4. Launch Web Application\n\n```\nstreamlit run ./app.py\n```\n\n## 📄 Minimal Integration\n\n```python\n# src/app.py\n\nimport streamlit as st\nfrom st_newsapi_connector.connection import NewsAPIConnection\n\nconn_newsapi = st.connection("NewsAPI", type=NewsAPIConnection)\n\n# Retrieves News Articles on a specific topic from the NewsAPI\ndf = conn_newsapi.everything(topic="AI, LLMs")\nst.dataframe(df)\n\n# Retrieves Top-Headlines in a country and category from the NewsAPI\ndf = conn_newsapi.top_headlines(country=\'US\', category=\'Science\')\nst.dataframe(df)\n```\n\n```toml\n# .streamlit/secrets.toml\n\nNEWSAPI_KEY = \'your-newsapi-key\'\nNEWSAPI_BASE_URL = \'https://newsapi.org/v2/\'\n```\n\n```txt\n# requirements.txt\n\npandas==1.5.1\npycountry==22.3.5\nrequests==2.31.0\nstreamlit==1.28.1\n```\n\n## 👩\u200d💻 Streamlit Web App\n\nDemo Web App deployed to [Streamlit Cloud](https://streamlit.io/cloud) and available at https://st-newsapi-connector.streamlit.app/ \n\n## 📚 References\n\n- [Streamlit BaseConnection](https://docs.streamlit.io/library/api-reference/connections/st.connections.baseconnection)\n- [Streamlit Connection](https://docs.streamlit.io/library/api-reference/connections/st.connection)\n- [Get Started with Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud/get-started)\n- [NewsAPI Dcoumentation](https://newsapi.org/docs)\n\n',
    'author': 'D. Carpintero',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://st-newsapi-connector.streamlit.app/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.9',
}


setup(**setup_kwargs)
