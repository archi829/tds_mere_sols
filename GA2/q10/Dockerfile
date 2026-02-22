FROM python:3.11-slim

# Create the user with UID 1000
RUN useradd -m -u 1000 user

# Ensure the app directory is owned by the user before switching WORKDIR
RUN mkdir -p /app && chown user:user /app
WORKDIR /app

# Switch to the non-root user
USER user

# Add the local bin to PATH so uvicorn can be found after pip install
ENV PATH="/home/user/.local/bin:${PATH}"

# Copy requirements and install
COPY --chown=user:user ./requirements.txt requirements.txt
RUN pip install --no-cache-dir --user --upgrade -r requirements.txt

# Copy the rest of the application
COPY --chown=user:user . .

# Set environment variables and expose port
# [cite_start]Ensure there are no citation brackets like [cite: 2] here
ENV APP_PORT=7006
EXPOSE 7006

# Use the environment variable in the CMD
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${APP_PORT}"]