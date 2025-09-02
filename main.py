import uvicorn,os
from sketchstar.core import *

print(app.routes)

if __name__ == "__main__":
    uvicorn.run('sketchstar.core:app', host="0.0.0.0", port=5001 if os.getenv("PLASH_PRODUCTION") else 5002, reload=True)