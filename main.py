from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    name = "Zhyldyz"  
    skills = ["Linux", "Docker", "AWS"]
    return templates.TemplateResponse("portfolio.html", {"request": request, "name": name, "skills": skills})
