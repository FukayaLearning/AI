---
name: scenario-update-cloud
description: >-
  高度クラウドエージェント環境向けシナリオブック（scenarios/persona_cloud.md）を更新・再構成するスキル。
  Claude Code、Cursor、Windsurf、MCP（Model Context Protocol）、自律型エージェントループ（SWE-Agent）、Thinkingモデル活用を執筆・整備します。
---

# 高度クラウドエージェント シナリオ更新スキル (Scenario Update: Cloud Agent)

本スキルは、**高度クラウドエージェント環境（`persona-cloud`）** 向けのシナリオブック（`scenarios/persona_cloud.md`）を個別に更新・洗練・再構成するための専用ワークフローです。

---

## ターゲットペルソナの特性・前提制約
- **対象環境**: Claude Code, GitHub Copilot, Cursor, Windsurf, OpenAI / Anthropic / Google Cloud API
- **制約条件**:
  - 原則としてモデル知能やツールの制約なし（最先端フロンティアモデルをフル活用）
  - API利用従量課金、Rate Limit、コンテキスト長とPrompt Cachingのコスト最適化への配慮が必要
  - 自律エージェントのループによる意図しないファイル破壊や無限ループの防止
- **主目的**:
  - 最先端フロンティアモデル（Claude 3.7 Sonnet, GPT-4o, Gemini 2.0 Flash）の選定とThinking/推論モードの最適化
  - 自律型コーディングエージェント（Claude Code / Cursor Agent Mode）での仕様策定〜実装〜テスト自動化ループ
  - MCP（Model Context Protocol）によるローカルツール、DB、外部Web APIのセキュアな拡張
  - Rules (`.cursorrules`, `CLAUDE.md`, `AGENTS.md`) や Skills によるコンテキスト制御

---

## 参照・取り込み推奨ドキュメント
シナリオ更新時は、リポジトリ内の以下の資料や知見を取り込み・参照してください。
- [ペルソナ対応マッピング](../scenario-curator/references/persona_mapping.md)
- [フロンティアモデル比較](../../../2_models/benchmark/Benchmark_Closed_Weights_Flash.md)（Coding, Reasoning, 速度, コスト比較）
- [推論・思考モデル](../../../2_models/2_5_reasoning_models.md)（Extended Thinkingの使い分け）
- [マルチモーダルモデル](../../../2_models/2_3_multimodal.md)（UIデザイン・画像入力タスク）
- [エージェントエンジニアリング](../../../11_engineering/)（MCP、自律ループ、Prompt Caching）

---

## 執筆・更新ワークフロー

### 1. 対象ファイルの確認
- 編集対象: `scenarios/persona_cloud.md`
- Frontmatter および Admonition を確認：
  ```markdown
  ---
  title: "高度クラウドエージェント 実践開発シナリオブック"
  description: "Claude Code / Cursor / MCP を駆使した自律型エージェントループと最先端モデル活用の実践ガイド"
  target_personas:
    persona-m365: "✕"
    persona-local: "○"
    persona-cloud: "◎"
  requirements:
    environment: "クラウドAPI (Anthropic / OpenAI / Google) または Pro/Max サブスクリプション"
    tools: ["Claude Code", "Cursor / Windsurf", "MCP Servers", "Git"]
  ---

  !!! info "対象読者ガイド: 高度クラウドエージェント環境"
      - 🏢 **M365 Copilot**: ✕（自律開発ツール・CLI操作が必要なため対象外）
      - 💻 **ローカルLLM**: ○（クラウドエージェントとのハイブリッド運用として参考に可能）
      - ☁️ **高度クラウドエージェント**: ◎（自律ループ・MCP・最新フロンティアモデル連携を完全網羅）
  ```

### 2. 7セクション標準構成に沿った更新
1. **前提・ターゲット環境**: 最先端API・ツールの前提、自律エージェントの目的
2. **モデル選定戦略 & 推論モード使い分け**:
   - 超高速・軽量タスク: Gemini 2.0 Flash / GPT-4o mini
   - 高度設計・難関実装・コードレビュー: Claude 3.7 Sonnet (Extended Thinking)
3. **エージェントツールスタック選定**: Claude Code (CLI自律型), Cursor / Windsurf (IDE統合型) の比較と使い分け
4. **MCP（Model Context Protocol）連携実践**: GitHub MCP, PostgreSQL/SQLite MCP, Fetch MCP 等の設定例 (`mcp_config.json`)
5. **実践ワークフロー（自律開発ループ & レシピ）**:
   - `Issue / 要件定義` → `Plan (実装計画)` → `Execute (TDD / 自動編集)` → `Verify (テスト・Lint実行)` の一連ループ（Mermaid図で視覚化）
   - コンテキスト制御ファイル（`AGENTS.md`, `CLAUDE.md`, `.cursorrules`）の設計
6. **運用・コスト最適化 & ガードレール**: Prompt Cachingの活用、無限ループ防止、Gitブランチ戦略
7. **関連ドキュメント一覧 (Reference Index)**: リポジトリ内リンク（`.md` 拡張子付き相対パス）

### 3. 整合性チェック
更新後、リンタースクリプトで整合性を確認します：
```bash
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/persona_cloud.md
```
