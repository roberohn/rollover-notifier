# Use slim image compatible with Raspberry Pi (ARM)
FROM python:3.11-slim

WORKDIR /app

# install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY app/ .

# Run the script
CMD ["python", "main.py"]
