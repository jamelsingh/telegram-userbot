
# Use official lightweight Python image
FROM python:3.10-slim

# Set work directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Set environment variables (optional defaults)
ENV API_ID=12345
ENV API_HASH=your_api_hash
ENV SESSION=userbot

# Run the bot
CMD ["python", "main.py"]
