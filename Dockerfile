# Use official Python slim image for a smaller footprint
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy application files
COPY app.py recipe_analyzer.py recipe_analysis.py nutrition_info.py streamlit_app.py ./
COPY requirements.txt ./
COPY .env ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Set environment variable for Streamlit
ENV STREAMLIT_SERVER_PORT=8501
ENV STREAMLIT_SERVER_ADDRESS=0.0.0.0

# Run Streamlit app
CMD ["streamlit", "run", "streamlit_app.py"]