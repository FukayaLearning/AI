---
name: scenario-lint-single
description: >-
  指定された単一のペルソナシナリオ（例: scenarios/persona_local.md）に対して、
  相対リンク切れ、PyMdown Snippetsパス・行範囲、YAML Frontmatter、Admonition構文を点検・検証・自動修正するスキル。
---

# 単一シナリオ整合性点検スキル (Scenario Lint: Single)

本スキルは、指定された **1つのシナリオファイル（`scenarios/persona_*.md`）** に対し、MkDocs Materialビルド互換性、相対リンクの正当性、PyMdown Snippetsの埋め込み範囲、Frontmatterのメタデータ整合性を検証・自動修正するためのツールです。

---

## 点検対象チェック項目

1. **ドキュメント間リンク (Cross-Document Links)**:
   - 相対リンクのターゲットファイルが存在するか
   - Markdownファイルへのリンクが `.md` 拡張子を含んでいるか（例: `[タイトル](../2_models/2_0_introduction.md)`）
   - アンカー付きリンク（`#heading-id`）が壊れていないか
2. **コンテンツ埋め込み (PyMdown Snippets)**:
   - `--8<-- "path"` で参照されているファイルが存在するか
   - 行範囲指定（`path:start:end`）が実ファイルの行数を超えていないか
3. **YAML Frontmatter & 対象読者ガイド**:
   - `title`, `description`, `target_personas`, `requirements` が正しく定義されているか
   - `!!! info "対象読者ガイド"` のAdmonitionとFrontmatterの判定が一致しているか
4. **MkDocs Material UI 構文**:
   - Content Tabs (`=== "..."`) のインデントが4スペースで正しく揃っているか
   - Collapsible Details (`??? tip "..."`) の構文が有効か

---

## 実行コマンド

単一ファイルを指定してリンタースクリプトを実行します：

```bash
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/<対象ファイル名>.md
```

### 例
```bash
# ローカルLLMシナリオの点検
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/persona_local.md

# M365 Copilotシナリオの点検
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/persona_m365.md

# 高度クラウドエージェントシナリオの点検
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/persona_cloud.md
```

---

## 修正ワークフロー
1. スクリプト出力の `🔴 Errors` および `🟡 Warnings` を確認します。
2. リンク切れの場合は、移動・改名された最新のMarkdownファイルパスに更新します。
3. Snippetsの行数オーバーの場合は、対象ファイルの行数を再確認して範囲を更新します。
4. 再度コマンドを実行し、`✅ All links, snippets, and frontmatter are valid!` が出力されることを確認します。
