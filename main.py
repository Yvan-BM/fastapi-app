
from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
import imquality.brisque as brisque
import shutil
import PIL.Image

app = FastAPI()


# class Image(BaseModel):
#     file: Image


@app.post("/upload/")
async def upload_image(myfile: UploadFile):
    with open(f'{myfile.filename}', "wb") as buffer:
        shutil.copyfileobj(myfile.file, buffer)
    # brisque.score(contents)
    return {"file_name": myfile.filename, "file_type": myfile.content_type}

@app.post("/image/check")
def image_quality(name: str):
    img = PIL.Image.open(name)
    return{"quality": brisque.score(img)}