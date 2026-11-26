"""
HTML to A4 High-Resolution PNG Generator
支援兩種模式：
1. Playwright (首選，支援字型/KaTeX等待與 Retina 2x 高解析度)
2. 系統內建 Edge/Chrome Headless (免安裝任何套件的備援模式)
"""

import sys
import os
import time
import subprocess
from pathlib import Path

# 專案路徑定位
PROJECT_ROOT = Path(__file__).resolve().parent.parent
HTML_DIR = PROJECT_ROOT / "html"
PNG_DIR = PROJECT_ROOT / "png"

# 確保輸出目錄存在
PNG_DIR.mkdir(parents=True, exist_ok=True)

DEFAULT_INPUT_HTML = HTML_DIR / "01_agent_based_model_vivid.html"
DEFAULT_OUTPUT_PNG = PNG_DIR / "01_agent_based_model.png"

def find_system_browser():
    """尋找 Windows 系統內建的 Edge 或 Chrome 瀏覽器"""
    candidates = [
        r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
        r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    ]
    for p in candidates:
        if os.path.exists(p):
            return p
    return None

def convert_with_playwright(input_file, output_file):
    print("▶ 偵測到 Playwright，啟動高解析度無頭渲染引擎...")
    from playwright.sync_api import sync_playwright

    with sync_playwright() as p:
        # 啟動 Chromium
        browser = p.chromium.launch(headless=True)
        # 設定 A4 標準比例與 2x Retina 像素倍率 (1588 x 2246 像素)
        context = browser.new_context(
            viewport={"width": 794, "height": 1123},
            device_scale_factor=2
        )
        page = context.new_page()

        file_url = input_file.resolve().as_uri()
        print(f"  載入網頁: {file_url}")
        page.goto(file_url, wait_until="networkidle")

        # 等待 KaTeX 數學式與 Google Fonts 載入完成
        try:
            page.wait_for_selector(".katex", timeout=5000)
        except Exception:
            pass
        time.sleep(1) # 讓字型抗鋸齒平滑渲染

        # 針對 .a4-page 容器截圖，確保完全貼合無邊界黑底
        card_element = page.query_selector(".a4-page")
        if card_element:
            card_element.screenshot(path=str(output_file))
        else:
            page.screenshot(path=str(output_file), full_page=True)

        browser.close()
    print(f"✔ 成功輸出高畫質圖卡至: {output_file}")
    return True

def convert_with_system_browser(input_file, output_file):
    browser_exe = find_system_browser()
    if not browser_exe:
        print("❌ 未找到系統瀏覽器 (Edge/Chrome)。請安裝 Playwright：pip install playwright && playwright install chromium")
        return False

    print(f"▶ 使用系統瀏覽器無頭模式: {browser_exe}")
    file_url = input_file.resolve().as_uri()

    # 視窗尺寸為標準 A4 2x (1588x2246)
    cmd = [
        browser_exe,
        "--headless",
        "--disable-gpu",
        "--hide-scrollbars",
        f"--window-size=1588,2246",
        f"--screenshot={str(output_file)}",
        file_url
    ]

    try:
        subprocess.run(cmd, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(f"✔ 成功輸出圖卡至: {output_file}")
        return True
    except Exception as e:
        print(f"❌ 截圖執行失敗: {e}")
        return False

def main():
    input_file = Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_INPUT_HTML
    output_file = Path(sys.argv[2]) if len(sys.argv) > 2 else DEFAULT_OUTPUT_PNG

    if not input_file.exists():
        print(f"❌ 找不到來源檔案: {input_file}")
        return

    print("==================================================")
    print("   單頁教學圖卡 PNG 轉檔器 (Infographic Exporter)")
    print("==================================================")
    print(f"來源 HTML: {input_file.name}")
    print(f"目標 PNG : {output_file.name}")

    # 執行風格合規檢查
    try:
        from lint_style import lint_file, print_report
        passed, errors, warnings = lint_file(input_file)
        print_report(input_file, passed, errors, warnings)
        if not passed:
            print("\n🚨 【風格攔截】圖卡風格未達標，請依上方提示修正後再輸出！")
            sys.exit(1)
        print("✨ 風格檢查通過，進入無頭瀏覽器高解析度渲染流程...\n")
    except ImportError:
        pass

    # 優先嘗試 Playwright
    try:
        import playwright
        convert_with_playwright(input_file, output_file)
    except ImportError:
        print("ℹ 系統未安裝 playwright 模組，自動切換至 Windows 內建瀏覽器引擎...")
        convert_with_system_browser(input_file, output_file)

if __name__ == "__main__":
    main()
