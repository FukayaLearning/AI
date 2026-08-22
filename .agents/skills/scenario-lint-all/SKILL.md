---
name: scenario-lint-all
description: >-
  全ペルソナシナリオ（scenarios/*.md）およびリポジトリ全体のドキュメントに対して、
  相対リンク切れ、PyMdown Snippetsパス、Frontmatter、MkDocs Materialビルド適合性を一括点検・検証レポートを作成するスキル。
---

# 全シナリオ一括点検・整合性チェックスキル (Scenario Lint: All)

本スキルは、`scenarios/` 配下の **すべてのシナリオファイル** を一括スキャンし、MkDocs Materialビルド互換性、相対リンク切れ、PyMdown Snippetsの埋め込みパス、YAML Frontmatterの整合性を検証・自動修正・レポート作成するための総合ツールです。

---

## 点検対象チェック項目

1. **全シナリオの相対リンク網羅点検**:
   - リポジトリ内のすべてのリンク（`1_hardware/`, `2_models/`, `11_engineering/` 等への参照）が実在し、`.md` 拡張子を含んでいるか
2. **PyMdown Snippets（`--8<--`）の一括検証**:
   - 参照ファイルパスが実在し、指定行範囲がはみ出していないか
3. **YAML Frontmatter の統一性**:
   - `target_personas`（`persona-m365`, `persona-local`, `persona-cloud`）のキーがすべてのファイルで漏れなく揃っているか
4. **MkDocs Material UI / ビルド適合性**:
   - Content Tabs, Admonition, Mermaid 図の構文エラーがないか

---

## 実行コマンド

全シナリオファイルを一括点検します：

```bash
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --all
```

---

## 実行結果と判定
- **✅ すべてパスした場合**:
  ```text
  Summary: 3 file(s) checked | 0 Error(s) | 0 Warning(s)
  ```
  GitHub Pages / MkDocs `--strict` ビルドが安全に成功する状態です。
- **🔴 エラーまたは 🟡 警告が検出された場合**:
  エラー一覧を確認し、該当ファイルの相対リンクパス・Snippets範囲・Frontmatterを修正後、再実行して検証を完了させてください。
