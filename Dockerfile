FROM python:3.9

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY index.html /usr/local/lib/python3.9/site-packages/streamlit/static/index.html
COPY . .

CMD ["streamlit", "run", "Home.py", "--server.headless", "true", "--server.fileWatcherType", "none", "--browser.gatherUsageStats=False"]

