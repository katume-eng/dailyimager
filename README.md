# 思い出再現 AI⽇記写真レイアウトジェネレーター

> Upload ✍️ **日記テキスト** + 📷 **写真** →  
> AI が文脈・感情に合わせたレイアウトを自動生成し、PNG / PDF アルバムを出力する Django アプリ

---

## 📚 Table of Contents
1. [背景](#背景)  
2. [主な機能](#主な機能)  
3. [技術スタック](#技術スタック)  
4. [ローカル環境セットアップ](#ローカル環境セットアップ)  
5. [使い方](#使い方)  
6. [ディレクトリ構成](#ディレクトリ構成)  
7. [今後のロードマップ](#今後のロードマップ)  
8. [ライセンス](#ライセンス)

---

## 背景
日記と写真の「並べ替え」や「デザイン調整」は時間がかかりがちです。本アプリは AI (LLM) と画像処理 (Pillow) を組み合わせ、  
**➀ 文脈を汲み取る** → **➁ 最適レイアウトを提案** → **➂ 高画質で書き出し**  
という流れをワンクリックで実現します。お気に入りレイアウトを学習するため、使うほど “あなたらしい” アルバムに進化します。

---

## 主な機能
|分類|機能|概要|
|---|---|---|
|ユーザー管理|登録 / ログイン|Django 認証 (E-mail / SNS)|
|アップロード|日記+写真投稿|複数画像と txt / md / rtf 等|
|レイアウト生成|AI レイアウトエンジン|感情分析 + Pillow で自動合成|
|出力|PNG / PDF 生成|1080p 相当の PNG と A4 PDF|
|テンプレート管理|フォント / カラーパターン編集|Django Admin|
|学習|お気に入りレイアウト蓄積|協調フィルタリングで個別化|
|再生成|ワンクリックで再レイアウト|納得いくまでリロード可|

---

## 技術スタック
- **Backend**: Django 5.x + Django REST Framework  
- **AI/ML**: OpenAI API (GPT-4o) / LangChain  
- **画像処理**: Pillow, ReportLab (PDF)  
- **DB**: SQLite (dev) / PostgreSQL (prod)  
- **非同期**: Celery + Redis (任意)  
- **インフラ**: Docker / docker-compose, GitHub Actions CI

---

## ローカル環境セットアップ

```bash
# 1. リポジトリ取得
git clone https://github.com/yourname/omoide-layout-ai.git
cd omoide-layout-ai

# 2. 仮想環境
python -m venv venv
source venv/bin/activate      # Windows の場合: .\venv\Scripts\activate

# 3. 依存関係
pip install -r requirements.txt

# 4. 環境変数 (.env) 作成
cp .env.example .env          # OPENAI_API_KEY, DEBUG などを設定

# 5. DB 初期化
python manage.py migrate
python manage.py createsuperuser

# 6. 開発サーバ
python manage.py runserver
