# ペルソナ別ドキュメント・リソース対応マッピング (Persona Mapping)

本ドキュメントは、本リポジトリ内の各要素技術ドキュメントが、どのペルソナ（`persona-m365`, `persona-local`, `persona-cloud`）の実践シナリオに関連しているかを定義したマッピング表です。シナリオブックの執筆・更新時に参照してください。

---

## 1. ペルソナ別 関連ドキュメント対応マトリクス

| ドキュメントパス / トピック | M365 Copilot (`persona-m365`) | ローカルLLM (`persona-local`) | 高度クラウドエージェント (`persona-cloud`) | 主な取り込み・参照目的 |
| :--- | :---: | :---: | :---: | :--- |
| **`1_hardware/1_0_introduction.md`**<br>(ハードウェア導入・VRAM基礎) | ✕ | **◎ (必須)** | △ | VRAMサイジング基準（8GB/24GB/96GB+）、メモリ帯域幅の重要性 |
| **`1_hardware/1_1_nvidia.md`**<br>(NVIDIA GPU / CUDA) | ✕ | **◎ (最重要)** | △ | RTX 3060/3090/4090等のスペック、TensorRT-LLM等の適合性 |
| **`1_hardware/1_2_apple.md`**<br>(Apple Silicon / Unified Memory) | ✕ | **◎ (重要)** | △ | Mac Mini/Studioでの大容量Unified Memory活用、Metal/MLX推論 |
| **`1_hardware/1_3_amd.md` / `1_4_intel.md`** | ✕ | **○** | △ | ROCm、Intel Arc/NPUでのエッジ・ローカル動作 |
| **`2_models/2_0_introduction.md`**<br>(LLMパラダイム・進化系譜) | ○ | ○ | ○ | 基盤モデルの全体像、Closed vs Openの選定思想 |
| **`2_models/2_1_architecture.md`**<br>(Transformer, MoE, SSM/Mamba) | ✕ | **◎** | **◎** | 小型MoE（Qwen 2.5, DeepSeek等）の動作原理、推論コスト |
| **`2_models/2_2_format.md`**<br>(GGUF, Safetensors, AWQ/EXL2) | ✕ | **◎ (必須)** | ✕ | Ollama/llama.cppで読み込むモデル形式（GGUF量子化タイプ）の選定 |
| **`2_models/2_3_multimodal.md`**<br>(Vision, Audio, Omni) | ○ | **○** | **◎** | マルチモーダル推論、画像・UI解析タスクでの活用 |
| **`2_models/2_4_quantization.md`**<br>(量子化手法: Q4_K_M, AWQ, FP8) | ✕ | **◎ (最重要)** | △ | 精度劣化を最小限に抑えつつVRAMに載せる量子化設定 |
| **`2_models/2_5_reasoning_models.md`**<br>(推論モデル・思考トークン) | △ | **◎** | **◎ (最重要)** | DeepSeek-R1 / OpenAI o-series / Claude Thinking の特性と活用 |
| **`2_models/2_6_training_alignment.md`**<br>(RLHF, DPO, ファインチューニング) | ✕ | **○** | **○** | ローカルLoRAや特定業務向け適応の背景理解 |
| **`2_models/2_A_Benchmark_graph_Unser10B.md`** | ✕ | **◎ (8GB向け)** | ✕ | 8GB VRAM（エントリー）で動く10B未満モデルの性能比較 |
| **`2_models/2_B_Benchmark_graph_Unser40B.md`** | ✕ | **◎ (24GB向け)** | ✕ | 24GB VRAM（ハイエンド）で動く40B未満モデルの性能比較 |
| **`2_models/benchmark/Benchmark_Open_Weights_Under_40B.md`** | ✕ | **◎ (必須)** | ○ | 7B/14B/32Bクラスのベンチマーク（Coding, Reasoning, MMLU） |
| **`2_models/benchmark/Benchmark_Open_Weights_40B_to_400B.md`** | ✕ | **◎ (96GB+向け)** | ○ | 70B/Qwen 72B等のハイエンドローカルモデル性能 |
| **`2_models/benchmark/Benchmark_Open_Weights_Over_400B.md`** | ✕ | △ (クラスタ要) | ○ | Llama 3.1 405B等のフロンティア級オープンモデル |
| **`2_models/benchmark/Benchmark_Closed_Weights_Flash.md`** | **◎ (M365裏側)** | ✕ | **◎ (最重要)** | Claude 3.5/3.7, GPT-4o, Gemini 2.0 Flash等の速度・知能比較 |
| **`11_engineering/` (今後追加)**<br>(Prompt Eng, Agent Loop, MCP, RAG) | **◎ (Prompt/Search)** | **◎ (Local RAG)** | **◎ (Agent/MCP)** | 各ペルソナにおける実践実装コード・設定例 |

---

## 2. ペルソナ別 取り込み・構成方針

### 1. `persona_m365.md`（M365 Copilot 限定環境）
- **前提**: インストール権限なし、API課金なし、Office UIとWebチャットのみ
- **取り込むべき知見**:
  - `2_models/benchmark/Benchmark_Closed_Weights_Flash.md`（商用フロンティアモデルの推論特性・思考パターンの理解）
  - 今後追加される `11_engineering/` のプロンプティング技術・ナレッジ検索（RAG）の基礎
- **構成のポイント**:
  - 技術的なコマンドやVRAM設定は排除し、Word/Excel/Teamsでのプロンプトテンプレート、社内データグラウンディングのコツに特化。

### 2. `persona_local.md`（ローカルLLM環境）
- **前提**: VRAM制約（8GB / 24GB / 96GB+）、完全オフライン/オンプレ、IDE補完・RAG
- **取り込むべき知見**:
  - `1_hardware/`（VRAMサイジング、NVIDIA CUDA / Apple Metal）
  - `2_models/2_2_format.md` & `2_4_quantization.md`（GGUF形式、Q4_K_M量子化）
  - `2_models/2_5_reasoning_models.md`（小型R1蒸留モデル等の思考活用）
  - `2_models/benchmark/Benchmark_Open_Weights_Under_40B.md` 等（VRAM別モデル選定）
- **構成のポイント**:
  - ハードウェアスペック別の「Content Tabs」を用いて、手元のGPU環境に応じた最適なモデルと推論設定（Ollama/llama.cpp）が迷わず選べるように統合。

### 3. `persona_cloud.md`（高度クラウドエージェント環境）
- **前提**: Claude Code / Cursor / Windsurf / MCP連携、最新フロンティアモデル利用可能
- **取り込むべき知見**:
  - `2_models/benchmark/Benchmark_Closed_Weights_Flash.md`（モデル別コーディング・推論性能）
  - `2_models/2_5_reasoning_models.md`（Thinking/Extended Reasoningの使い分け）
  - `11_engineering/`（SWE-Agentループ、MCPツール連携、Prompt Caching）
- **構成のポイント**:
  - 自律エージェントのループ設計、MCPによるローカル環境・DB・外部APIの統合、トークンコスト・キャッシュ最適化を一連のワークフローとして統合。
