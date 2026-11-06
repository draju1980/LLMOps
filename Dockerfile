FROM python:3.11-slim

WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git curl make postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Create combined requirements with core dependencies
RUN echo "duckdb==1.0.0\npydantic==2.5.0\npytest==9.0.2\npytest-asyncio==0.21.0\naiohttp==3.9.0\nfastapi==0.104.1\nuvicorn==0.24.0\npython-dotenv==1.0.0\ntransformers==4.36.0\ntorch==2.1.0\nscikit-learn==1.3.2\npandas==2.1.0\nnumpy==1.24.3\nPyYAML==6.0\njinja2==3.1.2\nrequests==2.31.0" > /tmp/requirements.txt

RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copy entire course
COPY . /workspace/

WORKDIR /workspace

# Default command
CMD ["/bin/bash"]
