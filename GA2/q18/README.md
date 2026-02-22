# Q18: FastAPI File Validation Service

A FastAPI service that validates file uploads (type, size, auth) and processes CSV files.

## Endpoint

`POST /upload`

# SecureUpload Data Processor

FastAPI service for validating and processing departmental CSV uploads.

## Validation Rules

1.  **Authentication**: Header `X-Upload-Token-9368: f24v9gj5omoqssjc` (401 Unauthorized)
2.  **File Type**: `.csv`, `.json`, `.txt` (400 Bad Request)
3.  **File Size**: Max 55KB (413 Payload Too Large)

## Running the Service

```bash
pip install -r requirements.txt
python main.py

## Request

-   Method: `POST`
-   Content-Type: `multipart/form-data`
-   Field: `file`

## Response (Success)

For a valid CSV upload:

```json
```json
{
  "email": "23f3001889@ds.study.iitm.ac.in",
  "filename": "data.csv",
  "rows": 40,
  "columns": ["id", "name", "value", "category"],
  "totalValue": 17971.25,
  "categoryCounts": {"D":11, "C":9, "B":12, "A":8}
}
```

## Running the Service

```bash
# Install dependencies
pip install -r requirements.txt

# Run server (port 8001 to avoid conflicts)
python main.py
```

## Testing

```bash
python test2.py
```
