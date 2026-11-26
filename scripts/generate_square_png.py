import time
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

input_html = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path("html/03_neural_networks_square.html").resolve()
output_png = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else Path("png/03_neural_networks_square.png").resolve()

print("==================================================")
print("   正方形 1:1 社群圖卡 PNG 轉檔器 (Square Exporter)")
print("==================================================")
print(f"來源 HTML: {input_html.name}")
print(f"目標 PNG : {output_png.name}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # 800x800 with 2x scale -> 1600x1600 px Retina Square
    context = browser.new_context(
        viewport={"width": 800, "height": 800},
        device_scale_factor=2
    )
    page = context.new_page()
    page.goto(input_html.as_uri(), wait_until="networkidle")
    try:
        page.wait_for_selector(".katex", timeout=5000)
    except Exception:
        pass
    time.sleep(1)

    card = page.query_selector(".square-card")
    if card:
        card.screenshot(path=str(output_png))
    else:
        page.screenshot(path=str(output_png), full_page=True)
    browser.close()

print(f"✔ 成功輸出 1600x1600 正方形高清社群圖卡至: {output_png}")
