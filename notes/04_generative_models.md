# 主題筆記 04：生成對抗網絡與擴散模型 (Generative Models: GAN & Diffusion)

本筆記專為【橫式 16:9 專欄橫幅圖卡 (Landscape 16:9 Article Banner)】設計。

---

# 【專欄橫幅精華區】（16:9 橫向流動畫布，尺寸 1280 × 720 px / 輸出 2K 1920 × 1080 px）

## 一、 題頭與古典隱喻 (Inscriptio & Metaphor)
* **純粹拉丁題頭**：*Tractatus de Arte Generativa*
* **副標題**：【生成對抗網絡與擴散模型】
* **古典箴言**：
  > *"Ex nihilo forma oritur; per aemulationem et dispersionis retrogressum, veritas ficta coalescit."*  
  > 虛無之中萬象自生；假鑑寶之競鋒與塵埃之逆流，虛像終與真跡同輝。

---

## 二、 雙雄並立之生成哲思架構 (橫向三欄宏觀流動)

### 1. 左翼：生成對抗網絡 GAN (The Duelling Artificers)
* **核心隱喻**：文藝復興天才造假畫師 (Generator $G$) vs 嚴苛鑑寶審查官 (Discriminator $D$)。
* **博弈動態**：極小極大零和博弈 (Minimax Game)：
  $$\min_G \max_D V(D, G) = \mathbb{E}_{x \sim p_{data}}[\log D(x)] + \mathbb{E}_{z \sim p_z}[\log (1 - D(G(z)))]$$
* **終局平衡**：抵達納許均衡 (Nash Equilibrium) 時，$D(x) = \frac{1}{2}$，鑑寶官再難辨真偽。

### 2. 中央：中央互動天平與相變樞紐 (The Fulcrum of Generation)
* 古典雙向平衡羅盤天平，連結左翼「對抗博弈」與右翼「熱力學逆向去噪」。
* 象徵現代生成式 AI 從「博弈擬真」邁向「熱力學能量流動」之思想躍遷。

### 3. 右翼：分數階擴散模型 Diffusion (The Thermodynamic Erasure & Reconstruction)
* **核心隱喻**：墨水入水之布朗熱力彌散 (Forward Noise) ➔ 逆轉時間之時空倒流去噪 (Reverse Denoising)。
* **前向加噪**：馬可夫鏈漫長擴散 $q(x_t \mid x_{t-1}) = \mathcal{N}(x_t; \sqrt{1 - \beta_t} x_{t-1}, \beta_t \mathbf{I})$。
* **逆向去噪**：神經網絡估算得分函數 (Score Matching) 逆轉歲月侵蝕：
  $$x_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{1 - \alpha_t}{\sqrt{1 - \bar{\alpha}_t}} \boldsymbol{\epsilon}_\theta(x_t, t) \right) + \sigma_t \mathbf{z}$$

---

## 三、 底部三聯專欄金句與動態題註
* **專欄金句 1**：**博弈演化** —— GAN 以對抗碰撞出潛在空間 (Latent Space) 的幾何流形。
* **專欄金句 2**：**熵增倒流** —— 擴散模型借鑑非平衡熱力學，以高維微積分逆轉時間之箭。
* **專欄金句 3**：**從無生有** —— 隨機高斯噪點化為栩栩如生之巨作，達成文藝復興造物之夢。
* **動態頁尾**：`Tractatus IV: De Arte Generativa · GAN-DIFF-04` ── `Daedalus & Machina scripsit` ── `Anno Domini 2026 · Typographia 16:9`
