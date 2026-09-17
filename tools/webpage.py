import re
import requests
from bs4 import BeautifulSoup
def read_webpage(url:str,max_chars:int=12000)->dict:
    if not url.startswith("http://","https://"):
        raise ValueError(
            "只支持http或https URL"
        )
    headers={
        "user-Agent":(
            "Mozilla/5.0"
            "ResearchAgent/0.6"
        )
    }
    response=requests.get(
        url,
        headers=headers,
        timeout=10,
    )

    response.raise_for_status()
    content_type=response.headers.get(
        "Content-Type",
        ""
    )

    if "text/html" not in content_type:
        raise ValueError(
            f"暂不支持该网页类型："
            f"{content_type}"
        )
    soup = BeautifulSoup(
        response.text,
        "html.parser"
    )

    for tag in soup(
        [
            "script",
            "style",
            "nav",
            "footer",
            "header",
            "noscript",
            "svg",
            "form",
        ]
    ):
        tag.decompose()

    content = (
        soup.find("article") or soup.find("main") or soup.body or soup
    )

    text = content.get_text(
        separator="\n",
        strip=True,
    )

    text = re.sub(
        r"\n{3,}",
        "\n\n",
        text,
    )

    title=""

    if soup.title:
        title=soup.title.get_text(
            strip=True
        )
    return{
        "title":title,
        "url":url,
        "content":text[:max_chars]
    }