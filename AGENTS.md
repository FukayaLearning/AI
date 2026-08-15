# AI リポジトリ運用・執筆規約 (AGENTS.md)

本ドキュメントは、本リポジトリ（AI技術・動向ナレッジベース）において、AIエージェントおよび執筆者がドキュメントを作成・編集・管理する際の基本方針と執筆規約を定めたものです。
本プロジェクトは **GitHub Pages (MkDocs Material)** による公開・Webサイト配信を前提としています。

---

## 1. プロジェクト憲章・目的

本リポジトリは、急速に進化するAI技術（基礎理論、モデル、ハードウェア、エンジニアリング、自律エージェント等）の包括的な情報を整理・蓄積し、GitHub Pages上で高品質な技術Webサイトとして一般公開することを目的としています。

### 核心方針
- **読者のシチュエーション（利用環境・制約）に適合した情報提供**:
  AIの活用法は、読者が利用できるツールやハードウェア制約によって全く異なります。「誰向けの技術なのか」「自分の環境で動かせるのか」が一目で判別できるように記事を構造化します。
- **想定読者別「シナリオブック（実践ガイド）」のWebサイト展開**:
  要素技術の解説だけでなく、読者環境に応じた実践的なワークフローやレシピ（シナリオブック）を体系的に公開・提供します。
- **GitHub Pages / MkDocs Material に最適化されたWebドキュメント体験**:
  レスポンシブデザイン、タブ切り替え、Admonition（コールアウト）、Mermaid図、高速検索を活用し、読者が快適に学べるUI/UXを提供します。

---

## 2. 想定読者ペルソナ定義

本リポジトリでは、読者の環境・制約を以下の **3つの主要ペルソナ** に分類します。

| ペルソナID | ペルソナ名称 | 主な利用可能ツール・環境 | 主な制約・前提 | 主な関心事・適用範囲 |
| :--- | :--- | :--- | :--- | :--- |
| **`persona-m365`** | **M365 Copilot 限定環境**<br>*(Enterprise Office Only)* | Microsoft 365 Copilot, Webチャット (Copilot/ChatGPT等) | ・IDE統合不可<br>・外部API/ローカルモデル利用不可<br>・企業ガバナンス/データ保護制約 | Officeアプリ（Word/Excel/PowerPoint/Teams）連携、プロンプト技術、議事録・要約、社内ナレッジ検索 |
| **`persona-local`** | **ローカルLLM環境**<br>*(Local LLM / Air-gapped)* | Ollama, llama.cpp, vLLM, Continue, Cline (OpenAI互換API) | ・VRAM制限（8GB / 24GB / 96GB 等）<br>・クローズドモデルより知能・推論速度・コンテキスト長で劣る<br>・機密情報保持/オンプレ要件 | 量子化モデル選定、VRAM別サイジング、小型推論/思考モデル活用、ローカルRAG、IDE補完連携 |
| **`persona-cloud`** | **高度クラウドエージェント環境**<br>*(Advanced Cloud Agent)* | Claude Code, GitHub Copilot, Cursor, Windsurf, OpenAI/Anthropic API | ・原則としてモデル・ツールの制限なし<br>・API従量課金/利用規約への配慮 | 自律型コーディング（SWE-Agents/Loop Engineering）、MCP連携、長文コンテキスト活用、Multi-Agent構築 |

### ローカルLLM環境 (`persona-local`) のVRAM基準目安
ローカルLLMに関する記事やシナリオを執筆する際は、以下のVRAMクラスを明記してください。

- **8GB VRAM (エントリー / 一般PC・Mac)**:
  - 3B〜8Bクラスの量子化モデル（Q4_K_M / Q8_0）、小型SLM（Llama 3.2 3B, Qwen 2.5 7B Q4, Phi-4 mini等）
  - 単一タスク補完、軽量チャット向け
- **24GB VRAM (ハイエンドコンシューマ / RTX 3090/4090, Apple Silicon 32GB~)**:
  - 14B〜32Bクラスの量子化モデル（Qwen 2.5 14B/32B Q4, DeepSeek-R1-Distill-Qwen-14B/32B 等）、小型MoE
  - 高度なコード生成、ローカルRAG、本格的な思考モデル実行が可能
- **96GB+ VRAM (ワークステーション / Mac Studio 128GB, 多枚数GPU)**:
  - 70Bクラス（Llama 3.3 70B Q4/Q8）、大型MoEモデル（Qwen 2.5 Max級/DeepSeek一部構成等）
  - クローズドモデルに迫る高度推論、大規模コンテキスト処理が可能

---

## 3. GitHub Pages / MkDocs 執筆・メタデータ規約

GitHub Pages上で正しくビルド・公開され、検索性・可読性の高いWebページを構築するためのルールです。

### 3.1 記事ヘッダー標準フォーマット (Frontmatter & Admonition)

すべての記事の先頭には、SEO/OGP用の **YAML Frontmatter** と **MkDocs Material Admonition（対象読者ガイド）** を配置します。

```markdown
---
title: "記事タイトル"
description: "記事の概要（1〜2文。SEOメタディスクリプションおよびソーシャルプレビューとして利用されます）"
target_personas:
  persona-m365: "✕"       # [◎ (最適) | ○ (利用可) | △ (一部のみ) | ✕ (対象外)]
  persona-local: "◎"
  persona-cloud: "○"
requirements:
  hardware: "VRAM 24GB以上推奨 (ローカルLLM実行時)"
  tools: ["Ollama", "VS Code (Continue拡張機能)"]
  cloud_api: "不要"
---

!!! info "対象読者ガイド"
    - 🏢 **M365 Copilot**: ✕（IDE/ローカル推論環境が必要なため対象外）
    - 💻 **ローカルLLM**: ◎（24GB VRAM環境での本格導入手順を解説）
    - ☁️ **高度エージェント**: ○（クラウドAPIでも代替可能ですが、ローカル完結手法を中心に扱います）

---
```

### 3.2 リンク & 参照規約 (MkDocsビルド完全互換)

MkDocsのビルド時バリデーション（`--strict` モードでのリンク切れ検知）をパスし、静的HTMLへの正確な変換を保証するため、以下の記法を厳守します。

1. **ドキュメント間リンク (Cross-Document Links)**:
   - 必ず **`.md` 拡張子を含む相対パス** で記述します。
   - 例: `[モデル選定ガイド](../models/benchmark/Benchmark_Open_Weights_Under_40B.md)`
   - アンカー付きリンク: `[GPU仕様](../1_hardware/1_0_introduction.md#gpu-spec)`
   - ※ 絶対URLや拡張子なしリンクはリンク切れ・ビルドエラーの原因となるため禁止。

2. **コンテンツ埋め込み (PyMdown Snippets 記法)**:
   - 他のMarkdownや表・コードブロックを再利用・インポートする場合は、`pymdownx.snippets` 記法（`--8<--`）を使用します。
   - **ファイル全体のインクルード**:
     ```markdown
     --8<-- "models/benchmark/Benchmark_Open_Weights_Under_40B.md"
     ```
   - **行範囲指定インクルード**:
     ```markdown
     --8<-- "models/benchmark/Benchmark_Open_Weights_Under_40B.md:10:30"
     ```

### 3.3 GitHub Pages 向けリッチUIコンポーネントの活用

MkDocs Materialが提供する以下のUI表現を積極的に活用し、Webサイトとしての視認性を高めます。

- **コンテンツタブ (Content Tabs)**:
  環境別・スペック別の手順を切り替え表示する際に使用。
  ```markdown
  === "8GB VRAM (エントリー)"
      小型SLM（Qwen 2.5 7B Q4等）を用いた設定手順...

  === "24GB VRAM (ハイエンド)"
      14B〜32Bクラスの思考モデルを用いた設定手順...
  ```

- **折りたたみAdmonition (Collapsible Details)**:
  補足情報やトラブルシューティングに使用。
  ```markdown
  ??? tip "上級者向けTips: KV Cache量子化によるVRAM削減"
      詳細な設定方法とフラグ指定について...
  ```

- **Mermaid ダイアグラム (Mermaid Visualizations)**:
  アーキテクチャやエージェントループ、データフローは Mermaid 記法を用いて視覚化します。

---

## 4. 想定読者別シナリオブック（Scenario Books）の構成方針

個別要素技術の解説とは別に、**「読者が自身の環境で目的を達成するための実践ガイド（シナリオブック）」** をペルソナごとに **1つのMarkdownファイル** として集約・管理します。

GitHub Pages上でシームレスに閲覧・展開できるよう、関連する技術解説Markdownへの相対リンクおよび Snippets インポート（`--8<--`）を活用して構成します。

### ファイル配置方針
```text
scenarios/
├── persona_m365.md    # M365 Copilot 限定環境向けシナリオブック
├── persona_local.md   # ローカルLLM環境向けシナリオブック
└── persona_cloud.md   # 高度クラウドエージェント向けシナリオブック
```

### シナリオファイルの標準構成（1ファイル完結型）
各シナリオファイルは以下の構成とし、GitHub Pages上でワンストップの実践ハブとして機能するように記述します。

1. **ヘッダー & ペルソナ前提条件**:
   - Frontmatter & `!!! info "対象読者ガイド"`
2. **実践ワークフロー（ステップ別目次 & ガイド）**:
   - 具体的な設定ファイル、プロンプト、コマンド例
   - 関連する基礎技術・モデル解説記事への MkDocs 相対リンクまたは Snippets 埋め込み
3. **トラブルシューティング & 回避策**:
   - `??? warning "トラブルシューティング"` などの折りたたみAdmonitionを活用
4. **関連ドキュメント一覧（Reference Index）**:
   - シナリオ内で参照したリポジトリ内ドキュメントの包括的リンクリスト（MkDocs 相対リンク形式）

---

## 5. AIエージェント行動規範（Agent Operational Guidelines）

本リポジトリで動作するすべてのAIエージェント（Antigravity、Claude Code、Cursor等）は、以下のルールを厳守してください。

1. **新規記事作成時のペルソナ判定とメタデータ付与**:
   - 新しいトピックや記事を追加する際は、必ず対象となる `target_personas` を判定し、Frontmatter および対象読者ガイドを漏れなく記載すること。
2. **GitHub Pages ビルド整合性の担保**:
   - 壊れた相対リンク、不正なYAML構文、無効なSnippetパスを配置しないこと（ビルド破壊を防止）。
3. **環境依存記述の明確化**:
   - 「LLMに〜〜させる」といった曖昧な記述を避け、「M365 Copilotのプロンプト」「Ollama経由のQwen 2.5 14B」「Claude 3.7 Sonnet + MCP」のように、どの環境・モデル規模を想定した記述かを明確にすること。
4. **シナリオブックとの双方向リンク**:
   - 基礎技術記事（例: `models/`, `1_hardware/`）を書く際は、それがどのペルソナのどのシナリオに役立つかを意識し、必要に応じてシナリオブックへのリンクを張ること。
5. **言語・トーン**:
   - 日本語で論理的かつ分かりやすく記述すること。
   - エンジニアが実務で判断材料として使える具体的な数値（VRAM消費量、パラメータ数、コンテキスト長、ベンチマークスコア等）を重視すること。
