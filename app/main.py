from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Format API",
    description="API for converting mathematical formulas to various formats (PNG, LaTeX, MathML, etc.)",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "message": "Format API is running",
        "version": "1.0.0",
        "available_formats": ["png"],  # We'll expand this list later
        "endpoints": {
            "png": "/png/generate"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

# We'll add PNG router here in the next step