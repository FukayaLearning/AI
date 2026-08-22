---
title: "学習手法・PEFT・アライメント徹底解説：LoRA/QLoRA、DPO、GRPO、知識蒸留"
description: "事前学習からSFT（指示調整）、PEFT/LoRA（効率的微調整）、アライメント（RLHF/DPO/GRPO）、およびフロンティアモデルからの知識蒸留技術を体系的に解説します。"
target_personas:
  persona-m365: "△"
  persona-local: "◎"
  persona-cloud: "◎"
requirements:
  hardware: "LoRA学習時はVRAM 16GB〜24GB+（QLoRA利用時）"
  tools: ["Unsloth", "Hugging Face TRL / PEFT", "vLLM", "PyTorch"]
  cloud_api: "不要"
---

!!! info "対象読者ガイド"
    - 🏢 **M365 Copilot**: △（モデルのトレーニング技術解説のため直接の利用はありませんが、社内特化AIの仕組みとして参考）
    - 💻 **ローカルLLM**: ◎（**Unslothを用いた単一GPU（RTX 3090/4090）でのLoRA/QLoRA高速ファインチューニング手順**）
    - ☁️ **高度エージェント**: ◎（社内ドメイン特化モデルの構築、DPO/GRPOによる自律タスク向けアライメント手法）

---

# 2.6 学習手法・PEFT・アライメント徹底解説

現代の大規模言語モデルは、膨大なテキストデータを読み込む「事前学習」から、指示に従うようにする「指示調整（SFT）」、人間の好みや論理的正しさに合わせる「アライメント」という多段階のパイプラインを経て作成されます。

本ドキュメントでは、モデルの学習ライフサイクルと、エンジニアが実務で活用するPEFT（LoRA）や最新アライメント手法を体系的に解説します。

---

## 1. LLM 学習パイプラインの全体像

```mermaid
flowchart LR
    D_RAW["1. 大規模生データ<br>(Web, コード, 数学, 合成データ)<br>数兆〜十数兆トークン"] --> PT["事前学習 (Pre-training)<br>Next Token Prediction"]
    PT --> BASE["ベースモデル (Base Model)<br>(文の続きを確率的に補完)"]
    
    D_SFT["高品質対話データ<br>(SFT Dataset)"] --> SFT["指示チューニング (SFT / PEFT)<br>LoRA / QLoRA"]
    BASE --> SFT
    SFT --> INST["Instruct / Chat モデル<br>(ユーザーの指示に応答可能)"]
    
    D_PREF["好み・正誤フィードバック<br>(Pairwise / Rewards)"] --> ALIGN["アライメント<br>(RLHF / DPO / GRPO)"]
    INST --> ALIGN
    ALIGN --> FINAL["最終モデル<br>(安全・論理的・高品質)"]
```

---

## 2. PEFT (Parameter-Efficient Fine-Tuning) & LoRA

モデル全体の重みをすべて更新する「フルファインチューニング」は、70Bモデルで数百GB以上のVRAMが必要となり個人や中小企業では困難です。

そこで用いられるのが、モデル重みの大部分を固定（Freeze）し、わずかな追加パラメータのみを学習する **PEFT（代表格: LoRA / QLoRA）** です。

```mermaid
flowchart TD
    subgraph Full["従来の Full Fine-Tuning (重み W 全体を更新)"]
        IN1["入力 $x$"] --> W_FULL["巨大な行列 $W_{d \times k}$ (学習・更新)"] --> OUT1["出力"]
    end

    subgraph LoRA["LoRA (Low-Rank Adaptation: ランク r 分解)"]
        direction TB
        IN2["入力 $x$"] --> W_FROZEN["固定された元の重み $W_{d \times k}$ (Freeze: 勾配計算なし)"]
        IN2 --> A["低ランク射影 $A_{d \times r}$ (学習対象)"]
        A --> B["低ランク射影 $B_{r \times k}$ (学習対象)"]
        B --> SCALE["スケーリング $\frac{\alpha}{r}$"]
        W_FROZEN & SCALE --> SUM["合算 ($W + \Delta W$)"] --> OUT2["出力"]
    end
```

### 2.1 LoRA / QLoRA / DoRA の比較

| 手法 | 特徴 | メモリ要件 (70Bモデル時) | メリット / デメリット |
| :--- | :--- | :--- | :--- |
| **LoRA** | ランク $r$（例: 8〜64）の低ランク行列 $A, B$ のみ学習 | VRAM 48GB〜80GB | 高速・安定。元の重みと完全にマージ可能 |
| **QLoRA** | 元のモデル重みを **4bit NormalFloat (NF4)** に量子化して固定 | **VRAM 24GB〜48GB** | **民生用GPU（RTX 3090/4090 24GB）で大型モデルを学習可能** |
| **DoRA** *(Weight-Decomposed LoRA)* | 重みの「方向（Direction）」と「大きさ（Magnitude）」を分離学習 | LoRAと同等 | フルファインチューニングに極めて近い表現力を達成 |

---

## 3. アライメント手法の進化（RLHF $\rightarrow$ DPO $\rightarrow$ GRPO）

モデルの出力が「指示に正確に従うか」「幻覚（Hallucination）や危険な発言がないか」「論理的に正しいか」を調整する技術です。

```mermaid
flowchart TD
    subgraph S1["1. RLHF (PPO) 時代"]
        PPO1["人間の好みを学習させた報酬モデル (Reward Model) を構築"]
        PPO2["Actor, Critic, Ref, Reward の4つの巨大モデルを同時常駐 (VRAM消費膨大)"]
    end

    subgraph S2["2. DPO (Direct Preference Optimization) 時代"]
        DPO1["報酬モデルを介さず、好ましい回答 $y_w$ と好ましくない回答 $y_l$ の差分確率から直接クロスエントロピー損失で最適化"]
        DPO2["学習がシンプル・安定・低メモリ"]
    end

    subgraph S3["3. GRPO (Group Relative Policy Optimization) 時代"]
        GRPO1["検証可能な問題（数学・コード）に対し、複数回答を生成してグループ内相対評価"]
        GRPO2["Criticモデル不要で推論時思考モデル（DeepSeek-R1）の強化学習を成功させた"]
    end

    S1 --> S2 --> S3
```

---

## 4. 知識蒸留 (Knowledge Distillation)

超巨大フロンティアモデル（教師: Teacher）の推論結果や思考プロセスをデータセット化し、小型モデル（生徒: Student）に学習させる技術です。

- **従来の蒸留**: 教師モデルの出力確率分布（Logits）を小型モデルに真似させる。
- **思考プロセスの蒸留 (Reasoning Distillation)**:
  DeepSeek-R1（671B）が生成した数十万件の `<think> ... </think>` 思考ログを、Qwen 2.5 14Bや32BにSFT学習させることで、**小型モデルでありながら巨大モデルと同等の多段階推論能力を獲得させることに成功**しました。
