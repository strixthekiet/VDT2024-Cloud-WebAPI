FROM python:3.10-slim
# Install dependencies in a single layer with caching
# Copy directly into build context
COPY requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Copy application code
# Set os environment variable
ENV MONGO_URL=localhost
COPY ./app /app
WORKDIR /app
# Start FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
