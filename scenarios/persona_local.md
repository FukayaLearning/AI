---
title: "ローカルLLM環境向け実践シナリオブック"
description: "VRAM制約（8GB/24GB/96GB）やオンプレ要件の中で、OllamaやContinue/Cline等を活用して高効率な開発環境を構築する実践ガイド"
target_personas:
  persona-m365: "✕"
  persona-local: "◎"
  persona-cloud: "○"
requirements:
  hardware: "VRAM 8GB / 24GB / 96GB+ いずれかのGPU/Mac環境"
  tools: ["Ollama / llama.cpp / vLLM", "VS Code (Continue / Cline)"]
  cloud_api: "不要 (ローカル完結)"
---

!!! info "対象読者ガイド"
    - 🏢 **M365 Copilot**: ✕（Office環境限定の方は [M365 Copilot シナリオブック](persona_m365.md) をご参照ください）
    - 💻 **ローカルLLM**: ◎（本シナリオブックの対象です）
    - ☁️ **高度エージェント**: ○（クラウドモデルとローカルモデルのハイブリッド利用時にも参考になります）

---

# ローカルLLM環境向け実践シナリオブック

## 1. 前提条件 & VRAM別サイジング基準

| VRAMクラス | 代表的なハードウェア | 推奨モデル規模 | 主な用途・性能感 |
| :--- | :--- | :--- | :--- |
| **8GB** | RTX 3060/4060, M1/M2/M3 Mac (16GB RAM) | 3B〜8B (Q4_K_M) | コード補完、軽量チャット、関数単位のレビュー |
| **24GB** | RTX 3090/4090, Apple Silicon 32GB~64GB | 14B〜32B (Q4), 小型MoE | 本格的なリファクタリング、小型思考モデル、ローカルRAG |
| **96GB+** | Mac Studio 128GB, 多枚数GPU (24GB×4等) | 70B (Q4/Q8), 大型MoE | フロンティア級推論、長文コード解析、自律型ローカルエージェント |

---

## 2. 実践ワークフロー & レシピ

### Step 1: モデル選定 & サービング構築
- [Open Weights Under 40B ベンチマーク](../models/benchmark/Benchmark_Open_Weights_Under_40B.md) を参考にモデルを選定
- Ollama または vLLM による推論サーバの起動とGPUメモリ割り当て最適化

### Step 2: IDE連携 (VS Code + Continue / Cline)
- OpenAI互換APIエンドポイントの設定
- タブ補完専用の小型SLMと、チャット・編集用の思考モデルの使い分け設定

### Step 3: 機密データを守るローカルRAG & ナレッジ検索
- Chroma / Qdrant を用いたローカル埋め込み・コードベースインデックス化
- 高速リランキングによる検索精度の向上

### Step 4: 小型思考・推論モデルの活用
- DeepSeek-R1 蒸留モデルや Qwen 2.5 思考モデルによるバグ解析・アルゴリズム設計

---

## 3. トラブルシューティング & Tips
??? warning "VRAM溢れ（OOM）や推論速度低下への対処"
    - **OOM対策**: コンテキスト長（`num_ctx`）を8kや16kに制限する、KV Cacheの量子化を有効化する
    - **速度低下**: レイヤーオフロード（GPU/CPU分散）の比率を見直し、GPU VRAM内にモデル本体が収まる量子化サイズ（Q4_K_Mなど）を選択する

---

## 4. 関連ドキュメント一覧 (Reference Index)
- 🧠 [Open Weights Under 40B ベンチマーク](../models/benchmark/Benchmark_Open_Weights_Under_40B.md)
- 🧠 [Open Weights 40B to 400B ベンチマーク](../models/benchmark/Benchmark_Open_Weights_40B_to_400B.md)
- ⚙️ [ハードウェア導入ガイド](../1_hardware/1_0_introduction.md)
- 📋 [AI 関連技術見出し体系 (Abstract.md)](../Abstract.md)
- 📜 [執筆・運用規約 (AGENTS.md)](../AGENTS.md)
