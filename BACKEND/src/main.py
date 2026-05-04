from fastapi import FastAPI 
from rag import get_answer
import uvicorn
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import os 
app = FastAPI(title="DRAGO AI")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   
    allow_methods=["*"],
    allow_headers=["*"],
)

FRONTEND_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "FRONTEND")
frontend_file=os.path.join(FRONTEND_PATH,"frontend.html")
app.mount("/static", StaticFiles(directory=FRONTEND_PATH), name="static")

@app.get("/")
def serve_frontend():
    """Serve the main frontend HTML page"""
    if os.path.exists(frontend_file):
        return FileResponse(frontend_file)
    else:
        return {
            "error": "Frontend not found",
            "message": f"Please place frontend.html in: {FRONTEND_PATH}",
            "status": "backend_running"
        }
        
@app.get("/health")
def health_check():
    """Check if backend is running"""
    return {
        "status": "healthy",
        "service": "DRAGO AI",
        "timestamp": __import__("datetime").datetime.now().isoformat()
    }
    
    
    
@app.get("/query")
def query(question: str):
    try:
        return {"answer": get_answer(query=question)}
    except Exception as e:
        return {"error": str(e)}
    
    


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",  
        port=8000,
        reload=True        
    )
