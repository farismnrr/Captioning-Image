# Captioning-Image

## How to Install
### Install by Code
- Clone the repository
```sh
git clone https://github.com/farismnrr/Captioning-Image.git
```
- Change the directory `cd Captioning-Image`
- Create Virtual Environment (Windows)
```sh
pip install virtualenv
python -m venv myenv
myenv\Scripts\activate
```
- Create Virtual Environment (Linux)
```sh
sudo apt install python3-venv
python -m venv myenv
source myenv/bin/activate
```
- Install all depedendependencies
```sh
pip install -r requirements.txt
```
- Training the model and run the app
```
uvicorn main:app --reload --host 0.0.0.0 --port 80
```

### Install by Docker
```sh
docker run -d -p 8000:8000 --name image-captioning farismnrr/image-captioning:latest
```
