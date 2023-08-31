# Pull the Python base image
FROM python:3.10-slim-bullseye

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /app

# Install dependencies
RUN apt-get update \
    && apt-get -y install git gcc libgomp1 make

# Clone the repository
RUN git clone --recursive https://github.com/ashwinprasadme/HeaderGen.git
RUN cd HeaderGen \
    && git submodule update --init --recursive \
    && git pull --recurse-submodules

WORKDIR /app/HeaderGen

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -e .

# Create headergen cache
RUN python /app/HeaderGen/scripts/start_headergen_cache.py

# Keep the container alive
CMD ["bash"]
