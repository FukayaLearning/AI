---
title: "AIモデル・アーキテクチャ・形式入門：フォーマット・量子化・分類と選定ガイド"
description: "LLM/VLM/世界モデルの種別、GGUF/MLX/Safetensors等の保存形式、量子化（AWQ/INT4/FP4）、アーキテクチャ（MoE/Mamba）、およびクラス別ベンチマーク選定マップを体系的に解説します。"
target_personas:
  persona-m365: "○"
  persona-local: "◎"
  persona-cloud: "◎"
requirements:
  hardware: "ローカルLLM実行時はVRAM 8GB〜24GB+推奨（クラウドAPI利用時は制限なし）"
  tools: ["llama.cpp", "Ollama", "vLLM", "MLX", "Hugging Face transformers"]
  cloud_api: "不要（ローカル実行）または OpenAI / Anthropic / Google 等の各種API"
---

!!! info "対象読者ガイド"
    - 🏢 **M365 Copilot**: ○（背後で動くフロンティアモデルやSLMの仕組み、性能特性の理解に役立ちます）
    - 💻 **ローカルLLM**: ◎（GGUF/MLX等のモデル形式、量子化ビット数選定、VRAM別モデル選定の決定版ガイド）
    - ☁️ **高度エージェント**: ◎（タスクに応じたモデルアーキテクチャ選定、クローズド/オープンモデルのベンチマーク比較に直結）

---

# 2.0 AIモデル・アーキテクチャ・形式：全体概要と選定ガイド

急速に進化するAIエコシステムにおいて、モデルの **「種別（LLM/VLM/世界モデル）」「内部構造（アーキテクチャ）」「保存・配信形式（Safetensors/GGUF/MLX）」「軽量化技術（量子化）」** を正しく理解することは、適切なモデル選定やシステム設計を行うための必須知識です。

本ドキュメントでは、モデルにまつわる要素技術を体系的に整理し、読者の環境（ペルソナ）に最適なモデル選定を支援します。

```mermaid
flowchart TD
    subgraph M1["1. モデル種別 & モダリティ"]
        A1["LLM (テキスト) / SLM (軽量小型)"]
        A2["Reasoning / 思考モデル (o1 / R1)"]
        A3["VLM (画像・動画) / 音声 / 世界モデル"]
    end

    subgraph M2["2. モデルアーキテクチャ"]
        B1["Dense Decoder-Only (標準 Transformer)"]
        B2["MoE (Mixture of Experts: 高速・大容量)"]
        B3["SSM / Mamba / ハイブリッド"]
    end

    subgraph M3["3. 最適化 & 量子化"]
        C1["量子化 (INT4 / FP4 / AWQ / GPTQ)"]
        C2["PEFT / LoRA (効率的ファインチューニング)"]
        C3["KVキャッシュ圧縮 & FlashAttention"]
    end

    subgraph M4["4. モデル保存形式 & 実行環境"]
        D1["Safetensors (Hugging Face / GPU クラウド)"]
        D2["GGUF (llama.cpp / Ollama / ローカル推論)"]
        D3["MLX (Apple Silicon ネイティブ)"]
        D4["ONNX / Core ML (エッジ・モバイル)"]
    end

    M1 --> M2 --> M3 --> M4
```

---

## 1. モデル保存形式 & 実行ランタイム (Model Formats & Runtimes)

モデルの重み（Weights）をファイルに保存し、推論エンジンにロードするための形式は、利用環境やターゲットハードウェアによって最適解が異なります。

| 形式 / ランタイム | 主な用途・ターゲット | 特徴・メリット | 代表的な実行エンジン |
| :--- | :--- | :--- | :--- |
| **Safetensors** | クラウドGPU / 学習 / Hugging Face標準 | ・Pickleの任意コード実行脆弱性を排除した安全なフォーマット<br>・ゼロコピー（Zero-copy）ロード対応でメモリ転送が高速 | PyTorch, Hugging Face, vLLM, TensorRT-LLM |
| **GGUF**<br>*(旧 GGML)* | ローカルPC / CPU+GPU推論 / エッジ | ・モデル重み、トークナイザ、メタデータを1ファイルに統合<br>・メモリマップ（mmap）高速起動<br>・VRAM容量に合わせてGPUとCPU(RAM)にレイヤ分割オフロード可能 | llama.cpp, Ollama, LM Studio, Jan |
| **MLX 形式** | Apple Silicon (Mac / iPad) | ・Apple SiliconのUnified Memory Architecture (UMA) ネイティブ<br>・Metal GPU + CPU間でゼロコピー高速推論・LoRA学習 | Apple MLX, mlx-lm |
| **AWQ / GPTQ / EXL2** | NVIDIA GPU 特化推論 | ・GPUのTensorコアに最適化された4bit/8bit重み形式<br>・EXL2（ExLlamaV2）は超高速トークン生成（100+ tok/s）を実現 | vLLM, SGLang, ExLlamaV2, TGI |
| **ONNX / Core ML** | エッジデバイス / Windows / iOS / Web | ・クロスプラットフォーム中間表現（ONNX）<br>・Apple Neural Engine (ANE) や NPU への最適化コンパイル | ONNX Runtime, Core ML Tools, WebLLM |

??? tip "💡 GGUF形式の重要性（ローカルLLMのデファクトスタンダード）"
    GGUF（GPT-Generated Unified Format）は、Georgi Gerganov氏率いる `llama.cpp` プロジェクトが策定した形式です。
    従来のPyTorch形式ではGPUのVRAMに全モデルを載せる必要がありましたが、GGUFでは「24層中18層をGPUのVRAMに、残り6層をメインメモリ(RAM)のCPUで計算」といった**動的オフロード**が可能なため、民生用PCでも手軽に大型モデルを動作させることができます。

---

## 2. モデル種別とモダリティ (Model Modalities & Types)

AIモデルは入力・出力のモダリティや、内部の推論メカニズムによって以下のように分類されます。

```mermaid
mindmap
  root((AIモデル分類))
    テキスト・推論
      LLM["大規模言語モデル (70B+ / フロンティア)"]
      SLM["小規模言語モデル (1B〜8B: エッジ/高速)"]
      Reasoning["推論・思考モデル (o1 / DeepSeek-R1)"]
    マルチモーダル
      VLM["視覚言語モデル (画像理解・UI操作)"]
      Audio["音声・会話モデル (端点対向低遅延)"]
      Video_3D["動画・3D空間生成 (DiT / NeRF)"]
    物理・自律
      World_Models["世界モデル (環境ダイナミクスシミュレーション)"]
      VLA["Vision-Language-Action (ロボティクス制御)"]
```

### 2.1 テキスト・推論特化モデル
- **大規模言語モデル (LLM / Large Language Models)**:
  パラメータ数数十B〜数百B級。広範な知識、高度なコード生成、長文文脈把握を行う基幹モデル。
- **小規模言語モデル (SLM / Small Language Models)**:
  1B〜8Bクラス（例: Llama 3.2 3B, Qwen 2.5 7B, Phi-4 mini）。低レイテンシ、ローカル動作、特定タスク特化に向く。
- **推論・思考モデル (Reasoning / Thinking Models)**:
  思考の連鎖（Chain-of-Thought）をモデル内部で自律的に展開し、回答前に「推論時計算量（Test-Time Compute）」を投入して難関数学・競プロ・論理パズルを解く新世代モデル（OpenAI o1/o3-mini, DeepSeek-R1 等）。

### 2.2 マルチモーダル & 物理・世界モデル
- **視覚言語モデル (VLM / Vision-Language Models)**:
  テキストと画像・ドキュメント（PDF/OCR）・スクリーンショットを統合理解（GPT-4o, Claude 3.5 Sonnet, Qwen2.5-VL 等）。
- **音声・リアルタイム対話モデル**:
  音声波形を直接トークンとして処理し、感情・抑揚を保持しながら100〜300msの超低遅延で双方向対話を実現。
- **世界モデル (World Models) & VLA**:
  テキストや映像から物理世界の因果関係や空間ダイナミクスを予測・シミュレーションし、ロボットの行動計画（VLA: Vision-Language-Action）や自律運転に活用。

---

## 3. モデルアーキテクチャ (Model Architectures)

Transformerを基盤としつつ、計算効率・コンテキスト長の限界を突破するための多様な構造が登場しています。

### 3.1 Dense Transformer vs MoE (Mixture of Experts)
- **Dense（密結合モデル）**:
  すべての入力トークンに対して、モデル内の全パラメータを使って計算を行う（例: Llama 3.3 70B）。高い知識密度を持つが計算コストが高い。
- **MoE（スパース疎結合モデル）**:
  モデル全体は巨大（例: 671B）だが、トークンごとにルーターが最適な専門家（Expert）サブネットワーク（例: 37B分）のみを選択して活性化させる（例: DeepSeek-V3, Mixtral 8x7B）。**「高い知能を持ちながら高速な推論スループット」** を実現。

### 3.2 状態空間モデル (SSM / Mamba) & 線形Attention
Transformerの自己注意機構（Attention）が抱える「系列長に対する二次関数的計算量 $\mathcal{O}(N^2)$」の課題を克服するため、線形計算量 $\mathcal{O}(N)$ で無限コンテキストを処理可能なアーキテクチャ（Mamba, Jamba, RWKV）も発展しています。

---

## 4. モデル最適化 & 量子化技術 (Optimization & Quantization)

ハードウェア制約（VRAM容量・帯域）を克服し、モデルを高速・軽量に実行するための主要技術です。

### 4.1 量子化（Quantization）の主要手法
浮動小数点数（FP16 / BF16: 16bit）で表現された重みや活性化関数を、低ビット（8bit, 4bit, 2bit）に丸める技術です。

```mermaid
flowchart LR
    BF16["FP16 / BF16 (16bit)<br>高品質・大VRAM<br>約2.0 GB / 1B params"] --> INT8["INT8 / FP8 (8bit)<br>精度劣化ほぼゼロ<br>約1.0 GB / 1B params"]
    INT8 --> INT4["INT4 / FP4 (4bit)<br>実用推奨バランス<br>約0.6〜0.8 GB / 1B params"]
    INT4 --> INT2["INT2 / 1.58bit (極限)<br>BitNet / 実験段階<br>超省メモリ・低精度"]
```

- **重みのみ量子化 (Weight-Only Quantization)**:
  - **GGUF (k-quants / i-quants)**: `Q4_K_M`, `Q5_K_M`, `IQ4_XS` など。重要レイヤの精度を維持する不等分割量子化。
  - **AWQ (Activation-aware Weight Quantization)**: 活性化値の大きい重要な1%の重みを保護し、4bit化での精度低下を最小化。
  - **EXL2 (ExLlamaV2)**: レイヤごとに異なるビットレート（例: 3.5bit〜6.0bit）を細かく割り振る超高速量子化。
- **重み＋活性化量子化 (W8A8 / W4A4 / FP8)**:
  - **FP8 (NVIDIA Ada/Blackwell, AMD MI300X)**: 行列演算器自体を8bit浮動小数点で実行し、VRAM削減と演算速度2倍を両立。

### 4.2 その他の最適化手法
- **PEFT / LoRA (Low-Rank Adaptation)**: 元のモデル重みを固定し、低ランク行列のみを追加学習することで、数GBのVRAMでファインチューニングを実現。
- **KVキャッシュ圧縮 & PagedAttention**: コンテキスト長増大によるメモリ枯渇を防ぐため、KVキャッシュのページ管理やINT8/FP8量子化を適用。
- **知識蒸留 (Knowledge Distillation)**: 超巨大フロンティアモデルの推論過程や出力を教師データとし、小型モデル（7B/14B等）に高度な推論能力を移植。

---

## 5. 最新モデルクラス別ベンチマーク & 選定マップ

各ユースケースやハードウェア環境に応じたモデル選定の詳細は、以下のクラス別ベンチマークドキュメントに網羅されています。

```mermaid
flowchart TD
    subgraph Selection["モデル選定マップ"]
        direction TB
        C["クローズド・フロンティアAPI"] -->|最高知能・クラウド前提| BC["クローズドモデル選定"]
        O1["オープン 400B+ (超大型)"] -->|GPUクラスタ / 複数枚GPU| BO1["超大型オープンモデル選定"]
        O2["オープン 40B〜400B (中〜大型)"] -->|VRAM 48GB〜96GB+| BO2["中〜大型オープンモデル選定"]
        O3["オープン Under 40B (中小型)"] -->|ローカル 8GB〜24GB VRAM| BO3["ローカル/小型モデル選定"]
    end

    click BC "benchmark/Benchmark_Closed_Weights.md" "クローズドモデル選定詳細"
    click BO1 "benchmark/Benchmark_Open_Weights_Over_400B.md" "400B+モデル選定詳細"
    click BO2 "benchmark/Benchmark_Open_Weights_40B_to_400B.md" "40B〜400Bモデル選定詳細"
    click BO3 "benchmark/Benchmark_Open_Weights_Under_40B.md" "40B未満モデル選定詳細"
```

### 📚 詳細ベンチマークドキュメント一覧

- 📊 **[総合ベンチマーク比較マップ & ポジショニングチャート](benchmark/Benchmark_graph.md)**
  - 全体像: クローズド vs オープンの知能・コスト・ハードウェア要件マトリクス
- 🔒 **[クローズド重みモデル (Closed Weights Benchmark)](benchmark/Benchmark_Closed_Weights.md)**
  - 対象: GPT-4o, Claude 3.7 Sonnet / 3.5 Haiku, Gemini 2.0 Flash / Pro, o1, o3-mini
- 🐘 **[超大型オープンモデル (Open Weights Over 400B)](benchmark/Benchmark_Open_Weights_Over_400B.md)**
  - 対象: DeepSeek-V3 / R1 (671B MoE), Llama 3.1 405B 等
- 🐎 **[中〜大型オープンモデル (Open Weights 40B〜400B)](benchmark/Benchmark_Open_Weights_40B_to_400B.md)**
  - 対象: Qwen 2.5 72B, Llama 3.3 70B, DeepSeek-R1-Distill-Llama-70B, Mixtral 8x22B
- 🚀 **[ローカル・中小型オープンモデル (Open Weights Under 40B)](benchmark/Benchmark_Open_Weights_Under_40B.md)**
  - 対象: DeepSeek-R1-Distill-Qwen (14B/32B), Qwen 2.5 (7B/14B/32B), Gemma 2 (9B/27B), Llama 3.2 (3B), Phi-4 (14B)

---

## 6. 本章の個別詳細ドキュメント一覧

- 🏗️ **[2.1 モデルアーキテクチャ徹底解説](2_1_architecture.md)**: Transformer, Attention進化 (GQA/MLA), MoE, Mamba/SSM
- 📦 **[2.2 モデル保存形式・実行ランタイム](2_2_format.md)**: Safetensors, GGUF, MLX, AWQ/EXL2, ONNX/Core ML
- 👁️ **[2.3 マルチモーダルAI & 世界モデル](2_3_multimodal.md)**: VLM, 音声対話, DiT動画生成, VLA・ロボティクス
- ⚙️ **[2.4 モデル量子化徹底解説](2_4_quantization.md)**: AWQ, GPTQ, GGUF k-quants, FP8, EXL2, KVキャッシュ量子化
- 🧠 **[2.5 推論・思考モデル（Reasoning Models）](2_5_reasoning_models.md)**: Test-Time Compute, GRPO, o1/DeepSeek-R1, 思考蒸留
- 🎯 **[2.6 学習手法・PEFT・アライメント](2_6_training_alignment.md)**: LoRA/QLoRA, DPO, GRPO, 事前学習と合成データ
