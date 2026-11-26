# AGENTS.md - 單頁教學圖卡生成專案規範

本檔案定義本專案的架構規範、設計原則與 AI Agent 協作執行流程。所有在此專案中協助的 Agent 必須嚴格遵守以下準則。

---

## 1. 專案核心目標 (Project Goal)
將知識主題、研究課題或作業內容，提煉轉化為**統一頂級質感、單頁 A4 直式**的教學圖卡系統：
* **結構嚴謹**：區分「核心單頁圖卡區」與「延伸補充內容區」，支援高品質 LaTeX 數學公式排版。
* **獨特美學**：依循 [`STYLE_GUIDE.md`](STYLE_GUIDE.md) 之**【達文西手繪手稿風】**，落實色調、筆觸、角色與構圖四大設計規範。
* **高畫質輸出**：產出適合直接列印、螢幕展示與作業繳交的 2× Retina 級 A4 PNG 圖卡。
* **版本控管與展示**：整合 Git / GitHub Desktop，並於首頁直接秀出成品，便於展示與一鍵同步。

---

## 2. 核心原則：分階段確認制 (Strict Phased Workflow)

> ⚠️ **重要原則**：
> 嚴格**禁止一條龍自動執行全部產出**。每個階段產出後，必須停下來讓使用者檢閱、提供修改建議，**獲得使用者明確確認後**，方可進入下一階段。

### 階段流程定義：

```
[階段 1: 筆記草稿] ➔ (使用者審查確認) ➔ [階段 2: HTML 圖卡] ➔ (使用者審查確認) ➔ [階段 3: 生動 PNG] ➔ [階段 4: GitHub 同步]
```

1. **階段 1：筆記草稿 (`notes/*.md`)**
   - 梳理主題知識點，嚴格劃分：
     - **【核心圖卡區】**：專為單頁 A4 設計，容量適度，包含：核心定義、三大支柱/要素、LaTeX 數學模型（微觀轉移與宏觀湧現）、典範比較表、經典案例。
     - **【延伸補充區】**：收納深入推導、模型代碼、次要背景，避免單頁圖卡擁擠。
   - **檢核點 (Checkpoint)**：呈交使用者審核，確認觀念、用詞、公式與剪裁適當。

2. **階段 2：單頁 HTML 圖卡 (`html/*.html`)**
   - 採用標準 A4 直式比例（寬高比 1 : 1.414，容器尺寸 `794px × 1123px`）。
   - 內建 **KaTeX** CDN 自動渲染數學式。
   - 嚴格落實 [`STYLE_GUIDE.md`](STYLE_GUIDE.md) 之達文西手繪手稿風（羊皮紙底、鋼筆墨水色、火漆印章、微型發條機關主體）。
   - **檢核點 (Checkpoint)**：提供本機預覽連結，由使用者確認版面配置與樣式。

3. **階段 3：生動視覺 PNG 圖卡 (`png/*.png`)**
   - 透過 Python 腳本 (`scripts/generate_png.py`) 驅動 Playwright Chromium 進行高解析度無頭截圖。
   - 參數設定：`viewport: {width: 794, height: 1123}`，`device_scale_factor: 2`（輸出 `1588 × 2246` 像素）。
   - 自動等待 `.katex` 數學式與字型平滑化完成。
   - **檢核點 (Checkpoint)**：由使用者確認圖檔解析度與視覺效果。

4. **階段 4：GitHub 同步與首頁展示**
   - 確保 `README.md` 置頂展示最新圖卡大圖。
   - 根目錄 `index.html` 提供全頁式線上圖卡檢視器（支援 GitHub Pages）。
   - 支援透過 GitHub Desktop 或雙擊 `upload.bat` 執行一鍵同步。

---

## 3. 目錄結構約定 (Directory Conventions)

專案路徑：`C:\Users\User\Desktop\Antigravity_Project\graphics\`

```text
graphics/
├── notes/                   # 階段 1：主題筆記草稿 (Markdown, 含核心區與補充區)
│   └── 01_agent_based_model.md
├── html/                    # 階段 2：單頁 A4 教學圖卡 (HTML + CSS + JS + KaTeX)
│   ├── 01_agent_based_model_davinci.html # 🌟 標準風格 A 達文西手繪手稿圖卡
│   ├── 01_agent_based_model_vivid.html   # 現代科技儀表板生動版 (備選)
│   └── index.html           # 原型風格選樣總覽入口
├── png/                     # 階段 3：轉出的高解析度 A4 PNG 圖卡
│   └── 01_agent_based_model.png
├── scripts/                 # 自動化截圖與輔助腳本
│   └── generate_png.py      # Playwright 高解析度自動截圖工具
├── .agent/                  # Antigravity 專案自定義配置
│   └── skills/              # 專案專用 Skill
│       └── infographic-pipeline/ # 圖卡全流程標準 Skill
├── index.html               # 🌟 GitHub Pages 根目錄展示入口 (全頁圖卡檢視器)
├── export_png.bat           # 🌟 雙擊一鍵重新產生高解析度 PNG
├── upload.bat               # 🌟 雙擊一鍵推送到 GitHub
├── STYLE_GUIDE.md           # 🌟 視覺設計系統指南 (色調/筆觸/角色/構圖)
├── README.md                # 專案首頁 (置頂展示圖卡大圖)
├── .gitignore               # 排除快取、暫存檔與虛擬環境
└── AGENTS.md                # 本規範文件
```

---

## 4. Agent 技術與環境約定 (Technical Standards)

* **語系與字體**：一律採用繁體中文（zh-TW）。英文字體使用 `Cinzel` 與 `Caveat`，繁體中文字體使用 Google Fonts 之 `Noto Serif TC`。
* **數學公式**：
  * 行內公式：`$E = mc^2$`
  * 獨立塊公式：`$$s_i(t+1) = f(s_i(t), \mathcal{N}_i(t), E(t))$$`
  * 必須確保 KaTeX delimiters 配置支援 `$` 與 `$$`。
* **A4 直式尺寸約束**：
  * 寬度固定 `794px`，最小高度 `1123px`，嚴防文字過多溢出單頁。
* **執行環境**：
  * Python 環境：`C:\Users\User\Desktop\AI_Knowledge_Workspace\.venv\Scripts\python.exe`
  * Git 程式：`C:\Users\User\AppData\Local\GitHubDesktop\app-3.6.11\resources\app\git\cmd\git.exe`
