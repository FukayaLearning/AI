# AI 関連技術・動向メモ (全レイヤー・包括的見出し体系)

> **ソフトウェアエンジニア（SWE）との関連度指標**:
>
> - ★★★★★ : 必須・日常的に実装/活用する領域 (アプリケーション実装, エージェント, プロンプト, 開発ツール等)
> - ★★★★☆ : 高い (システムアーキテクチャ設計, RAG, Vector DB, 推論サービング, Evals/品質評価等)
> - ★★★☆☆ : 中程度 (仕組みの理解・選定・最適化で知っておくべき領域: モデル構造, 量子化, LoRA, キャッシュ等)
> - ★★☆☆☆ : やや専門的 (インフラ/MLOps/特定ドメインエンジニアが主に担当する領域)
> - ★☆☆☆☆ : 低い (主に半導体製造・物理ハードウェア・設備設計等の専門領域)

---

## 0. 最新トレンド & 最重要注目領域 (Cutting-Edge Trends)

- 自律型AIエージェント (Agentic Workflows & Multi-Agent Orchestration) 【★★★★★】
- 推論時計算 (Test-Time Compute / Reasoning Scale) 【★★★★☆】
- Model Context Protocol (MCP) & エージェント連携標準 【★★★★★】
- フィジカル AI / 世界モデル (World Models & Embodied AI / Robotics) 【★★☆☆☆】
- 超長文コンテキスト (Infinite / Mega Context Windows & KV Cache Optimization) 【★★★★☆】
- オープンフロンティアモデル & 高効率自律蒸留 (DeepSeek-R1 / Llama Era) 【★★★★☆】
- ソフトウェア開発の完全AI自動化 (Loop Engineering / SWE-Agents) 【★★★★★】

## 1. ハードウェア・半導体レイヤ (Hardware & Semiconductors)

- GPU アーキテクチャ (NVIDIA Blackwell / Rubin 等) 【★★★☆☆】
- TPU / NPU (Google TPU, Apple Neural Engine, スマホ/PC向けNPU) 【★★☆☆☆】
- カスタム ASIC (AWS Trainium/Inferentia, Meta MTIA, Microsoft Maia) 【★★☆☆☆】
- メモリ帯域 & テクノロジー (HBM3e / HBM4, CXL, LPDDR5X) 【★★☆☆☆】
- 次世代コンピューティング (光コンピューティング / 量子AI / Neuromorphic Chip) 【★☆☆☆☆】
- 省電力設計 & データセンター熱設計 (液冷システム / 電力グリッド問題) 【★☆☆☆☆】

## 2. インフラ・分散システムレイヤ (Infrastructure & Networking)

- 大規模分散トレーニングクラスタ (RDMA, InfiniBand, RoCE) 【★★☆☆☆】
- LLM 推論サービングエンジン (vLLM, TensorRT-LLM, TGI, SGLang) 【★★★★☆】
- 分散並列手法 (Data Parallelism, Tensor Parallelism, Pipeline Parallelism, 3D Parallelism) 【★★★☆☆】
- オンデバイス・エッジ推論環境 (ggml/llama.cpp, ONNX Runtime, CoreML) 【★★★★☆】
- クラスターオーケストレーション & 障害耐性 (Kubeflow, Ray, Slurm) 【★★★☆☆】

## 3. 基礎モデル & アーキテクチャレイヤ (Foundation Models & Architecture)

- Transformer 拡張・代替アーキテクチャ (Mamba / SSM, RWKV, Linear Attention) 【★★★☆☆】
- 大規模言語モデル (LLM: Decoder-Only, Encoder-Decoder) 【★★★★☆】
- 推論・思考モデル (Reasoning / Thinking Models) 【★★★★★】
- 小規模言語モデル (SLM: Small Language Models) 【★★★★☆】
- ビジョン・言語・マルチモーダルモデル (VLM, Vision-Language-Action Models) 【★★★★☆】
- 音声・音楽生成モデル (Voice Cloning, Real-time Audio-to-Audio) 【★★★☆☆】
- 動画・3D・空間生成モデル (Diffusion Transformer / DiT, NeRF, 3D Gaussian Splatting) 【★★☆☆☆】
- 世界モデル (World Models / 物理シミュレーション結合) 【★★☆☆☆】

## 4. モデル最適化 & 学習手法レイヤ (Optimization & Training Methods)

- 事前学習 (Pre-training: Synthetic Data / データ品質フィルタリング) 【★★☆☆☆】
- 知識蒸留 (Knowledge Distillation) 【★★★☆☆】
- 量子化技術 (Quantization: INT8, INT4, FP4, AWQ, GGUF, GPTQ, SmoothQuant) 【★★★★☆】
- パラメータ効率的ファインチューニング (PEFT: LoRA, QLoRA, DoRA, Prefix Tuning) 【★★★★☆】
- アライメント・人間からのフィードバック (RLHF, DPO, GRPO, KTO, RLAIF) 【★★★☆☆】
- キャッシュ・メモリ最適化 (KV-Cache Compression, FlashAttention, PagedAttention) 【★★★★☆】

## 5. プロンプト & コンテキストエンジニアリングレイヤ (Prompt & Context Engineering)

- コンテキスト設計 (Context Window Management, System Prompt Architecture) 【★★★★★】
- 構造化思考プロンプティング (Chain-of-Thought, Tree-of-Thoughts, Graph-of-Thoughts) 【★★★★★】
- インコンテキスト学習 (Zero-shot / Few-shot Prompting, In-Context Alignment) 【★★★★★】
- 出力フォーマット制約 (Structured Output / JSON Mode / Grammar-Guided Decoding) 【★★★★★】
- 役割・ペルソナエンジニアリング (Persona & Guardrail Prompting) 【★★★★☆】

## 6. 検索・知識データベース・ナレッジ活用レイヤ (RAG & Knowledge Data)

- RAG アーキテクチャ (Naive RAG, Advanced RAG, Modular RAG, Self-RAG) 【★★★★★】
- ベクトルデータベース (Pinecone, Qdrant, Milvus, Chroma, pgvector) 【★★★★★】
- ハイブリッド検索 (Dense Retrieval + Sparse BM25 / Reranking) 【★★★★★】
- Graph RAG & ナレッジグラフ結合 (Knowledge Graph Integration) 【★★★★☆】
- 高度なチャンキング & エンベディング戦略 (Contextual Retrieval, Late Chunking) 【★★★★☆】
- LLM Wiki / 自律更新型ナレッジベース (Dynamic LLM Wiki / Auto-Synthesized Docs) 【★★★★★】
- コードベースQ&A & リポジトリナレッジ化 (Repo Wiki / Contextual Codebase Indexing) 【★★★★★】
- Deep Research / 自律型調査レポート生成 (Multi-Source Deep Research Agents) 【★★★★☆】

## 7. AI エージェント & オーケストレーションレイヤ (Agent Systems & Orchestration)

- シングル・マルチエージェントフレームワーク (LangChain, LangGraph, LlamaIndex, AutoGen, CrewAI) 【★★★★★】
- ツール利用 & 外部 API 連携 (Tool Use / Function Calling, Browser Use) 【★★★★★】
- ツール仕様 & インターフェース標準 (OpenSpec / OpenAPI, Function Schema) 【★★★★★】
- エージェントスキル & 拡張機能 (Agent Skills / SKILL.md, Custom Plugins) 【★★★★★】
- リポジトリレベルのエージェント指示・規約 (AGENTS.md, GEMINI.md, .cursorrules) 【★★★★★】
- 統合プロトコル (Model Context Protocol / MCP) 【★★★★★】
- エージェント記憶システム (Short-Term, Long-Term Memory, Epistemic Memory) 【★★★★★】
- エージェント計画・反射機能 (Planning, Reflection, Self-Correction Loops) 【★★★★★】

## 8. アプリケーション & UI/UX・開発運用活用レイヤ (Application, Interface & DevSecOps)

- Generative UI / Dynamic UI (リアルタイムUI動的生成) 【★★★★★】
- 対話型・マルチモーダル UI (リアルタイム音声会話, カメラ映像対話) 【★★★★☆】
- コーディング補助・自動化ツール (Cursor, Claude Code, GitHub Copilot, Devin) 【★★★★★】
- AI Code Review & PR 要約・変更影響分析 (Automated Code Review & PR Summary) 【★★★★★】
- 仕様書・コードからのテスト自動生成 (Test Case & E2E Test Generation) 【★★★★☆】
- SRE / 障害トリアージ & ログ根本原因分析 (Log Analysis & Incident RCA Triage) 【★★★★☆】
- Text-to-SQL & データ分析エージェント (AI BI / Natural Language to SQL) 【★★★★☆】
- AI Agent Workflows / ノンコード・ローコード統合 (n8n, Make, Zapier AI) 【★★★★☆】
- 評価・オブザーバビリティ (LangSmith, Phoenix, Arize, Tracing) 【★★★★★】

## 9. 産業別・ドメイン応用 & 業務システム組み込み (Domain & Enterprise Applications)

- エンタープライズ検索 & 社内アシスタント (Enterprise Search & Internal Q&A Bots) 【★★★★★】
- カスタマーサポート自動化 & チケット自動解決 (Autonomous Support Agent & Ticketing) 【★★★★☆】
- 金融・法務・契約書レビュー (Contract Analysis, Compliance, Audit) 【★★★☆☆】
- 医療・ヘルスケア AI (創薬, 医療画像診断, 電子カルテ解析) 【★★☆☆☆】
- 製造・ロボティクス (Industrial Automation, Autonomous Robots) 【★★☆☆☆】
- クリエイティブ・エンタメ (ゲームNPC, 映像制作自動化, 音楽制作) 【★★★☆☆】

## 10. AI セキュリティ・ガバナンス・倫理レイヤ (Safety, Security & Governance)

- ガードレールシステム (NeMo Guardrails, Llama Guard) 【★★★★☆】
- セキュリティ脆弱性・攻撃手法 (Prompt Injection, Jailbreaking, Data Poisoning) 【★★★★★】
- AI ガバナンス・合意形成 (AI Act, EU AI 規制, 著作権法・ライセンス) 【★★★☆☆】
- 評価指標・ベンチマーク (MMLU, HumanEval, SWE-bench, LiveBench) 【★★★★☆】

## 11. エンジニア市場・キャリア・組織構造 (Engineering Market & Workforce)

- 開発者の役割変化 (ループエンジニアリング, エージェントエンジニア, AI Architect) 【★★★★★】
- 組織の AI ネイティブ化 (AI-First Organization, Shadow AI 対策) 【★★★★☆】
- 人材市場・求人動向 (エンジニアのスキルセット変容) 【★★★★☆】
