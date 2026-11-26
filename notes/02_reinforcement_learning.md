# 主題筆記 02：強化學習與馬可夫決策過程 (Reinforcement Learning & MDP)

本筆記依據專案規範，嚴格劃分為【核心圖卡區】與【延伸補充區】。

---

# 【核心圖卡區】（單頁 A4 圖卡專屬精練內容）

## 一、 題頭與古典隱喻 (Inscriptio & Metaphor)
* **拉丁題頭**：*Tractatus de Ratione Discendi · 達文西手繪手札卷二*
* **副標題**：【強化學習與馬可夫決策過程 · 達文西手繪手札】
* **古典哲學箴言**：
  > *"Experientia est optima rerum magistra; per praemia et poenas animus ad perfectionem ducitur."*  
  > 經驗乃世間萬物之良師；心智藉由賞罰之天平，自試誤中步向至善至境。

---

## 二、 系統核心骨架：MDP 五元組 (Tria et Duo Fundamenta)
馬可夫決策過程以古典五元組 $\mathcal{M} = \langle \mathcal{S}, \mathcal{A}, \mathcal{P}, \mathcal{R}, \gamma \rangle$ 構成封閉互動宇宙：
1. **狀態空間 $\mathcal{S}$ (Status)**：環境與探索者所處之時空拓撲點位（如迷宮坐標、棋局殘型）。
2. **行動空間 $\mathcal{A}$ (Actio)**：發條探索者於當下可撥動之機械機關（轉向、躍進、施力）。
3. **轉移機率 $\mathcal{P}$ (Transition Kernel)**：動態自然法則 $P(s' \mid s, a)$，決定行動後落入新狀態之機遇。
4. **即時賞罰 $\mathcal{R}$ (Praemium)**：大自然之立即回饋 $R(s, a, s')$，阿基米德天平上之沉浮砝碼。
5. **折現因子 $\gamma \in [0, 1)$ (Remissio)**：對遠期未來果報之衡量遠見，愈趨近 $1$ 愈深謀遠慮。

---

## 三、 核心數學卷軸：貝爾曼最優方程 (Calculus Bellmanianus)
追求累積期望回報最大化之最優策略 $\pi^*$：

$$V^*(s) = \max_{a \in \mathcal{A}} \left[ R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s' \mid s, a) V^*(s') \right]$$

$$Q^*(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P(s' \mid s, a) \max_{a' \in \mathcal{A}} Q^*(s', a')$$

* **手札註解**：當前行動之最優價值，等於當下即時賞罰，加上未來最優狀態之折現期望總和。

---

## 四、 中央手繪解剖大圖：阿基米德天平與發條探索者閉環 (Figura II)
* **(左) 微觀主體：發條探索者 (Clockwork Explorer)**
  - 帶有決策指針與試誤游標之發條人偶，前方投射出動作選擇之機率扇面 $\pi(a \mid s)$。
* **(中) 交互天平：阿基米德賞罰天平 (Balance of Reward & Penalty)**
  - 左盤承載正向獎勵（金砝碼），右盤承載負向懲罰（鉛砝碼），槓桿傾角直接牽引策略梯度。
* **(右) 宏觀演化：價值曲面與最優路徑 (Optimal Policy Manifold)**
  - 迷宮空間中自混沌隨機遊走（Random Walk），自發收斂為流暢如流體的最優軌跡線。

---

## 五、 典範之衡鑑：監督學習 vs 強化學習 (Paradigmata)

| 比較維度 | 監督學習 (Supervised Learning) | 強化學習 (Reinforcement Learning) |
| :--- | :--- | :--- |
| **指導者 (Supervisor)** | **明師親炙**：給予標準答案（Ground Truth 標籤）。 | **自然試誤**：僅給予延遲的成敗賞罰信號。 |
| **回饋時滯 (Feedback)** | **立即性**：每筆輸入即刻對比誤差損失。 | **延遲性 (Delayed Reward)**：當下一舉，影響百步之後果報。 |
| **探索與利用 (Dilemma)** | 無須探索：固定訓練集靜態分佈。 | **天平抉擇 (Exploration vs Exploitation)**：採摘當前甜果 vs 涉險開拓新境。 |

---

## 六、 歷代三大里程碑驗證 (Exempla Classica)
1. **Case 01 · Q-Learning 無模型探索 (Watkins, 1989)**
   - 擺脫對環境轉移矩陣之依賴，僅憑單步經驗 $Q(s, a) \leftarrow Q(s, a) + \alpha \delta$ 即可自發逼近全局最優解。
2. **Case 02 · 蒙地卡羅樹搜尋 MCTS (Coulom, 2006)**
   - 選擇、擴展、模擬、反向傳播四步循環，以古典隨機模擬之光芒刺破天文級決策樹之黑暗迷霧。
3. **Case 03 · 深度強化學習 DQN / AlphaGo (DeepMind, 2013-2016)**
   - 經驗回放 (Experience Replay) 與雙神經網絡之結合，以矽晶之算力於古老圍棋千變萬化中悟出神之一手。

---

# 【延伸補充區】（進階研究與背景資料，不擠入單頁圖卡）

### 1. 馬可夫性質 (Markov Property) 之哲學涵義
* 系統下一狀態的機率分佈，僅由當前狀態決定，而與過去歷史無關：
  $$P(S_{t+1} = s_{t+1} \mid S_t = s_t, S_{t-1} = s_{t-1}, \dots, S_0 = s_0) = P(S_{t+1} = s_{t+1} \mid S_t = s_t)$$
* 這代表「當下即全知」，過去之一切歷史記憶已完全凝結壓縮於現有狀態向量 $S_t$ 之中。

### 2. 探索與利用之 $\epsilon$-貪婪策略推導
* 策略定義：
  $$\pi(a \mid s) = \begin{cases} 1 - \epsilon + \frac{\epsilon}{|\mathcal{A}|}, & \text{if } a = \arg\max_{a'} Q(s, a') \\ \frac{\epsilon}{|\mathcal{A}|}, & \text{otherwise} \end{cases}$$
* 保證發條探索者有 $\epsilon$ 機率涉足未知荒原，避免過早陷入局域最優之泥淖。

### 3. 策略梯度定理 (Policy Gradient Theorem)
* 當策略以連續參數 $\theta$ 表達時，期望回報 $J(\theta)$ 對參數之梯度：
  $$\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta} \left[ \nabla_\theta \log \pi_\theta(a \mid s) Q^{\pi_\theta}(s, a) \right]$$
