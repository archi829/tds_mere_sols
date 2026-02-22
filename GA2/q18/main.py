from fastapi import FastAPI, UploadFile, File, Header, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import csv
import io
import os

app = FastAPI()

# 1. Standard CORSMiddleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

# 2. Global Middleware to force CORS headers on every response (including errors)
@app.middleware("http")
async def add_cors_header(request: Request, call_next):
    # Handle preflight OPTIONS requests manually if needed
    if request.method == "OPTIONS":
        response = JSONResponse(content="OK")
    else:
        response = await call_next(request)
    
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

VALID_TOKEN = "f24v9gj5omoqssjc"
MAX_SIZE = 55 * 1024 
ALLOWED_EXTENSIONS = {".csv", ".json", ".txt"}

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...),
    x_upload_token_9368: str = Header(None),
):
    # Auth check
    if not x_upload_token_9368 or x_upload_token_9368 != VALID_TOKEN:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # File type check
    filename = file.filename or ""
    ext = os.path.splitext(filename)[1].lower()
    if ext not in ALLOWED_EXTENSIONS:
        raise HTTPException(status_code=400, detail="Bad Request")

    # Size check
    contents = await file.read()
    if len(contents) > MAX_SIZE:
        raise HTTPException(status_code=413, detail="Payload Too Large")

    # CSV Processing
    if ext == ".csv":
        text = contents.decode("utf-8")
        reader = csv.DictReader(io.StringIO(text))
        rows = list(reader)
        columns = list(rows[0].keys()) if rows else []

        total_value = 0.0
        category_counts = {}
        for row in rows:
            total_value += float(row.get("value", 0))
            cat = row.get("category", "Unknown")
            category_counts[cat] = category_counts.get(cat, 0) + 1

        return {
            "email": "23f3001889@ds.study.iitm.ac.in",
            "filename": filename,
            "rows": len(rows),
            "columns": columns,
            "totalValue": round(total_value, 2),
            "categoryCounts": category_counts,
        }

    return {"message": "File accepted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=9000)