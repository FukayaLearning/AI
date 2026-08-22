---
name: scenario-update-m365
description: >-
  M365 Copilot限定環境向けシナリオブック（scenarios/persona_m365.md）を更新・再構成するスキル。
  Officeアプリ（Word/Excel/PowerPoint/Teams）連携、プロンプト技術、社内ナレッジ検索、制約回避策の実践ガイドを執筆・整備します。
---

# M365 Copilot シナリオ更新スキル (Scenario Update: M365)

本スキルは、**M365 Copilot 限定環境（`persona-m365`）** 向けのシナリオブック（`scenarios/persona_m365.md`）を個別に更新・洗練・再構成するための専用ワークフローです。

---

## ターゲットペルソナの特性・前提制約
- **対象環境**: Microsoft 365 Copilot (Enterprise / Business), Webチャット (Copilot / ChatGPT Enterprise 等)
- **制約条件**:
  - IDEやローカル推論環境、自作スクリプト、CLIツールの実行は不可
  - 外部API直接呼び出し不可（企業ポリシー・ネットワーク制限）
  - 社内ガバナンス・機密保護（Commercial Data Protection）下での運用
- **主目的**:
  - Word, Excel, PowerPoint, Teams, OneNote での日常業務自動化・高品質ドラフト作成
  - 社内SharePoint / メール / 会議トランスクリプトを対象としたナレッジ検索・グラウンディング
  - ロール・コンテキスト・制約条件を明示した実用プロンプトテンプレートの提供

---

## 参照・取り込み推奨ドキュメント
シナリオ更新時は、リポジトリ内の以下の資料や知見を取り込み・参照してください。
- [ペルソナ対応マッピング](../scenario-curator/references/persona_mapping.md)
- [フロンティアモデル比較](../../../2_models/benchmark/Benchmark_Closed_Weights_Flash.md)（Copilotの背後にあるGPT/フロンティアモデルの推論特性や思考パターンの解説に活用）
- [プロンプト・エンジニアリング知見](../../../11_engineering/)（Officeアプリへのグラウンディング指示プロンプトの構成）

---

## 執筆・更新ワークフロー

### 1. 対象ファイルの確認
- 編集対象: `scenarios/persona_m365.md`
- Frontmatter および Admonition を確認：
  ```markdown
  ---
  title: "M365 Copilot 実践活用シナリオブック"
  description: "Microsoft 365 Copilot環境に最適化された業務自動化・プロンプト・社内ナレッジ検索の実践ガイド"
  target_personas:
    persona-m365: "◎"
    persona-local: "✕"
    persona-cloud: "✕"
  requirements:
    environment: "Microsoft 365 Copilot ライセンス / Webチャット"
    tools: ["Word", "Excel", "PowerPoint", "Teams", "SharePoint"]
  ---

  !!! info "対象読者ガイド: M365 Copilot 限定環境"
      - 🏢 **M365 Copilot**: ◎（Officeアプリ連携・社内検索の実践ワークフローを網羅）
      - 💻 **ローカルLLM**: ✕（ローカル推論・IDE等は扱いません）
      - ☁️ **高度クラウドエージェント**: ✕（外部APIや自律ループ等は扱いません）
  ```

### 2. 7セクション標準構成に沿った更新
1. **前提・ターゲット環境**: 企業ポリシー・利用可能ツールの明確化
2. **モデル特性・動作原理**: Copilot（フロンティアモデル）の強みとプロンプト応答特性
3. **Officeアプリ別 実践レシピ**:
   - **Word**: 長文企画書ドラフト、スタイル指定推敲、要約
   - **Excel**: 計算式生成、データ傾向分析、Python in Excel（利用可能な場合）
   - **PowerPoint**: アウトラインからのスライド構成生成、トーン＆マナー統一
   - **Teams / Outlook**: 会議文字起こしからの議事録・決定事項・Action Items抽出、メールスレッド要約
4. **社内ナレッジ検索（グラウンディング）テクニック**: SharePointファイル参照、検索ノイズを減らす命名・フォルダ構成のコツ
5. **プロンプトテンプレート集**: ロール・コンテキスト・出力フォーマット・制約条件（Constraints）を網羅したコピペ可能テンプレート
6. **トラブルシューティング & 限界と回避策**: ハルシネーション対策、参照ファイル認識失敗時の対処
7. **関連ドキュメント一覧 (Reference Index)**: リポジトリ内リンク（`.md` 拡張子付き相対パス）

### 3. 整合性チェック
更新後、リンタースクリプトで整合性を確認します：
```bash
python3 .agents/skills/scenario-curator/scripts/lint_scenarios.py --file scenarios/persona_m365.md
```
