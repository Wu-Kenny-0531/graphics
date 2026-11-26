---
name: infographic-pipeline
description: >-
  單頁 A4 教學圖卡標準生成管線。嚴格遵循「分階段確認制」，依序執行：
  1. 筆記草稿 (Markdown in notes/) 審查與核心/補充區分流
  2. 達文西手稿風格單頁 HTML 圖卡 (html/) 結構化排版與 KaTeX 渲染
  3. 生動視覺 PNG 圖卡 (png/) 高解析度轉檔輸出
  4. GitHub 首頁圖卡展示與一鍵同步管理
---

# 教學圖卡標準生成管線 (Infographic Pipeline)

本 Skill 定義本專案專屬的工作流程標準，所有參與的 Agent 請嚴格按照以下階段推進。

---

## 執行流程守則 (Phased Protocol)

### 階段一：筆記草稿撰寫與審查 (`notes/`)
- 知識點濃縮，嚴格劃分【核心圖卡區】與【延伸補充區】。
- 檢驗 LaTeX 公式在 KaTeX 下的語法相容性（行內 `$ ... $`、獨立塊 `$$ ... $$`）。
- **必須停下由使用者確認內容無誤**。

### 階段二：單頁 HTML 圖卡排版 (`html/`)
- 嚴格維持 A4 直式比例（寬度固定 `794px`，高度受限 `1123px`，絕不溢出單頁）。
- 嚴格落實 [`STYLE_GUIDE.md`](STYLE_GUIDE.md) 之**【達文西手繪手稿風】**：
  - 羊皮紙基底 (`#FAF5EB`) + 核桃深褐墨水 (`#23180F`) + 朱砂火漆印章 (`#9E2A2B`)。
  - 手繪雙線邊框、四角花飾、古典素描交叉排線 (Cross-Hatching)。
  - 角色形象：微型發條機關主體（含感知半徑錐度 $\mathcal{N}_i$ 與指向向量 $\vec{v}_i$）。
- **必須停下由使用者確認網頁版面與視覺階層**。

### 階段三：高解析度 PNG 圖卡輸出 (`png/`)
- 執行自動化無頭截圖腳本：
  ```bash
  python scripts/generate_png.py html/<target>.html png/<target>.png
  ```
- 採用 Playwright Chromium 引擎，設定 `device_scale_factor: 2`（輸出 2× Retina 高清大圖）。
- 自動等待 `.katex` 數學式與 Google Fonts 平滑渲染完成。
- **由使用者檢視圖檔品質**。

### 階段四：版本控管與展示 (`git / GitHub Desktop`)
- 確保 `README.md` 置頂展示最新的高解析度圖卡圖片。
- 根目錄 `index.html` 連結至最新圖卡，確保 GitHub Pages 一開啟即為全頁圖卡。
- 指引使用者透過 GitHub Desktop 或雙擊 `upload.bat` 執行同步。
