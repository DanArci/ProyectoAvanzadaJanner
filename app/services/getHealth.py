from routes.router import router

@router.get("/health", summary="System Health")
def get_health():
    return {"status": "ok"}