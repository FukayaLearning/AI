---
name: scenario-update-all
description: >-
  リポジトリ内の全ペルソナシナリオ（M365 / Local LLM / Cloud Agent）を一括して更新・同期・再構成するスキル。
  ハードウェア、モデル、量子化、ベンチマーク等の最新知見を各シナリオブックに抜け漏れなく反映します。
---

# 全ペルソナシナリオ一括更新スキル (Scenario Update: All Personas)

本スキルは、`scenarios/` 配下の **すべてのペルソナシナリオブック（`persona_m365.md`, `persona_local.md`, `persona_cloud.md`）** をリポジトリの最新状態に合わせて一括更新・同期・体系化するための総合ワークフローです。

---

## 実行ワークフロー（4ステップ）

### Step 1: リポジトリ全体の変更点・最新ドキュメントの収集
1. `1_hardware/`, `2_models/`, `11_engineering/` 配下の最新ファイルを走査・確認します。
2. [Persona Mapping (ドキュメント対応表)](../scenario-curator/references/persona_mapping.md) を参照し、各シナリオに反映すべき最新の知見（新ベンチマークグラフ、新しいモデル形式、MCP等の技術）を整理します。

### Step 2: 3つのシナリオを順次更新
各シナリオブックを以下の役割分担に従って更新します。

1. **`scenarios/persona_m365.md`**:
   - M365 Copilot限定環境のOfficeアプリ（Word/Excel/PowerPoint/Teams）連携、プロンプト、社内ナレッジ検索を更新。
   - 参照: [scenario-update-m365](../scenario-update-m365/SKILL.md)
2. **`scenarios/persona_local.md`**:
   - VRAM別サイジング（8GB/24GB/96GB+）、モデル選定（Qwen/Llama/DeepSeek）、Ollama/Continue連携を更新。
   - 参照: [scenario-update-local](../scenario-update-local/SKILL.md)
3. **`scenarios/persona_cloud.md`**:
   - Claude Code / Cursor / Windsurf / MCP / 自律エージェントループ / Thinkingモデル活用を更新。
   - 参照: [scenario-update-cloud](../scenario-update-cloud/SKILL.md)

### Step 3: 共通トーン & MkDocs Material UI の標準化
- すべてのシナリオが [Structure Templates (構成テンプレート)](../scenario-curator/references/structure_templates.md) の7セクション構成に準拠しているか確認。
- Content Tabs (`=== "..."`)、Admonition (`!!! info` 等)、Collapsible Details (`??? tip` 等)、Mermaid図が適切に活用されているか確認。

### Step 4: 全体整合性・リントの実行
更新完了後、全シナリオに対して一括整合性チェックを実行します：
```bash
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --all
```
エラーや警告がゼロになるまでリンク・Snippetsを修正します。
