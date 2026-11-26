---
name: infographic-pipeline
description: >-
  專案專用：單頁 A4 達文西手繪手稿風教學圖卡、海報與插畫之標準端到端生成管線。嚴格遵循「分階段確認制」，覆蓋：
  1. 筆記草稿 (Markdown in notes/) 知識濃縮與核心/補充區分流
  2. 達文西手稿風格 HTML 圖卡 (html/) 基於母範本 _template_davinci.html 排版、清松手寫體本地嵌入與 KaTeX 渲染
  3. Playwright 2× Retina 高解析度 PNG 圖卡 (png/) 截圖轉檔
  4. 根目錄 index.html 互動切換器、README.md 畫廊展示與 GitHub Desktop 同步
---

# 達文西手繪手札圖卡生成專用 Skill (Infographic Pipeline Skill)

本 Skill 是本專案專屬的工作流大腦與作業標準手冊。所有在此專案中協助的 AI Agent 必須自動載入並嚴格遵循以下四階段推進流程與設計準則。

---

## 核心設計理念與風格守則 (Master Style Standard)

本專案拒絕千篇一律的現代科技儀表板或死板向量排版，立足於**「達文西文藝復興學者手札 (Da Vinci Codex)」**，由四大維度構成：

1. **色調質地 (Ancient Color & Washes)**：
   - 焦邊羊皮紙底（`#F0E4CB`）、四周焦褐暈染暗角（`inset 0 0 110px rgba(55, 30, 10, 0.55)`）、雙向十字造紙纖維紋理。
   - 疊加半透明琥珀（Amber, `#B8860B`）與深墨褐色（Sepia, `#4A2F13`）多層次水彩漬洗層（`parchment-wash-layer`）。
   - 核桃深褐主墨水（`#1E1309`）、朱砂火漆赤紅（`#8F2223`）、普魯士藍（`#15325B`）、古典黃銅金（`#8A6310`）。
2. **手繪線條與草記筆觸 (Hand-Drawn Brushwork)**：
   - 嚴格禁止生硬直角直線，所有卡片容器採用**手繪有機顫筆不規則圓角**（`border-radius: 255px 15px 225px 15px/15px 225px 15px 255px`）。
   - 章節標題下劃線採用**落筆濃、收筆淡、兩端自然收窄**的漸層毛邊墨線。
   - 陰影與立體感**嚴禁使用現代模糊半透明陰影 (`blur filter`)**，一律採用 $45^\circ$ 古典素描交叉排線 (Cross-Hatching)。
   - **真實手札痕跡**：保留朱砂紅一字刪劃草稿補正筆跡（`manuscript-scratch`）、虛線註解引線 (Callouts)、幾何量測弧尺（`[Scala Geometria]`）。
3. **主題角色與插圖體系 (Thematic Vignettes & Figures)**：
   - 將抽象演算法轉化為古典文藝復興物理機關（齒輪、木質連桿、天平、透鏡、發條、羽翼、卷軸）。
   - 一律使用內嵌輕量向量 SVG 本地繪製，零外部圖片依賴，高解析度不失真。
4. **100% 全手寫字型排印 (Typography)**：
   - 中文全域強制採用本地 TTF **清松手寫體第五代（大五體, `assets/fonts/JasonHandwriting5.ttf`）**，厚實飽滿、筆跡感極強。
   - 英文與簽名採用 **Caveat**，數學公式採用深褐墨水 KaTeX。
5. **主題專屬動態頁尾 (Dynamic Thematic Footers)**：
   - 結構：`Tractatus [卷號]: De [主題拉丁名] · [領域代碼-序號]` ── `[草寫簽名] scripsit` ── `Anno Domini 2026 · Typographia A4`。

---

## 標準執行四階段守則 (Strict Phased Protocol)

> ⚠️ **紀律要求**：
> 嚴格**禁止一條龍自動執行全部產出**。每個階段完成後，必須停下向使用者報告並展示成果，**獲得使用者明確確認後**，方可前進至下一階段。

### 【階段一】：主題筆記撰寫與知識分流 (`notes/`)
1. 深入梳理該知識主題，撰寫 `notes/{xx_topic_name}.md`。
2. 嚴格劃分兩大區塊：
   - **【核心圖卡區】**：專為單頁 A4 設計，容量適度，包含：題頭與古典隱喻、五大核心骨架、核心數學公式（KaTeX 語法）、中央手繪解剖大圖規劃、典範比較表、歷代三大經典里程碑。
   - **【延伸補充區】**：收納深入推導、模型代碼、次要背景，避免單頁圖卡擁擠。
3. **檢核點 (Checkpoint 1)**：停下呈交使用者審核，確認觀念、用詞、公式與剪裁適當。

### 【階段二】：單頁 HTML 圖卡實作 (`html/`)
1. **基於母範本派生**：複製 `html/_template_davinci.html` 為 `html/{xx_topic_name}_davinci.html`。
2. **遵守 A4 直式尺寸約束**：寬度固定 `794px`，高度受限 `1123px`，絕不溢出單頁。
3. **注入核心內容與專屬 SVG 插圖**：
   - 替換題頭、火漆印章、四幕敘事內容、KaTeX 數學卷軸、比較表格。
   - 依據「主題角色對應設計庫」繪製專屬的輕量向量 SVG（如發條飛鳥、阿基米德天平、神經樹脈、雙螺旋等）。
   - 設定專屬的動態頁尾論著代碼與草寫簽名。
4. **檢核點 (Checkpoint 2)**：提供本機預覽連結，由使用者確認版面配置、文字呼吸感與樣式。

### 【階段三】：高解析度 PNG 渲染輸出 (`png/`)
1. 使用 Playwright Chromium 引擎執行轉檔腳本：
   ```powershell
   & "C:\Users\User\Desktop\AI_Knowledge_Workspace\.venv\Scripts\python.exe" "scripts\generate_png.py" "html/{xx_topic_name}_davinci.html" "png/{xx_topic_name}.png"
   ```
2. 參數鎖定：`viewport: {width: 794, height: 1123}`，`device_scale_factor: 2`（輸出為 `1588 × 2246` 像素之 2× Retina 高清大圖）。
3. 腳本會自動等待 `.katex` 數學式與本地字型平滑化完成。
4. **檢核點 (Checkpoint 3)**：由使用者檢視圖檔品質。

### 【階段四】：展示集成與 GitHub 同步
1. **更新首頁切換器**：在 `index.html` 中新增對應的新頁籤按鈕與 `CARDS` 資料映射，讓線上訪客能一鍵切換。
2. **更新專案首頁**：在 `README.md` 的「圖卡典藏畫廊」置頂新增此圖卡之高解析預覽圖與下載連結。
3. **版本控管與推送**：
   - 使用 Git 暫存並提交所有變更。
   - 指引使用者於 GitHub Desktop 點擊 **Push origin**（或雙擊 `upload.bat`）推送到 GitHub 與 GitHub Pages。
