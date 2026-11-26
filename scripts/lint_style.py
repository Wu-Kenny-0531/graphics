"""
Da Vinci Style Linter (達文西手稿風格自動檢查器)
檢查 HTML 圖卡是否完全符合 STYLE_GUIDE.md 與 AGENTS.md 的視覺與內容規範。
"""

import sys
import re
from pathlib import Path

# 規範禁語表（嚴禁出現現代感贅字）
FORBIDDEN_PATTERNS = [
    (r"達文西手繪手札卷", "禁止出現『達文西手繪手札卷』說明贅詞"),
    (r"手繪手札卷[一二三四五六七八九十\d]", "禁止出現『手繪手札卷X』贅詞"),
    (r"手札卷[一二三四五六七八九十\d]", "禁止出現『手札卷X』贅詞"),
    (r"手稿考卷", "禁止出現『手稿考卷』現代考試用詞"),
    (r"考試重點", "禁止出現『考試重點』現代教材用詞"),
]

# 核心手稿六大規範檢測規則 (嚴格對齊 STYLE_GUIDE.md)
REQUIRED_PATTERNS = [
    ("繁體手寫字型", r"JasonHandwriting5", "需正確引入 JasonHandwriting5 繁體手寫字體"),
    ("英文墨水草寫體", r"Caveat", "需引入 Caveat 字型用於拉丁文、標籤與簽名"),
    ("羊皮紙基底色碼", r"--parchment-base", "CSS 需定義 --parchment-base 羊皮紙色 (#f0e4cb)"),
    ("古典深褐墨水", r"--ink-primary", "CSS 需定義 --ink-primary 古籍墨水色 (#1e1309)"),
    ("朱砂火漆印章", r"(--seal-red|\.seal|印章|Seal)", "需包含朱砂紅印章元素 (--seal-red / .seal)"),
    ("頁尾草寫簽名", r"(\.signature|scripsit)", "頁尾需包含學者草寫簽名 (class='signature' 或 scripsit)"),
    ("拉丁文題頭/卷號", r"(Folio|Tractatus|Codex|Frontispiece)", "頂部或頁尾需標註古典拉丁文卷號 (如 Folio / Tractatus)"),
    ("手繪向量圖解 (SVG)", r"<svg", "核心解說圖必須採用內嵌輕量向量 SVG 繪製"),
    ("手繪有機顫筆邊框", r"(border-radius:\s*\d{2,3}px\s+\d{1,2}px|jitter|jittered|organic)", "區塊邊框需採用手繪有機顫筆曲率或抖動樣式"),
]

def lint_file(file_path: Path) -> tuple[bool, list[str], list[str]]:
    """
    檢查單一 HTML 檔案是否符合達文西手稿規範。
    回傳 (is_passed, errors, warnings)
    """
    if not file_path.exists():
        return False, [f"找不到檔案：{file_path}"], []

    content = file_path.read_text(encoding="utf-8", errors="ignore")
    errors = []
    warnings = []

    # 1. 禁詞檢查
    for pattern, msg in FORBIDDEN_PATTERNS:
        matches = re.findall(pattern, content)
        if matches:
            errors.append(f"【禁詞違規】發現 {len(matches)} 處：{msg}")

    # 2. 必要手稿元素檢查
    for name, pattern, hint in REQUIRED_PATTERNS:
        if not re.search(pattern, content, re.IGNORECASE):
            errors.append(f"【元素缺失】未找到「{name}」：{hint}")

    # 3. 現代色彩違規警告（檢查是否直接在大區塊使用純白背景）
    if re.search(r"background(-color)?\s*:\s*#ffffff\b", content, re.IGNORECASE):
        warnings.append("【色彩警示】偵測到使用純白背景 (#ffffff)，建議改用 var(--parchment-base)")

    is_passed = len(errors) == 0
    return is_passed, errors, warnings


def print_report(file_path: Path, is_passed: bool, errors: list[str], warnings: list[str]):
    print(f"\n📄 檢驗檔案: {file_path.name}")
    print("-" * 55)
    if is_passed and not warnings:
        print("  ✨ [100% 合規] 完全符合達文西手稿古籍風格標準！")
    elif is_passed:
        print("  ✔ [風格合規] 通過核心門檻，但有以下建議：")
        for w in warnings:
            print(f"    ⚠ {w}")
    else:
        print("  ✖ [風格違規] 發現風格偏離或關鍵元素缺失：")
        for e in errors:
            print(f"    ❌ {e}")
        for w in warnings:
            print(f"    ⚠ {w}")


def main():
    root = Path(__file__).parent.parent
    html_dir = root / "html"

    # 如果有給定參數，檢查指定檔案；否則檢查所有達文西系列圖卡
    if len(sys.argv) > 1:
        targets = [Path(sys.argv[1]).resolve()]
    else:
        # 掃描所有正式產出之圖卡（排除底線開頭之模板 _template）
        all_htmls = (list(html_dir.glob("*_davinci.html")) + 
                     list(html_dir.glob("*_square.html")) + 
                     list(html_dir.glob("*_landscape.html")))
        targets = sorted([f for f in all_htmls if not f.name.startswith("_")])

    print("==================================================")
    print("   📜 達文西手稿風格自動檢查器 (Da Vinci Style Linter)")
    print("==================================================")

    all_passed = True
    for target in targets:
        passed, errors, warnings = lint_file(target)
        print_report(target, passed, errors, warnings)
        if not passed:
            all_passed = False

    print("\n" + "=" * 55)
    if all_passed:
        print("🎉 全部圖卡通過風格檢核！完美保持一致性。")
        sys.exit(0)
    else:
        print("🚨 部分圖卡存在風格偏離，請依上方提示修正。")
        sys.exit(1)


if __name__ == "__main__":
    main()
