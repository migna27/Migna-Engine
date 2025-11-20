import time
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# --- Metadata ---
ENGINE_VERSION = "0.1.0"
START_TIME = time.time()

# --- FastAPI App Initialization ---
app = FastAPI(
    title="Migna Engine API",
    description="API para gestionar el motor de novelas visuales Migna.",
    version=ENGINE_VERSION,
)

# --- CORS Configuration ---
# Permite que el frontend (que se ejecutará en otro puerto) se comunique con este servidor.
# Usamos "*" temporalmente para el desarrollo, como indica el manual.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Endpoints ---
@app.get("/")
def get_root():
    """Endpoint raíz que confirma que el motor está en funcionamiento."""
    return {"engine": "Migna", "status": "ok"}

@app.get("/api/health")
def get_health_status():
    """Devuelve el estado de salud del motor, su versión y tiempo de actividad."""
    uptime_seconds = time.time() - START_TIME
    return {
        "engine_version": ENGINE_VERSION,
        "status": "online",
        "uptime_seconds": round(uptime_seconds, 2)
    }

# --- Server Execution ---
if __name__ == "__main__":
    import uvicorn
    print("Iniciando servidor de Migna Engine en http://127.0.0.1:8000")
    uvicorn.run(app, host="127.0.0.1", port=8000)
