from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    
    summary_ = "CyberArk Labs discovered a new malware called Vare that is distributed over the popular chatting service, Discord. Vare has been used to target new malware operators by using social engineering tactics on them. Additionally, we have found that Vare uses Discord’s infrastructure as a backbone for its operations. This malware is linked to a new group called “Kurdistan 4455” based out of southern Turkey and is still early in its forming stage."
    content_ = [
        {"title": "vava's first blog", "posted_on": '12-12-12', 'summary': summary_,"image": "static/images/header-image-.webp"},
        {"title": "vava's second blog", "posted_on": '12-12-12', 'summary': summary_,"image": "static/images/header-image-.webp"},
        {"title": "vava's third blog", "posted_on": '12-12-12', 'summary': summary_,"image": "static/images/header-image-.webp"},
        {"title": "vava's fourth blog", "posted_on": '12-12-12', 'summary': summary_,"image": "static/images/header-image-.webp"}
    ]
    return templates.TemplateResponse("index.html", {"request": request, "contents": content_})

