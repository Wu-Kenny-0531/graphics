import time
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

input_html = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (Path(__file__).parent.parent / "html" / "04_generative_models_landscape.html").resolve()
output_png = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else (Path(__file__).parent.parent / "png" / "04_generative_models_landscape.png").resolve()

print("==================================================")
print("   16:9 橫式專欄圖卡 PNG 轉檔器 (Landscape Exporter)")
print("==================================================")
print(f"來源 HTML: {input_html.name}")
print(f"目標 PNG : {output_png.name}")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    # 1280x720 with 2x scale -> 2560x1440 px Retina 16:9 Landscape
    context = browser.new_context(
        viewport={"width": 1280, "height": 720},
        device_scale_factor=2
    )
    page = context.new_page()
    page.goto(input_html.as_uri(), wait_until="networkidle")
    try:
        page.wait_for_selector(".katex", timeout=5000)
    except Exception:
        pass
    time.sleep(1)

    card = page.query_selector(".landscape-card")
    if card:
        card.screenshot(path=str(output_png))
    else:
        page.screenshot(path=str(output_png), full_page=True)
    browser.close()

print(f"✔ 成功輸出 2560x1440 16:9 橫式專欄高清圖卡至: {output_png}")
