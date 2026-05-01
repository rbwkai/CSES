import os
import re
import requests
from bs4 import BeautifulSoup, NavigableString, Tag
from urllib.parse import urljoin

BASE = "https://cses.fi"
OUT_DIR = "cses-md"


def slug(s: str) -> str:
    return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')


# ---------------- LOGIN ----------------
def login(user: str, password: str) -> requests.Session:
    s = requests.Session()
    url = f"{BASE}/login/"

    r = s.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    csrf = soup.find('input', {'name': 'csrf_token'})['value']

    r = s.post(url, data={
        'csrf_token': csrf,
        'nick': user,
        'pass': password
    })

    if not r.history:
        print("Login failed")
        exit(1)

    return s


# ---------------- MATH ----------------
def parse_math(tag):
    ann = tag.find("annotation", {"encoding": "application/x-tex"})
    tex = ann.text.strip() if ann else tag.text.strip()

    if "math-display" in tag.get("class", []):
        return f"\n\n$$\n{tex}\n$$\n\n"
    return f"${tex}$"


# ---------------- HTML → MD ----------------
def render(node):
    if isinstance(node, NavigableString):
        return str(node)

    if not isinstance(node, Tag):
        return ""

    if node.name in ["script", "style"]:
        return ""

    if node.name == "span" and "math" in node.get("class", []):
        return parse_math(node)

    if node.name == "p":
        return "".join(render(c) for c in node.children) + "\n\n"

    if node.name == "h1":
        return f"## {node.text.strip()}\n\n"

    if node.name == "ul":
        return "\n".join(f"- {render(li).strip()}" for li in node.find_all("li", recursive=False)) + "\n\n"

    if node.name == "li":
        return "".join(render(c) for c in node.children)

    if node.name == "pre":
        return f"```\n{node.text.strip()}\n```\n\n"

    return "".join(render(c) for c in node.children)


# ---------------- PROBLEM PARSE ----------------
def extract_problem(s, url):
    soup = BeautifulSoup(s.get(url).text, "lxml")

    title = soup.find("h1").text.strip()

    constraints_ul = soup.find("ul", {"class": "task-constraints"})
    time = constraints_ul.find_all("li")[0].text.strip()
    memory = constraints_ul.find_all("li")[1].text.strip()

    md_div = soup.find("div", {"class": "md"})

    body = "## Problem\n\n"
    for child in md_div.children:
        body += render(child)

    return title, time, memory, body, soup


# ---------------- SOLUTION ----------------
def get_latest_solution(s, soup):
    link = soup.find("a", href=re.compile(r"/problemset/result/"))
    if not link:
        return "// No submission found"

    sub_url = urljoin(BASE, link["href"])
    sub_soup = BeautifulSoup(s.get(sub_url).text, "lxml")

    code = sub_soup.find("pre", {"class": "linenums"})
    return code.text if code else "// No code found"


# ---------------- SAVE ----------------
def save_md(title, time, memory, body, code, section):
    folder = slug(section)
    dir_path = os.path.join(OUT_DIR, folder)
    os.makedirs(dir_path, exist_ok=True)

    filename = slug(title) + ".md"
    path = os.path.join(dir_path, filename)

    with open(path, "w") as f:
        f.write(f"# {title}\n\n")
        f.write(f"**{time}**  \n")
        f.write(f"**{memory}**\n\n")

        f.write("---\n\n")
        f.write(body)

        f.write("\n---\n\n")
        f.write("## Solution\n\n")
        f.write("```cpp\n")
        f.write(code.strip())
        f.write("\n```\n")

    print(f"✔ {section} -> {title}")


# ---------------- SCRAPE LIST (KEY PART) ----------------
def scrape_all(s):
    list_url = f"{BASE}/problemset/list/"
    soup = BeautifulSoup(s.get(list_url).text, "lxml")

    sections = soup.find_all("h2")

    for sec in sections:
        section_name = sec.text.strip()

        # everything until next h2
        for sibling in sec.find_next_siblings():
            if sibling.name == "h2":
                break

            if sibling.name == "ul":
                for a in sibling.find_all("a", href=True):
                    url = urljoin(BASE, a["href"])

                    try:
                        title, time, memory, body, soup2 = extract_problem(s, url)
                        code = get_latest_solution(s, soup2)
                        save_md(title, time, memory, body, code, section_name)
                    except Exception as e:
                        print(f"❌ Failed: {url} -> {e}")


# ---------------- RUN ----------------
if __name__ == "__main__":
    os.makedirs(OUT_DIR, exist_ok=True)

    user = input("username: ")
    pw = input("password: ")

    s = login(user, pw)
    scrape_all(s)
