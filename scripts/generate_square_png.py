import time
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

# 引入風格防呆檢驗器
try:
    from lint_style import lint_file, print_report
except ImportError:
    lint_file = None

input_html = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else (Path(__file__).parent.parent / "html" / "03_neural_networks_square.html").resolve()
output_png = Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else (Path(__file__).parent.parent / "png" / "03_neural_networks_square.png").resolve()

print("==================================================")
print("   正方形 1:1 社群圖卡 PNG 轉檔器 (Square Exporter)")
print("==================================================")
print(f"來源 HTML: {input_html.name}")
print(f"目標 PNG : {output_png.name}")

# 執行自動風格審查
if lint_file:
    passed, errors, warnings = lint_file(input_html)
    print_report(input_html, passed, errors, warnings)
    if not passed:
        print("\n🚨 【風格攔截】圖卡風格未達標，請依上方提示修正後再輸出！")
        sys.exit(1)
    print("✨ 風格檢查通過，進入無頭瀏覽器高解析度渲染流程...\n")

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
