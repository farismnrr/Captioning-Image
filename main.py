from fastapi import FastAPI, File, UploadFile
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

app = FastAPI()

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

@app.get("/")
async def root():
    return {"message": "Server is connected"}

@app.post("/conditional_captioning")
async def conditional_captioning(image: UploadFile, text: str):
    raw_image = Image.open(image.file)
    inputs = processor(raw_image, text, return_tensors="pt")
    out = model.generate(**inputs)
    return {"caption": processor.decode(out[0], skip_special_tokens=True)}

@app.post("/unconditional_captioning")
async def unconditional_captioning(image: UploadFile):
    raw_image = Image.open(image.file)
    inputs = processor(raw_image, return_tensors="pt")
    out = model.generate(**inputs)
    return {"caption": processor.decode(out[0], skip_special_tokens=True)}
