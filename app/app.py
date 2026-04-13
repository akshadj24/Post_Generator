from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import Post_generation.generate_post as post_gen
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

# If your html is in app/templates/app.html



app = FastAPI()

# Enable CORS so your HTML file can talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, replace "*" with your domain
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data structure for the request
class PostRequest(BaseModel):
    topic: str
    language: str
    length: str

# Your custom Python logic
def generate_post_content(topic, lang, length):
    # --- Insert your custom logic/model here ---
    post=post_gen.generate_post(length, lang,topic)
    return post


@app.get("/")
async def read_index():
    return FileResponse('app/templates/app.html')


@app.post("/generate")
async def generate(request: PostRequest):
    # Access data using request.topic, request.language, etc.
    content = generate_post_content(request.topic, request.language, request.length)
    return {"post": content}

if __name__ == "__main__":
    
    uvicorn.run(app, host="127.0.0.1", port=8000)