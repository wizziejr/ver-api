from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()

db = {
    "P00202469": {"id": "P00202469", "name": "BadLogic", "qualification": "Senior Software Engineer"},
    "P00202470": {"id": "P00202470", "name": "John Doe", "qualification": "Software Engineer"},
    "P00202471": {"id": "P00202471", "name": "Jane Smith", "qualification": "Junior Software Engineer"},
}

@app.get("/")
def read_root():
    """Returns HTML file."""
    return FileResponse("http/index.html")  

@app.get("/certs/all")
def read_all_certs(offset: int = 0, limit: int = 10):
    """Returns a list of all certificates in the database."""
    return list(db.values())[offset:offset + limit]

@app.post("/cert/")
def create_cert(cert_id: str, name: str, qualification: str):
    """Creates a new certificate in the database."""
    # Validate the certificate ID format
    validate_cert(cert_id) 
    
    if cert_id in db:
        raise HTTPException(status_code=400, detail="Certificate ID already exists")
    
    db[cert_id] = {"id": cert_id, "name": name, "qualification": qualification}
    
    return {"message": f"Certificate created for {name}"}

@app.get("/cert/{cert_id}")
def read_cert(cert_id: str):
    """Returns the certificate information for the given certificate ID."""
    
    # Validate the certificate ID format
    validate_cert(cert_id)
    
    # Verify that the certificate ID exists in the database
    verify_cert(cert_id)
    
    return db.get(cert_id)

def verify_cert(cert_id: str):
    """Verifies the certificate ID against the database."""
    if cert_id not in db:
        raise HTTPException(status_code=404, detail="Certificate ID not found in the database")

def validate_cert(cert_id: str):
    """Validates the certificate ID against the database."""
    
    # If it starts with P00 and is 8 characters long, it's valid
    if not cert_id.startswith("P00"):
        raise HTTPException(status_code=400, detail="Certificate ID must start with 'P00'")
    
    if len(cert_id) != 9:
        raise HTTPException(status_code=400, detail="Certificate ID must be exactly 9 characters long")
