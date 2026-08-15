---
title: "M365 Copilot 限定環境向け活用シナリオブック"
description: "IDE統合や外部API利用が制限された企業環境で、Microsoft 365 Copilot等を最大限に活用するための実践ガイド"
target_personas:
  persona-m365: "◎"
  persona-local: "✕"
  persona-cloud: "△"
requirements:
  hardware: "一般的なPC / ブラウザ環境"
  tools: ["Microsoft 365 Copilot", "Teams / Word / Excel / PowerPoint"]
  cloud_api: "M365ライセンスに含まれるCopilot機能"
---

!!! info "対象読者ガイド"
    - 🏢 **M365 Copilot**: ◎（本シナリオブックの対象です）
    - 💻 **ローカルLLM**: ✕（ローカル推論環境をお持ちの方は [ローカルLLM シナリオブック](persona_local.md) をご参照ください）
    - ☁️ **高度エージェント**: △（クラウドIDEエージェント環境をお持ちの方は [高度クラウドエージェント シナリオブック](persona_cloud.md) をご参照ください）

---

# M365 Copilot 限定環境向け活用シナリオブック

## 1. 前提条件 & 環境制約
- **利用可能ツール**: Microsoft 365 Copilot (Office各アプリ内, Teams, Copilot Chat)
- **主な制約**:
  - IDE（VS Code等）との直接連携は不可
  - ローカルモデルや未認可の外部API呼び出しは不可
  - 企業セキュリティポリシーおよびテナント内データ保護が適用

---

## 2. 実践ワークフロー & レシピ

### Step 1: Office アプリケーション連携・プロンプト技術
- Wordでの仕様書・ドキュメント骨子生成
- Excelでのデータ抽出・簡易集計支援
- PowerPointでの構成案・プレゼン資料ドラフト化

### Step 2: 会議・コミュニケーション支援
- Teams 会議文字起こしからの自動議事録・アクションアイテム抽出
- 長文メールスレッドの要約と返信ドラフト作成

### Step 3: 社内ナレッジ・Graph 検索の最大活用
- SharePoint / OneDrive 内ドキュメントを横断した情報探索
- 関連ドキュメントを明示的にコンテキスト指定するプロンプティング手法

---

## 3. トラブルシューティング & Tips
??? warning "ハルシネーションの抑制と精度向上"
    - 参照ドキュメント（SharePointファイル名）を明示的に指定する
    - 回答のフォーマットや出力構造を箇条書き等でステップバイステップ指示する

---

## 4. 関連ドキュメント一覧 (Reference Index)
- 📋 [AI 関連技術見出し体系 (Abstract.md)](../Abstract.md)
- 📜 [執筆・運用規約 (AGENTS.md)](../AGENTS.md)
