---
title: "高度クラウドエージェント 実践開発シナリオブック"
description: "Claude Code / Cursor / MCP を駆使した自律型エージェントループと最先端モデル活用の実践ガイド"
target_personas:
  persona-m365: "✕"
  persona-local: "○"
  persona-cloud: "◎"
requirements:
  hardware: "一般的な開発マシン / インターネット接続"
  tools: ["Claude Code", "Cursor / Windsurf", "MCP Servers", "Git"]
  cloud_api: "Anthropic / OpenAI / Google Cloud 等のAPIキーまたはサブスクリプション"
---

!!! info "対象読者ガイド: 高度クラウドエージェント環境"
    - 🏢 **M365 Copilot**: ✕（自律開発ツール・CLI操作が必要なため対象外）
    - 💻 **ローカルLLM**: ○（クラウドエージェントとローカルモデルのハイブリッド運用として参考に可能）
    - ☁️ **高度クラウドエージェント**: ◎（自律ループ・MCP・最新フロンティアモデル連携を完全網羅）

---

# 高度クラウドエージェント 実践開発シナリオブック

## 1. 本シナリオの前提・ターゲット環境

本シナリオは、最先端の商用フロンティアモデル（Claude 3.7 Sonnet, GPT-4o, Gemini 2.0 Flash）および自律型コーディングツール（Claude Code, Cursor, Windsurf, Antigravity等）を活用し、**仕様策定から実装、テスト、リファクタリング、MCP連携までを高度に自動化したい開発者** を対象としています。

### 想定環境と主な特徴
- **利用可能ツール**: Claude Code, Cursor, Windsurf, Model Context Protocol (MCP), 各種LLM API
- **前提条件**:
  - フロンティアモデルの広大なコンテキストウィンドウ（128k〜2Mトークン）と推論時計算（Extended Thinking）をフル活用
  - 外部API課金およびセキュリティ規約への配慮
- **目指すゴール**:
  - タスク駆動型の自律コーディングループ（SWE Loop）を構築する
  - MCPを活用してファイル操作、Git、DB、外部Web検索をエージェントに統合する
  - Prompt Caching やガードレールによりトークンコストと暴走リスクを最適化する

---

## 2. モデル選定戦略 & 推論モードの使い分け

モデル性能の詳細な比較については [Closed Weights ベンチマーク](../2_models/benchmark/Benchmark_Closed_Weights_Flash.md) および [推論・思考モデルの解説](../2_models/2_5_reasoning_models.md) を参照してください。

```mermaid
graph TD
    Task[開発タスクの投入] --> Check{タスクの複雑度}
    Check -->|設計・複雑なリファクタリング・難関バグ| A[Claude 3.7 Sonnet<br>Extended Thinking 有効]
    Check -->|高速な単体テスト作成・Lint修正| B[Gemini 2.0 Flash /<br>GPT-4o mini]
    Check -->|UIデザイン・画面モックアップ| C[マルチモーダル対応モデル<br>Claude 3.7 / GPT-4o]
    
    A --> SWE[SWE 自律開発ループ実行]
    B --> SWE
    C --> SWE
```

- **用途別推奨モデル**:
  - **アーキテクチャ設計・難関実装・コードレビュー**: `Claude 3.7 Sonnet` (Thinking Tokenを活用)
  - **超高速テスト実行・単純な定型コード生成**: `Gemini 2.0 Flash` または `GPT-4o mini`
  - **UI/UXスクリーンショット解析・画像入力**: `Claude 3.7 Sonnet` / `GPT-4o`（詳細は [マルチモーダルモデル](../2_models/2_3_multimodal.md) 参照）

---

## 3. エージェントツールスタック選定

開発スタイルに応じて最適なツールスタックを選択します。

| ツール分類 | 代表的ツール | 主なユースケース | 特徴・強み |
| :--- | :--- | :--- | :--- |
| **CLI自律型** | `Claude Code` / `SWE-Agent` | 大規模リファクタリング、バグ修正の一括完了 | ターミナル完結、Bash/Gitコマンド直接実行、自律ループ |
| **IDE統合型** | `Cursor` / `Windsurf` | 日常的な対話型コーディング、インライン編集 | エディタとの一体感、差分ハイライト、リアルタイム補完 |
| **拡張プロトコル** | `Model Context Protocol (MCP)` | ツール拡張（DB, Web, GitHub, Jira等） | オープン標準規格によるシームレスな外部データ統合 |

---

## 4. Model Context Protocol (MCP) 連携実践

MCPを導入することで、エージェントに対して安全かつ標準化されたツールアクセス権限を付与できます。

### 設定例 (`mcp_config.json`)
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxxxxxxxxxx"
      }
    },
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost:5432/mydb"]
    },
    "fetch": {
      "command": "uvx",
      "args": ["mcp-server-fetch"]
    }
  }
}
```

---

## 5. 実践ワークフロー（自律開発ループ & TDD）

エージェントを自律的に動作させる際の標準ワークフローです。

```mermaid
flowchart TD
    Start([要件・Issue 受領]) --> Plan[1. 実装計画の策定<br>implementation_plan.md]
    Plan --> TestGen[2. テストケース先行作成<br>TDD / Red State]
    TestGen --> CodeGen[3. コード実装 & 編集<br>Green State を目指す]
    CodeGen --> ExecTest[4. テスト・Lint 自動実行]
    ExecTest -->|失敗| FixLoop[エラー解析 & 修正ループ]
    FixLoop --> CodeGen
    ExecTest -->|合格| Review[5. 差分レビュー &<br>walkthrough.md 作成]
    Review --> Commit([Git コミット / PR 作成])
```

### コンテキスト制御規約（`AGENTS.md` / `CLAUDE.md`）の整備
エージェントがプロジェクトの方針から逸脱しないよう、リポジトリルートに規約ファイルを配置します。
- 命名規則、使用禁止ライブラリ、テスト実行コマンドを明記。
- 参照: 本リポジトリの [AGENTS.md](../AGENTS.md)

---

## 6. 運用・コスト最適化 & ガードレール

??? tip "Prompt Caching による大幅なコスト削減と高速化"
    - **原理**: 静的なシステムプロンプトやリポジトリ規約（`AGENTS.md`）、コードベースの共通ヘッダーをキャッシュすることで、入力トークンコストを最大90%削減し、初回応答速度を大幅に引き上げます。
    - **対策**: 頻繁に変更されない規約ファイルやMCPツール定義をプロンプトの先頭に配置する。

??? warning "無限ループ防止 & 安全なガードレール"
    - エージェントの最大実行ターン数（Max Steps）を設定する。
    - 破壊的なGit操作（`git reset --hard`, `git push --force`）や外部送信コマンドに確認ステップを設ける。

---

## 7. 関連ドキュメント一覧 (Reference Index)

- 🧠 [Closed Weights (フロンティアモデル) ベンチマーク](../2_models/benchmark/Benchmark_Closed_Weights_Flash.md)
- 🧠 [推論・思考モデルの解説](../2_models/2_5_reasoning_models.md)
- 👁️ [マルチモーダルモデルの活用](../2_models/2_3_multimodal.md)
- 📋 [AI 関連技術見出し体系 (Abstract.md)](../Abstract.md)
- 📜 [執筆・運用規約 (AGENTS.md)](../AGENTS.md)
- 🏢 [M365 Copilot 実践シナリオブック (persona_m365.md)](persona_m365.md)
- 💻 [ローカルLLM 実践シナリオブック (persona_local.md)](persona_local.md)
