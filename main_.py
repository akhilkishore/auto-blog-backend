from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
###############
from content import overview
###############

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")





def prepare_overview(content_list):
    
    full_content = ""
    for item in content_list:
        title_ = item['title']
        posted_on_ = item['posted_on']
        summary_ = item['summary']
        post_ = overview.format(title_,posted_on_,summary_)
        full_content += post_
    return full_content
    
    
    
    





# @app.get("/items/{id}", response_class=HTMLResponse)
# async def read_item(request: Request, id: str):
#     return templates.TemplateResponse("item.html", {"request": request, "id": id})

@app.get("/home", response_class=HTMLResponse)
async def read_item(request: Request):
    c_ = [
        {"title": "vava's first blog", "posted_on": '12-12-12', 'summary': "vava's first post on nandhu's blog"},
        {"title": "vava's second blog", "posted_on": '12-12-12', 'summary': "vava's second post on nandhu's blog"},
        {"title": "vava's third blog", "posted_on": '12-12-12', 'summary': "vava's third post on nandhu's blog"},
        {"title": "vava's fourth blog", "posted_on": '12-12-12', 'summary': "vava's fourth post on nandhu's blog"}
    ]
    content_ = prepare_overview(c_)
    return templates.TemplateResponse("index.html", {"request": request, "content": content_})

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

