# mundane imports
import uvicorn
from typing import Annotated

# fastapi imports
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# repo specific
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav


# ---- setting up App ----
output_path = "static/mp3/out.wav"
app = FastAPI()
templates = Jinja2Templates(directory="static")
app.mount("/static", StaticFiles(directory="static"), name="static")

# --- Routes ---
@app.post("/predict", response_class = HTMLResponse)
async def predict(request: Request, input_text: Annotated[str, Form(...)]):
    audio_array = generate_audio(input_text)
    write_wav(output_path, SAMPLE_RATE, audio_array)
    return templates.TemplateResponse("templates/result.html", {"request": request, "prompt": input_text})

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("templates/index.html", {"request": request})


if __name__ == "__main__":
    preload_models(text_use_gpu = False, coarse_use_gpu = False, fine_use_gpu = False, codec_use_gpu = False)
    uvicorn.run("test:app", host = "127.0.0.1", port = 8000, reload = True)