from playwright.sync_api import sync_playwright
import pathlib
html = pathlib.Path("chat-vs-agent.html").resolve().as_uri()
with sync_playwright() as p:
    b = p.chromium.launch(channel="msedge")
    pg = b.new_page(viewport={"width":1500,"height":900}, device_scale_factor=2.6)
    pg.goto(html, wait_until="networkidle")
    pg.wait_for_timeout(1200)
    el = pg.query_selector(".wrap")
    el.screenshot(path="chat-vs-agent.png")
    box = el.bounding_box()
    print("rendered", box["width"], "x", box["height"], "css px")
    b.close()
