# 主題筆記：Agent-Based Model (ABM, 基於主體的模型)

> **說明**：
> 本筆記為圖卡製作的草稿。分為 **【核心圖卡區】**（預計濃縮收納進 A4 單頁教學圖卡）與 **【延伸補充區】**（供作業深入閱讀與查閱，不擠入圖卡本體）。
> 請您審視內容的深度、名詞翻譯、以及是否有需要刪改或移至補充區的部分。

---

## 📌 第一部分：【核心圖卡區】（A4 單頁直式規劃）

### 1. 什麼是 Agent-Based Model (ABM)？
* **核心理念**：「由下而上 (Bottom-up)」的計算模擬典範。
* **一句話精髓**：不直接對宏觀現象立方程式，而是模擬一群**具有自主決策能力的個體（Agents）**在特定環境中依循簡單規則互相互動，進而**自然「湧現 (Emergence)」**出宏觀層面的複雜群體行為。

---

### 2. ABM 的三大核心支柱 (The Core Triad)

| 支柱要素 | 特性與角色 | 關鍵概念 |
| :--- | :--- | :--- |
| **1. 主體 (Agents)** | 系統的基本單元（人、細胞、車輛、公司） | **自主性 (Autonomous)**、**異質性 (Heterogeneous)**、**有限理性 (Bounded Rationality)** |
| **2. 環境 (Environment)** | 主體生存與互動的空間背景 | 格網空間 (Grid/Cellular)、複雜網絡 (Network)、連續物理空間 (Continuous 2D/3D) |
| **3. 互動與規則 (Rules & Interactions)** | 驅動系統演化的因果邏輯 | 局部感知 (Local Sensing)、條件反應、學習與適應 (Adaptation) |

---

### 3. 微觀到宏觀的數學表達 (Micro-to-Macro Emergence)

* **微觀狀態演化 (Micro Dynamics)**：
  每個個體 $i$ 在時間 $t+1$ 的狀態 $s_i$，取決於當前自身狀態 $s_i(t)$、鄰近個體狀態集 $\mathcal{N}_i(t)$ 與環境變數 $E(t)$：
  $$s_i(t+1) = f\Big(s_i(t), \; \mathcal{N}_i(t), \; E(t)\Big)$$

* **宏觀現象湧現 (Macro Observable)**：
  整個系統的總體指標 $M(t)$（如群體秩序、市場價格、疾病感染率）是由所有微觀個體的非線性聚合產生，通常無法由單一個體直接推導：
  $$M(t) = \mathcal{G}\Big(\{s_1(t), s_2(t), \dots, s_N(t)\}\Big) \approx \frac{1}{N}\sum_{i=1}^N g(s_i(t))$$

---

### 4. ABM vs 傳統方程式模型 (Top-Down vs Bottom-Up)

| 維度 | 傳統頂層模型 (如微分方程 ODE/PDE) | 代理人模型 (ABM) |
| :--- | :--- | :--- |
| **建模視角** | 由上而下 (宏觀總體聚集) | 由下而上 (微觀個體互動) |
| **個體假設** | 假設均質 (Homogeneous, 代表性個體) | 允許完全異質 (年齡、偏好、資源各異) |
| **互動拓撲** | 通常假設完全混合 (Well-mixed) | 基於真實空間與社交網絡結構 (Networks) |
| **動態特徵** | 線性/連續平滑趨勢 | 非線性、突變臨界點 (Tipping Points)、路徑依賴 |

---

### 5. 三大經典範例 (Classic Milestones)

1. **謝林隔離模型 (Schelling's Segregation Model)**：
   * 微觀：每個人只希望鄰居有 $\ge 30\%$ 與自己相同（微小偏好）。
   * 宏觀：最終城市演化成極度嚴重的全面種族隔離（個人良善微觀意圖 $\neq$ 宏觀善果）。
2. **鳥群湧現模型 (Craig Reynolds' Boids)**：
   * 僅靠三條局部規則：**避碰 (Separation)**、**對齊 (Alignment)**、**聚合 (Cohesion)**。
   * 湧現出壯麗如一體般的自然群飛軌跡。
3. **流行病傳播 (SIR on Complex Networks)**：
   * 模擬接觸網絡、超級傳播者與區域流動對疫情擴散的真實影響。

---

## 📚 第二部分：【延伸補充區】（不納入單頁圖卡，作為作業深讀或備審資料）

### 補充 A：謝林隔離模型的決策規則推導
個體 $i$ 位於網格座標 $(x,y)$，其鄰域 $\mathcal{N}_i$ 大小為 $k$（例如 Moore 鄰域 $k=8$）。
定義滿意度指示函數：
$$H_i(t) = \frac{\sum_{j \in \mathcal{N}_i} \mathbb{I}(\text{Type}_j = \text{Type}_i)}{|\mathcal{N}_i|}$$
決策規則：
$$\text{Move}(i, t) = \begin{cases} 
\text{保持原位}, & \text{若 } H_i(t) \ge \theta \\
\text{隨機遷移至空位}, & \text{若 } H_i(t) < \theta 
\end{cases}$$
其中 $\theta$ 為容忍門檻（通常設為 $0.3 \sim 0.5$）。數值實驗顯示，即使 $\theta = 0.33$（即能容忍三分之二鄰居為相異族群），系統最終的平均同質比率往往高達 $75\% \sim 80\%$。

### 補充 B：主流開發框架與工具
* **Python Mesa**：目前 Python 生態系最熱門的 ABM 模組，模組化支援空間網格、代理人排程與視覺化儀表板。
* **NetLogo**：最經典且直觀的教學與研究環境，具備豐富的模型庫 (Models Library) 與極低入門門檻。
* **AnyLogic**：商業級多方法模擬軟體，能無縫整合 ABM、離散事件 (Discrete Event) 與系統動力學 (System Dynamics)。

### 補充 C：ABM 的挑戰與局限
1. **維度災難與算力消耗**：個體數量 $N \ge 10^6$ 時，空間搜尋與全網遍歷需要分散式平行運算。
2. **參數校準 (Calibration) 困難**：微觀參數過多容易導致「過擬合 (Overfitting)」，驗證真實因果機制的難度較高。
