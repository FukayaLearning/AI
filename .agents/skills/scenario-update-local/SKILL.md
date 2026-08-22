---
name: scenario-update-local
description: >-
  ローカルLLM環境向けシナリオブック（scenarios/persona_local.md）を更新・再構成するスキル。
  VRAM別サイジング（8GB/24GB/96GB+）、モデル選定（Qwen/Llama/DeepSeek）、Ollama/llama.cpp/vLLM設定、Continue/Cline等のIDE連携を執筆・整備します。
---

# ローカルLLM シナリオ更新スキル (Scenario Update: Local LLM)

本スキルは、**ローカルLLM環境（`persona-local`）** 向けのシナリオブック（`scenarios/persona_local.md`）を個別に更新・洗練・再構成するための専用ワークフローです。

---

## ターゲットペルソナの特性・前提制約
- **対象環境**: Ollama, llama.cpp, vLLM, LM Studio, Continue, Cline (OpenAI互換API)
- **制約条件**:
  - ハードウェアVRAM容量（8GB / 24GB / 96GB+ 等）によるモデル規模の物理的制約
  - クローズドフロンティアモデル（Claude 3.7 / GPT-4o等）と比較した知能・推論速度・コンテキスト長のトレードオフ
  - 完全オフライン / オンプレミス / エアギャップ（機密保持要件）
- **主目的**:
  - ハードウェアスペック（VRAM）に応じた最適な量子化モデル（GGUF / AWQ / FP8）の選定
  - ローカル推論サーバー（Ollama / vLLM）のセットアップと最適起動パラメータ（GPU Offloading / KV Cache量子化）
  - VS Code / JetBrains 上での Continue 拡張機能によるローカルコード補完・RAG・チャット連携の実装

---

## 参照・取り込み推奨ドキュメント
シナリオ更新時は、リポジトリ内の以下の資料や知見を取り込み・参照してください。
- [ペルソナ対応マッピング](../scenario-curator/references/persona_mapping.md)
- [ハードウェア基礎・VRAMサイジング](../../../1_hardware/1_0_introduction.md)
- [NVIDIA CUDA環境](../../../1_hardware/1_1_nvidia.md) / [Apple Silicon環境](../../../1_hardware/1_2_apple.md)
- [モデル形式（GGUF等）](../../../2_models/2_2_format.md) & [量子化手法](../../../2_models/2_4_quantization.md)
- [思考・推論モデル（DeepSeek-R1蒸留等）](../../../2_models/2_5_reasoning_models.md)
- [10B未満ベンチマーク](../../../2_models/2_A_Benchmark_graph_Unser10B.md)（8GB VRAM向け）
- [40B未満ベンチマーク](../../../2_models/2_B_Benchmark_graph_Unser40B.md)（24GB VRAM向け）
- [40B未満オープンモデル比較](../../../2_models/benchmark/Benchmark_Open_Weights_Under_40B.md)

---

## 執筆・更新ワークフロー

### 1. 対象ファイルの確認
- 編集対象: `scenarios/persona_local.md`
- Frontmatter および Admonition を確認：
  ```markdown
  ---
  title: "ローカルLLM 実践導入シナリオブック"
  description: "VRAM制約別（8GB/24GB/96GB+）のモデル選定・Ollama推論サーバー・IDE連携の実践ガイド"
  target_personas:
    persona-m365: "✕"
    persona-local: "◎"
    persona-cloud: "○"
  requirements:
    hardware: "VRAM 8GB / 24GB / 96GB+ (NVIDIA GPU または Apple Silicon)"
    tools: ["Ollama / llama.cpp", "VS Code (Continue拡張機能)"]
    cloud_api: "不要 (完全オフライン実行可)"
  ---

  !!! info "対象読者ガイド: ローカルLLM環境"
      - 🏢 **M365 Copilot**: ✕（ローカル推論環境・GPUが必要なため対象外）
      - 💻 **ローカルLLM**: ◎（VRAM別サイジングからIDE連携・ローカルRAGまで完全網羅）
      - ☁️ **高度クラウドエージェント**: ○（ローカル検証・フォールバック環境として利用可能）
  ```

### 2. 7セクション標準構成 & Content Tabs の活用
1. **前提・ターゲット環境**: 機密保持要件、オフライン運用の前提
2. **ハードウェア・サイジング基準（Content Tabs 必須）**:
   - `=== "8GB VRAM (エントリー / 一般PC・Mac)"`: 3B〜8Bクラス（Qwen 2.5 7B Q4, Llama 3.2 3B等）
   - `=== "24GB VRAM (ハイエンド / RTX 3090/4090, Apple Silicon 32GB~)"`: 14B〜32Bクラス（Qwen 2.5 14B/32B Q4, DeepSeek-R1-Distill-Qwen-14B/32B等）
   - `=== "96GB+ VRAM (ワークステーション / Mac Studio 128GB)"`: 70Bクラス（Llama 3.3 70B, Qwen 72B等）
3. **モデル選定 & ベンチマーク知見**: Codingスコア、MMLU、推論モデル（思考トークン）の使い分け
4. **推論サーバー構築（Ollama / vLLM）**: `Modelfile` 定義、Context Size (`num_ctx`) 指定、KV Cache量子化
5. **IDE連携（Continue / Cline）**: `config.json` 実例、AutocompleteモデルとChatモデルの分離設定
6. **トラブルシューティング & 最適化**: VRAMあふれ（OOM）対策、CPUオフロードの回避、レスポンス速度チューニング
7. **関連ドキュメント一覧 (Reference Index)**: リポジトリ内リンク（`.md` 拡張子付き相対パス）

### 3. 整合性チェック
更新後、リンタースクリプトで整合性を確認します：
```bash
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/persona_local.md
```
