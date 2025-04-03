# 1. Use an official Python runtime as a parent image
# Using 'slim' version for a smaller image size
FROM python:3.10-slim

# 2. Set the working directory in the container
WORKDIR /app

# 3. Copy the requirements file into the container at /app
COPY requirements.txt .

# 4. Install any needed packages specified in requirements.txt
# --no-cache-dir prevents pip from storing the download cache, keeping the image smaller
# --trusted-host pypi.python.org prevents potential SSL issues in some environments
RUN pip install --no-cache-dir --trusted-host pypi.python.org -r requirements.txt

# 5. Copy the current directory contents into the container at /app
COPY app.py .

# 6. Make port 5000 available to the world outside this container
EXPOSE 5000

# 7. Define environment variables (optional, but good practice)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# 8. Run app.py when the container launches
# Use exec form for CMD to handle signals properly
CMD ["python", "app.py"]
