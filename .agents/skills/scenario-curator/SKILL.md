---
name: scenario-curator
description: >-
  シナリオブック（scenarios/persona_*.md）の作成・更新・再構成を行う際に使用します。
  リポジトリ内の要素技術資料（ハードウェア、モデル、量子化、ベンチマーク等）をMkDocs機能（Snippets、タブ、Admonition、相対リンク）で取り込み、
  ペルソナ（M365 / Local LLM / Cloud Agent）ごとに1本のまとまった実践ドキュメントとして再構築する手順を提供します。
---

# シナリオブック統合・構成スキル (Scenario Curator Skill)

本スキルは、`scenarios/` 配下のペルソナ別シナリオブック（`persona_m365.md`, `persona_local.md`, `persona_cloud.md`）に対して、本リポジトリ内の各要素技術資料（ハードウェア、モデルアーキテクチャ、量子化形式、ベンチマーク結果等）を適切に取り込み、GitHub Pages (MkDocs Material) 上で「1つのまとまりのある実践的読み物」として読めるように整理・構成・執筆するための標準ワークフローです。

---

## 実行ワークフロー（5ステップ）

### Step 1: 対象ペルソナとスコープの確認
編集対象のシナリオブックとペルソナ（`persona-m365`, `persona-local`, `persona-cloud`）の前提条件を確認します。
- `persona-m365`: Office/Copilot UI限定、API不可、プロンプト/データ検索中心
- `persona-local`: VRAM制約（8GB/24GB/96GB+）、Ollama/vLLM/Continue、量子化/小型思考モデル中心
- `persona-cloud`: Claude Code/Cursor/Windsurf/MCP、フロンティアモデル/エージェントループ中心

### Step 2: 取り込むリポジトリ内資料の選定
[Persona Mapping (ドキュメント対応表)](./references/persona_mapping.md) を参照し、当該ペルソナに必要なリポジトリ内のドキュメント（`1_hardware/`, `2_models/`, `11_engineering/` など）を特定します。

### Step 3: 7セクション標準構成に沿ったアウトライン設計
[Structure Templates (構成テンプレート)](./references/structure_templates.md) に基づき、シナリオを以下の7セクション構成に整理します。
1. 前提・ターゲット環境
2. ハードウェア・実行環境の選定とサイジング
3. モデル選定戦略 & ベンチマーク知見の活用
4. 開発環境・ツールのセットアップ手順
5. 実践ワークフロー & 業務別レシピ（核心部）
6. トラブルシューティング & 運用・コスト最適化
7. 関連ドキュメント一覧 (Reference Index)

### Step 4: MkDocs Material リッチUIを用いた文章統合 & 執筆
単なるリンク集やコードの貼り付けにせず、前後に文脈を説明するリード文を添えて1本のストーリーとして執筆します。
- **分岐・スペック別設定**: Content Tabs (`=== "8GB VRAM"`, `=== "24GB VRAM"`)
- **重要な注意・ガイダンス**: Admonition (`!!! info "対象読者ガイド"`, `!!! warning`)
- **詳細チューニング**: Collapsible Details (`??? tip "上級者向け設定"`)
- **フローの図解**: Mermaid ダイアグラム (`mermaid`)
- **表・データの再利用**: PyMdown Snippets (`--8<-- "パス:開始行:終了行"`)

### Step 5: リンク整合性 & ペルソナ整合性の検証
- ドキュメント間リンクがすべて `.md` 拡張子を含む相対パス（例: `[ハードウェア導入](../1_hardware/1_0_introduction.md)`）になっているか確認します。
- Frontmatter の `target_personas` や `requirements` が本文と完全に一致しているか確認します。

---

## 特化型スキル一覧 (Specialized Scenario Skills)

シナリオの作業内容や目的に応じて、以下の特化スキル（スラッシュコマンド）を使い分けることができます。

### 1. 個別シナリオ更新スキル
- 🏢 **`scenario-update-m365`**: M365 Copilot限定環境シナリオ（`scenarios/persona_m365.md`）の個別更新・プロンプト拡充
- 💻 **`scenario-update-local`**: ローカルLLM環境シナリオ（`scenarios/persona_local.md`）の個別更新・VRAM別サイジング拡充
- ☁️ **`scenario-update-cloud`**: 高度クラウドエージェント環境シナリオ（`scenarios/persona_cloud.md`）の個別更新・自律ループ/MCP拡充

### 2. 全シナリオ一括更新スキル
- 🔄 **`scenario-update-all`**: リポジトリ全体の最新知見を検知し、全ペルソナシナリオを一括同期・更新

### 3. 整合性点検・リンタースキル
- 🔍 **`scenario-lint-single`**: 指定された単一シナリオ（`persona_*.md`）の相対リンク切れ・Snippets・Frontmatterを点検
- 📋 **`scenario-lint-all`**: 全シナリオ（`scenarios/*.md`）を一括点検し、MkDocs Materialビルド適合性を検証

---

## 関連リファレンス & スクリプト
- 🗺️ [ペルソナ別ドキュメント対応マッピング](./references/persona_mapping.md)
- 📐 [シナリオ構成テンプレート & 執筆ガイド](./references/structure_templates.md)
- 🐍 [シナリオ整合性リンタースクリプト](./scripts/lint_scenarios.py)
- 📜 [リポジトリ執筆・運用規約](../../../AGENTS.md)
