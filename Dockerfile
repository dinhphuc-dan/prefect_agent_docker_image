# We're using the latest version of Prefect with Python 3.10
FROM prefecthq/prefect:2.14-python3.10
WORKDIR /app

# Add our requirements.txt file to the image and install dependencies
COPY requirements.txt /app
RUN pip install -r requirements.txt --trusted-host pypi.python.org --no-cache-dir

ENV CURL_CA_BUNDLE=''
ENV PYTHONHTTPSVERIFY='false'
