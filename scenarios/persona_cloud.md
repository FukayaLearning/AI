---
title: "高度クラウドエージェント環境向け活用シナリオブック"
description: "Claude Code、GitHub Copilot、Cursor、MCP等を最大限に駆使し、自律的なソフトウェア開発ループと高度エージェントワークフローを構築する実践ガイド"
target_personas:
  persona-m365: "✕"
  persona-local: "○"
  persona-cloud: "◎"
requirements:
  hardware: "一般的な開発マシン / インターネット接続"
  tools: ["Claude Code", "GitHub Copilot", "Cursor / Windsurf", "Model Context Protocol (MCP)"]
  cloud_api: "Anthropic / OpenAI / GitHub Copilot 等のAPIキーまたはサブスクリプション"
---

!!! info "対象読者ガイド"
    - 🏢 **M365 Copilot**: ✕（Office環境限定の方は [M365 Copilot シナリオブック](persona_m365.md) をご参照ください）
    - 💻 **ローカルLLM**: ○（オンプレ環境での構築は [ローカルLLM シナリオブック](persona_local.md) をご参照ください）
    - ☁️ **高度エージェント**: ◎（本シナリオブックの対象です）

---

# 高度クラウドエージェント環境向け活用シナリオブック

## 1. 前提条件 & スタック概要
- **利用可能ツール**: Claude Code, GitHub Copilot, Cursor, Windsurf, Claude 3.7 Sonnet, GPT-4o 等
- **主な特徴**:
  - フロンティアモデルの超長文コンテキストと推論時計算（Thinking）をフル活用可能
  - Model Context Protocol (MCP) によるDB・外部API・ツール群とのシームレス連携
  - 複数ターンの自律コーディングループ（SWE Loop）の実行

---

## 2. 実践ワークフロー & レシピ

### Step 1: 自律コーディングエージェント環境の構築
- Claude Code / Cursor Agent によるタスク駆動型開発ループの設定
- リポジトリ規約（`AGENTS.md`）の設計とプロンプト整合

### Step 2: Model Context Protocol (MCP) 連携
- GitHub, PostgreSQL, ファイルシステム, ブラウザ操作MCPサーバーの導入
- エージェントに対する安全なツール実行権限の付与

### Step 3: Test-Driven Development (TDD) & Loop Engineering
- エージェントによるテスト自動生成とテスト駆動での実装修正ループ
- 品質評価ベンチマークとの照合

### Step 4: Multi-Agent オーケストレーション
- プランナー・アーキテクトとコーダー・レビュアーの役割分離設計

---

## 3. ベストプラクティス & コスト・コンテキスト管理
??? tip "コンテキスト最適化 & コスト抑制"
    - **Prompt Caching**: プレフィックスキャッシュを活用し、トークンコスト削減と高速化を図る
    - **無限ループ防止**: エージェントの最大ターン数やファイル変更権限にガードレールを設ける

---

## 4. 関連ドキュメント一覧 (Reference Index)
- 🧠 [Closed Weights ベンチマーク](../models/benchmark/Benchmark_Closed_Weights.md)
- 📋 [AI 関連技術見出し体系 (Abstract.md)](../Abstract.md)
- 📜 [執筆・運用規約 (AGENTS.md)](../AGENTS.md)
