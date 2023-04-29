# mundane imports
import uvicorn
import os

# fastapi imports
from fastapi import FastAPI
from starlette.responses import FileResponse
from starlette.background import BackgroundTasks

# repo specific
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write


# ---- setting up App ----
output_path = "static/mp3/out.wav"
app = FastAPI()
preload_models(text_use_gpu = False, coarse_use_gpu = False, fine_use_gpu = False, codec_use_gpu = False)


def remove_file(path: str) -> None:
    os.remove(path)

@app.post("/", response_class = FileResponse)
async def root(input_text: str, background_tasks: BackgroundTasks):
    audio_array = generate_audio(input_text)
    write(output_path, SAMPLE_RATE, audio_array)

    # will be executed after the reponse.
    background_tasks.add_task(remove_file, output_path)
    return FileResponse(output_path, media_type='audio/mp3', filename="out.wav")

if __name__ == "__main__":
    uvicorn.run("test:app", host = "127.0.0.1", port = 9000, reload = True)
	