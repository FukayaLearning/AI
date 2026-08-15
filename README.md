# AI Knowledge Base & Scenario Books

本リポジトリは、急速に進化するAI技術（基礎理論、モデル、ハードウェア、エンジニアリング、自律エージェント等）の包括的なナレッジと、**読者の利用環境・制約に応じた実践ガイド（シナリオブック）** を集約・公開するプロジェクトです。

---

## 🎯 想定読者別シナリオブック (Scenario Books)

読者の利用可能なツールやハードウェア環境（VRAM、IDE統合の可否、セキュリティ制約）に応じて、最適な実践ワークフローを1ファイルに集約しています。ご自身の環境に合わせて以下のシナリオブックをご参照ください。

| ペルソナ / 環境 | 主な利用ツール・制約 | シナリオブック |
| :--- | :--- | :--- |
| 🏢 **M365 Copilot 限定環境**<br>*(Enterprise Office Only)* | Microsoft 365 Copilot, Webチャット<br>・IDE統合不可 / 企業データ保護制約 | [M365 Copilot 活用シナリオブック](scenarios/persona_m365.md) |
| 💻 **ローカルLLM環境**<br>*(Local LLM / Air-gapped)* | Ollama, llama.cpp, Continue, Cline<br>・VRAM制限 (8GB / 24GB / 96GB) / オンプレ機密保持 | [ローカルLLM 実践シナリオブック](scenarios/persona_local.md) |
| ☁️ **高度クラウドエージェント環境**<br>*(Advanced Cloud Agent)* | Claude Code, GitHub Copilot, Cursor, MCP<br>・制約最小限 / 自律型コーディング・ループ | [高度クラウドエージェント 活用シナリオブック](scenarios/persona_cloud.md) |

> 💡 **VRAMクラスの目安 (ローカルLLM)**:
> - **8GB VRAM**: 3B〜8Bクラス（Q4/Q8）、小型SLMによる軽量補完・チャット
> - **24GB VRAM**: 14B〜32Bクラス、小型MoE、ローカルRAG、思考モデル実行
> - **96GB+ VRAM**: 70Bクラス、大型MoE、クローズドモデルに迫る高度推論

---

## 📚 ナレッジベース体系 (Knowledge Index)

各要素技術の体系的な見出しおよび詳細ドキュメントへのインデックスです。

- 📋 [**AI 関連技術・動向見出し一覧 (Abstract.md)**](Abstract.md)
  - ソフトウェアエンジニアとの関連度（★1〜★5）付きの全レイヤー見出し体系

### 主なカテゴリ
- 🧠 [**models/ (基礎モデル・選定・ベンチマーク)**](models/)
  - [Open Weights Under 40B ベンチマーク](models/benchmark/Benchmark_Open_Weights_Under_40B.md)
  - [Open Weights 40B to 400B ベンチマーク](models/benchmark/Benchmark_Open_Weights_40B_to_400B.md)
  - [Open Weights Over 400B ベンチマーク](models/benchmark/Benchmark_Open_Weights_Over_400B.md)
  - [Closed Weights ベンチマーク](models/benchmark/Benchmark_Closed_Weights.md)
- ⚙️ [**1_hardware/ (ハードウェア・半導体・GPU)**](1_hardware/1_0_introduction.md)
- 🛠️ [**11_engineering/ (エージェント・RAG・開発自動化)**](11_engineering/)

---

## ✍️ 執筆・運用規約 (For Agents & Contributors)

本リポジトリにドキュメントを追加・編集する際は、[AGENTS.md](AGENTS.md) を遵守してください。

- **記事ヘッダーの標準フォーマット**:
  記事の冒頭に `target_personas`（ペルソナ別マッチ度）および `requirements`（必要スペック・ツール）を記載します。
- **想定読者ガイドの設置**:
  読者がひと目で自身の環境に適しているか判断できる引用ブロックを設けます。
- **シナリオブックとの連携**:
  要素技術の解説を追加した際は、該当するペルソナのシナリオブックからも参照リンクを構成します。
