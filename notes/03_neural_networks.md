# 主題筆記 03：類神經網絡與反向傳播 (Neural Networks & Backpropagation)

本筆記依據專案規範，嚴格劃分為【核心圖卡區】與【延伸補充區】。

---

# 【核心圖卡區】（單頁 A4 圖卡專屬精練內容）

## 一、 題頭與古典隱喻 (Inscriptio & Metaphor)
* **拉丁題頭**：*Tractatus de Nexu Nervorum*
* **副標題**：【類神經網絡與反向傳播】
* **古典哲學箴言**：
  > *"Sicut arbor per ramos sucum transmittit, ita mens per nexus gradusque erroris veritatem contexit."*  
  > 猶如古樹由脈絡逆向汲取甘露，心智亦自層疊之結網與誤差之梯度中，逆向織就萬物之真理。

---

## 二、 系統核心骨架：神經突觸之四大支柱 (Quattuor Fundamenta)
類神經網絡以「多層感知機 (MLP)」為基礎，構建資訊前饋與梯度逆流之雙向織網：
1. **輸入與特徵感知層 $\mathbf{x} \in \mathbb{R}^d$ (Sensorium)**：
   外界刺激之信號源泉，如眼目之光感、琴鍵之聲震。
2. **權重突觸與偏置矩陣 $\mathbf{W}^{(l)}, \mathbf{b}^{(l)}$ (Synapses & Vectes)**：
   微型齒輪之傳動比率與阻尼閥門，決定信號在層間穿梭時之強弱縮放。
3. **非線性激活算子 $\sigma(z)$ (Ignitio / Activation)**：
   超越線性束縛之神經放電閾值（如 $\mathrm{ReLU}(z) = \max(0, z)$、$\sigma(z) = \frac{1}{1 + e^{-z}}$），賦予網絡擬合任意複雜曲面之神能。
4. **目標損失泛函 $\mathcal{L}(\hat{y}, y)$ (Damnum / Loss)**：
   衡量預測輸出與客觀真實之差距，如均方誤差 (MSE) 或交叉熵 (Cross-Entropy)，為系統反思校準之起點。

---

## 三、 核心數學卷軸：微積分鏈鎖律與梯度逆流 (Calculus Catenarius)
誤差信號自輸出端向輸入端層層逆傳，依微積分鏈鎖律精確撥動每一枚齒輪突觸：

$$\delta^{(l)} \equiv \frac{\partial \mathcal{L}}{\partial \mathbf{z}^{(l)}} = \left( (\mathbf{W}^{(l+1)})^T \delta^{(l+1)} \right) \odot \sigma'(\mathbf{z}^{(l)})$$

$$\frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}} = \delta^{(l)} (\mathbf{a}^{(l-1)})^T, \quad \mathbf{W}^{(l)} \leftarrow \mathbf{W}^{(l)} - \eta \frac{\partial \mathcal{L}}{\partial \mathbf{W}^{(l)}}$$

* **手札註解**：前向傳導織出推論之網，反向鏈鎖推演微調萬千突觸；步長 $\eta$ 猶如匠人微雕之巧勁。

---

## 四、 中央手繪解剖大圖：突觸樹脈與古織布梭機雙向流動 (Figura III)
* **(左) 微觀單元：人工神經元解剖 (Neuron Anatomy)**
  - 樹突信號匯聚盤 $\sum w_i x_i + b$，中心帶有放電激發閾值鉚釘，前方延伸出軸突末梢。
* **(中) 交互機關：古織布梭機多層傳動 (Loom of Synapses)**
  - 輸入層、隱藏層、輸出層透過深褐墨水虛線縱橫交錯，宛如文藝復興提花織布機之經緯線。
  - **前向推論（藍色光束 $\to$）**：信號前饋層層點亮神經節點。
  - **反向反饋（紅色逆流 $\leftarrow$）**：誤差梯度沿著同條突觸逆流而上，微調齒輪節奏。
* **(右) 宏觀演化：高維損失曲面與最速下降 (Loss Landscape)**
  - 丘陵起伏之高維地形圖，梯度向量自崎嶇峰巒循等高線自發滑入至善之鞍部低谷。

---

## 五、 典範之衡鑑：符號邏輯 AI vs 聯結主義神經網絡 (Paradigmata)

| 比較維度 | 符號主義邏輯推理 (Symbolic AI) | 聯結主義神經網絡 (Connectionist NN) |
| :--- | :--- | :--- |
| **知識表徵 (Representation)** | **顯式規則**：專家手工撰寫 If-Else 與一階邏輯。 | **隱式分佈**：數百萬連續權重矩陣之全域協同。 |
| **可解釋性 (Interpretability)** | **通透白箱**：每步因果推導皆有邏輯鏈可循。 |
| **泛化與抗噪 (Robustness)** | 脆弱僵化：遭遇微小語意干擾即崩潰。 | **湧現直覺**：具備強大容錯、模糊聯想與泛化遷移力。 |

*(註：在比較矩陣中保留朱砂紅一字刪劃筆跡：將「~~死板程式碼~~」補正為「**➔ 連續幾何映射**」)*

---

## 六、 歷代三大經典里程碑驗證 (Exempla Classica)
1. **Case 01 · 感知機 Perceptron (Rosenblatt, 1958)**
   - 誕生於康乃爾航太實驗室，單層線性閥門首次以機械機關實現圖像分類，開創機器學習先河。
2. **Case 02 · 反向傳播復興 (Rumelhart, Hinton & Williams, 1986)**
   - 突破 Minsky 異或 (XOR) 詛咒之寒冬，以微積分鏈鎖律徹底攻克多層網絡訓練難題。
3. **Case 03 · 深度卷積 AlexNet (Krizhevsky & Hinton, 2012)**
   - GPU 並行算力與 ReLU 激活之璀璨結合，在 ImageNet 競賽以壓倒性優勢引爆全球深度學習革命。

---

# 【延伸補充區】（進階研究與推導，不擠入單頁圖卡）

### 1. 萬能近似定理 (Universal Approximation Theorem, Hornik 1989)
* 只要包含至少一個隱藏層與具備非線性擠壓激活函數的神經網絡，就能以任意精度逼近緊緻集上的任何連續多維函數 $f: \mathbb{R}^n \to \mathbb{R}^m$。
* 這是神經網絡被譽為「通用數學逼近器」的理論基石。

### 2. 梯度消失 (Vanishing Gradient) 與 ReLU 之解法
* 傳統 Sigmoid 函數於 $|z| \gg 0$ 時導數趨近於 $0$（$\sigma'(z) \le 0.25$），經多層相乘後 $\prod_{l} \sigma'$ 指數衰減至零。
* ReLU 函數在正區間導數恆為 $1$（$\frac{\partial \max(0,z)}{\partial z} = 1$），徹底打通深度架構反向傳播之任督二脈。
