# AGENTS.md - 達文西手繪手札視覺系統與創作管線規範 (Universal Codex System)

本檔案定義本專案的架構規範、美學規則、角色插畫體系與 AI Agent 協作執行流程。
**未來無論是生成「教學圖卡 (Infographics)」、「學術海報 (Academic Posters)」、「主題插畫 (Artistic Illustrations)」或「知識手記 (Study Notes)」**，所有參與協作的 Agent 必須嚴格遵照以下色調、筆觸、角色、排版與擴充指南。

---

## 1. 核心美學規則庫 (Master Style System)

本專案拒絕千篇一律的現代向量電腦風格，立足於**「達文西文藝復興學者手稿 (Da Vinci Codex)」**，由四大核心維度構成：

### ① 色調體系 (Ancient Color Palette)
* **焦邊羊皮紙底色 (`--parchment-base: #F0E4CB`)**：
  - 疊加中心微亮（`#FFFDF5`）、四周天然焦褐暈染暗角（`inset 0 0 110px rgba(55, 30, 10, 0.55)`）。
  - 雙向網狀造紙纖維紋理（`0deg` 與 `90deg` 疊加）。
  - 疊加半透明琥珀色（Amber, `#B8860B`）與深墨褐色（Sepia, `#4A2F13`）多層次不規則水彩漬洗（`parchment-wash-layer`）。
* **核桃深褐主墨水 (`--ink-primary: #1E1309`)**：鋼筆原墨，用於標題、核心公式、主要骨架與外框。
* **手寫次級墨水 (`--ink-secondary: #362415` / `--ink-muted: #5C4531`)**：用於內文說明、註記解說與次要數據。
* **朱砂火漆赤紅 (`--seal-red: #8F2223`)**：火漆印章 (Wax Seal)、章節序號、重點強調、草稿刪劃補正筆跡。
* **普魯士工程藍 (`--prussian-blue: #15325B`)**：拓撲網絡、微觀動態箭頭、幾何輔助引線、比較維度次色。
* **古典黃銅金 (`--antique-gold: #8A6310`)**：幾何量測刻度尺（`Scala Geometria`）、天文星盤刻線、裝飾印記。

### ② 筆觸與紋理規範 (Brushwork & Hand-Drawn Textures)
* **手繪有機顫筆外框 (Jittered Borders)**：
  - 嚴格禁止生硬直角邊線，所有卡片容器統一採用手繪顫筆不規則圓角（`border-radius: 255px 15px 225px 15px/15px 225px 15px 255px`）。
  - 雙層外框：外層 `2px solid #322114`，內層 `1px dashed rgba(50, 33, 20, 0.5)`，配備 `14px × 14px` 朱砂四角花飾。
* **古典素描交叉排線 (Cross-Hatching)**：
  - 陰影與立體感**嚴禁使用現代模糊半透明陰影 (`blur filter`)**，一律採用 $45^\circ$ 細斜線交叉排線。
* **真實手札草記特徵 (Manuscript Artifacts)**：
  - **草稿刪劃修正筆跡 (`manuscript-scratch`)**：在思想演進處保留朱砂紅一字刪劃與上方補正草寫。
  - **手繪註解引線 (Callout Pointers)**：虛線引線指向機械部位或核心元件。
  - **幾何量測弧尺與羅盤刻度 (Compass Scales & Crosshairs)**：邊界點綴工程十字對齊線與角度分度規。

### ③ 角色形象與主題插畫體系 (Personas & Thematic Vignettes)
本系統將抽象演算法或概念具象化為古典機關物：
* **構成要素**：一律由「齒輪、木質連桿、滑輪、透鏡、天平、發條、羽翼、羊皮卷軸」等文藝復興物理構件組成。
* **主題對應清單 (Universal Thematic Mapping)**：
  - **代理人模型 / 群體智慧**：發條機械飛鳥 (Ornithopter)、同心齒輪感知錐、聚落漩渦。
  - **類神經網絡 / 深度學習**：神經突觸樹脈 (Synaptic Tree)、齒輪權重傳動層。
  - **強化學習 / 決策科學**：阿基米德螺旋天平 (Balance of Reward)、迷宮探索發條軸。
  - **遺傳演算法 / 演化計算**：雙螺旋生命卷軸 (Helix Parchment)、突變星芒刻印。
  - **搜尋與圖論**：古天文星盤 (Astrolabe)、樹狀分支幾何剪枝線。
  - **大語言模型 / Transformer**：多稜鏡聚光儀 (Prism of Attention)、雙向索引卷軸。
* **技術實現**：所有插圖一律使用內嵌輕量向量 SVG 本地繪製，保證高解析度放大不失真。

### ④ 100% 全手寫字型排印 (Typography System)
* **中文全域字型**：`JasonHandwriting5`（清松手寫體第五代·大五體，本地 TTF `assets/fonts/JasonHandwriting5.ttf` 載入），筆畫飽滿有力、手寫辨識度極高。
* **英文、數字與簽名**：`Caveat`（Google Fonts, 600/700），具備文藝復興學者流暢鋼筆草寫風。
* **數學公式**：KaTeX 引擎渲染，融入深褐墨水色。

### ⑤ 標題與題頭禁語規則 (Strict Title Conventions)
* 🚫 **嚴格禁止出現任何「達文西手繪手札卷X」、「手稿考卷」等說明文字**。
  - 頂部左側題頭：僅保留乾淨純粹的拉丁名（如 `Tractatus de Nexu Nervorum`）。
  - 主標題副標：僅標記中文主題名稱本體（如 `【類神經網絡與反向傳播】`），絕不贅加後綴。

### ⑥ 頁尾動態題註規範 (Dynamic Thematic Footers)
頁尾文字嚴禁死板固定，必須隨主題領域與卷號動態演進，結構為三欄古典式：
* **左欄（論著名稱與代碼）**：`Tractatus [卷號]: De [主題拉丁名] · [領域代碼-序號]`
  - 例：`Tractatus I: De Systematibus Agentium · ABM-01`
  - 例：`Tractatus II: De Ratione Discendi · RL-02`
* **中欄（手寫草簽名）**：主題核心思想家或哲學隱喻的流暢鋼筆草寫（`Caveat` 字體）：
  - ABM：`Complexitas Emergente scripsit` (複雜湧現者書)
  - RL：`Bellman & Machina scripsit` (貝爾曼與發條機關書)
* **右欄（紀年與規格）**：`Anno Domini 2026 · Typographia A4`

---

## 2. 跨類型作品生成指南 (Posters, Illustrations & Cards)

本風格不限於單頁 A4 圖卡，更可廣泛擴充至各類視覺作品：

| 作品類型 (Artifact Type) | 建議尺寸與容器 | 版面結構特徵 | 關鍵設計要素 |
| :--- | :--- | :--- | :--- |
| **教學圖卡 (Infographics)** | A4 直式 (`794 × 1123 px`) | 四幕敘事：題頭 ➔ 雙欄原理 ➔ 跨欄大解剖圖 ➔ 比較矩陣 ➔ 案例三聯畫 | 密集資訊量、公式卷軸、三元組 |
| **學術海報 (Academic Posters)** | A1 / A2 / 寬版海報 (`1200 × 1600 px` 或自訂) | 三欄式宏大排版：頂部橫幅 ➔ 左側背景與方法 ➔ 中央巨型解剖圖 ➔ 右側實驗與結論 | 巨型齒輪動力解析圖、羊皮紙多聯裝裱外框 |
| **獨立主題插畫 (Art Illustrations)** | 1:1 方形或黃金比例橫幅 | 單一焦點構圖：主體大型古典透視手稿（如大型多頭注意力透鏡機） | 豐富交叉排線陰影、草稿邊緣推導公式、比例尺 |
| **章節摘要小卡 (Flashcards)** | 明信片規格 (`800 × 500 px`) | 雙面或卡片式：正面概念圖解，背面三條金句與推導 | 粗邊手繪顫筆框、大字火漆章、短引言 |

---

## 3. 核心原則：分階段確認制 (Strict Phased Workflow)

> ⚠️ **重要原則**：
> 嚴格**禁止一條龍自動執行全部產出**。每個階段產出後，必須停下來讓使用者檢閱、提供修改建議，**獲得使用者明確確認後**，方可進入下一階段。

```
[階段 1: 筆記草稿] ➔ (使用者確認) ➔ [階段 2: HTML 排版] ➔ (使用者確認) ➔ [階段 3: 高清 PNG] ➔ [階段 4: Git 同步]
```

1. **階段 1：筆記草稿 (`notes/*.md`)**
   - 梳理主題知識點，嚴格劃分：
     - **【核心圖卡區】**：專為單頁 A4 設計，容量適度，包含：核心定義、三大支柱/要素、LaTeX 數學模型（微觀轉移與宏觀湧現）、典範比較表、經典案例。
     - **【延伸補充區】**：收納深入推導、模型代碼、次要背景，避免單頁圖卡擁擠。
   - **檢核點 (Checkpoint)**：呈交使用者審核，確認觀念、用詞、公式與剪裁適當。

2. **階段 2：單頁 HTML 實作 (`html/*.html`)**
   - **標準範本派生**：基於 `html/_template_davinci.html` 進行填寫，繼承完整的 CSS 質地、手繪邊框與字體。
   - 嚴格落實本指南之色調、筆觸、字型與主題插畫規範。
   - **檢核點 (Checkpoint)**：提供本機預覽連結，由使用者確認版面配置與樣式。

3. **階段 3：生動視覺 PNG 輸出 (`png/*.png`)**
   - 透過 Python 腳本 (`scripts/generate_png.py`) 驅動 Playwright Chromium 進行高解析度無頭截圖。
   - 參數設定：`viewport: {width: 794, height: 1123}`，`device_scale_factor: 2`（輸出 `1588 × 2246` 像素）。
   - 自動等待 `.katex` 數學式與字型平滑化完成。
   - **檢核點 (Checkpoint)**：由使用者確認圖檔解析度與視覺效果。

4. **階段 4：GitHub 同步與首頁展示**
   - 確保 `README.md` 置頂展示最新圖卡大圖。
   - 根目錄 `index.html` 提供全頁式線上圖卡檢視器（支援 GitHub Pages）。
   - 支援透過 GitHub Desktop 或雙擊 `upload.bat` 執行一鍵同步。

---

## 4. 目錄結構約定 (Directory Conventions)

專案路徑：`C:\Users\User\Desktop\Antigravity_Project\graphics\`

```text
graphics/
├── assets/                  # 專案靜態資源
│   └── fonts/               # 🌟 本地手寫字型庫 (JasonHandwriting5.ttf, 9, 1, 3 等)
├── notes/                   # 階段 1：主題筆記草稿 (Markdown, 含核心區與補充區)
├── html/                    # 階段 2：HTML 圖卡 / 海報 / 插畫原始檔
│   ├── _template_davinci.html # 🌟 達文西萬用標準母範本 (所有作品皆以此派生)
│   ├── 01_agent_based_model_davinci.html # 達文西手繪手稿圖卡第一號 (ABM)
│   └── index.html           # 原型風格選樣入口
├── png/                     # 階段 3：轉出的高解析度 Retina PNG 圖卡
│   └── 01_agent_based_model.png
├── scripts/                 # 自動化截圖與轉檔輔助腳本
│   └── generate_png.py      # Playwright 高解析度自動截圖工具
├── .agent/skills/           # Antigravity 專案自定義 Skill
│   └── infographic-pipeline/ # 專案工作流標準指令集
├── index.html               # 🌟 GitHub Pages 根目錄展示入口 (全頁圖卡檢視器)
├── export_png.bat           # 🌟 雙擊一鍵重新產生高解析度 PNG
├── upload.bat               # 🌟 雙擊一鍵推送到 GitHub
├── STYLE_GUIDE.md           # 🌟 視覺設計系統完整規範指南
├── README.md                # 專案首頁 (置頂展示圖卡大圖)
└── AGENTS.md                # 🌟 本專案核心指示 (Agent Master Instructions)
```

---

## 5. Agent 技術與環境約定 (Technical Standards)

* **繁體中文 (zh-TW)**：全部筆記、HTML 標註與文件一律採用正體中文。
* **字體優先順序**：`'Caveat', 'JasonHandwriting5', cursive`（離線本地載入優先，零外部依賴）。
* **數學公式**：一律相容 KaTeX 語法（行內 `$ ... $`，區塊 `$$ ... $$`）。
* **執行環境**：
  - Python 環境：`C:\Users\User\Desktop\AI_Knowledge_Workspace\.venv\Scripts\python.exe`
  - Git 程式：`C:\Users\User\AppData\Local\GitHubDesktop\app-3.7.0\resources\app\git\cmd\git.exe`
  - Playwright：`device_scale_factor: 2`（Retina 2x 解析度保證）
