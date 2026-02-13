from fastapi import FastAPI

app = FastAPI()

db = {
    "P00202469": {"id": "P00202469", "name": "BadLogic", "qualification": "Senior Software Engineer"},
    "P00202470": {"id": "P00202470", "name": "John Doe", "qualification": "Software Engineer"},
    "P00202471": {"id": "P00202471", "name": "Jane Smith", "qualification": "Junior Software Engineer"},
}

@app.get("/")
def read_root():
    return {"Hello": "iiiiii"}

@app.get("/cert/{cert_id}")
def read_cert(cert_id: str):
    """Returns the certificate information for the given certificate ID."""
    
    if not validate_cert(cert_id):
        return {"error": "Invalid certificate ID format"}
    
    if not verify_cert(cert_id):
        return {"error": "Certificate ID not found in the database"}
    
    return db.get(cert_id)

def verify_cert(cert_id: str) -> bool:
    """Verifies the certificate ID against the database."""
    return cert_id in db    

def validate_cert(cert_id: str) -> bool:
    """Validates the certificate ID against the database."""
    
    # If it starts with P00 and is 8 characters long, it's valid
    if cert_id.startswith("P00") and len(cert_id) == 9:
        return True
    else:
        return False