# FocusLine

日本の重要ニュースを自動追跡し、タイムラインで可視化するシステム

## 概要

FocusLineは、日本の主要ニュースサイト（NHK、Yahoo!ニュース）から自動的にニュースを収集し、AI分析により同じ出来事を追跡・集約して、わかりやすいタイムラインとして可視化するWebアプリケーションです。

## 主な機能

### バックエンド
- **自動ニュース収集**: NHK、Yahoo!ニュースJapanからRSS経由で自動収集
- **AI分析**: OpenAI GPT-4を使用した日本語記事の分析
  - 関連記事の自動クラスタリング
  - イベントの要約・説明生成
  - タイムラインエントリーの自動抽出
- **RESTful API**: FastAPIベースの高速APIサーバー
- **自動更新**: 1時間ごとの自動スクレイピング

### フロントエンド
- **イベント一覧**: 追跡中のニュースイベントを見やすく表示
- **インタラクティブタイムライン**: 時系列で出来事を可視化
- **リアルタイム更新**: 5分ごとの自動更新
- **レスポンシブデザイン**: モバイル・デスクトップ対応

## 技術スタック

### バックエンド
- Python 3.11+
- FastAPI
- SQLAlchemy (SQLite)
- OpenAI API
- BeautifulSoup4
- APScheduler

### フロントエンド
- Next.js 14
- React 18
- TypeScript
- Tailwind CSS
- Axios

## セットアップ

### 前提条件
- Python 3.11以上
- Node.js 18以上
- OpenAI APIキー（オプション、AI分析に必要）

### Docker Composeを使用する場合（推奨）

1. リポジトリをクローン:
```bash
git clone https://github.com/rakei076/FocusLine.git
cd FocusLine
```

2. 環境変数を設定:
```bash
cp .env.example .env
# .envファイルを編集してOPENAI_API_KEYを設定
```

3. Docker Composeで起動:
```bash
docker-compose up -d
```

4. アプリケーションにアクセス:
- フロントエンド: http://localhost:3000
- バックエンドAPI: http://localhost:8000
- API ドキュメント: http://localhost:8000/api/v1/docs

### 手動セットアップ

#### バックエンド

1. バックエンドディレクトリに移動:
```bash
cd backend
```

2. 仮想環境を作成:
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. 依存関係をインストール:
```bash
pip install -r requirements.txt
```

4. 環境変数を設定:
```bash
cp .env.example .env
# .envファイルを編集してOPENAI_API_KEYを設定
```

5. サーバーを起動:
```bash
cd app
python main.py
```

#### フロントエンド

1. フロントエンドディレクトリに移動:
```bash
cd frontend
```

2. 依存関係をインストール:
```bash
npm install
```

3. 環境変数を設定:
```bash
cp .env.local.example .env.local
```

4. 開発サーバーを起動:
```bash
npm run dev
```

## API エンドポイント

### イベント管理
- `GET /api/v1/events` - イベント一覧取得
  - クエリパラメータ: `status` (active/archived), `skip`, `limit`
- `GET /api/v1/events/{id}` - イベント詳細とタイムライン取得
- `PUT /api/v1/events/{id}` - イベント更新
- `POST /api/v1/scrape` - 手動スクレイピング実行

### ヘルスチェック
- `GET /` - ルートエンドポイント
- `GET /health` - ヘルスチェック

## アーキテクチャ

```
FocusLine/
├── backend/           # Pythonバックエンド
│   ├── app/
│   │   ├── api/      # APIエンドポイント
│   │   ├── core/     # 設定・データベース
│   │   ├── models/   # データモデル
│   │   ├── services/ # ビジネスロジック
│   │   └── scrapers/ # ニュースクローラー
│   └── requirements.txt
│
├── frontend/         # Next.jsフロントエンド
│   ├── src/
│   │   ├── app/      # ページとレイアウト
│   │   ├── components/ # Reactコンポーネント
│   │   ├── lib/      # ユーティリティ
│   │   └── types/    # TypeScript型定義
│   └── package.json
│
└── docker-compose.yml # Docker設定
```

## 開発

### バックエンド開発

```bash
cd backend
# 仮想環境をアクティブ化
source venv/bin/activate
# 開発サーバー起動（自動リロード有効）
cd app
uvicorn main:app --reload
```

### フロントエンド開発

```bash
cd frontend
npm run dev
```

## ライセンス

ISC

## 作者

rakei076

## 貢献

プルリクエストを歓迎します！大きな変更の場合は、まずissueを開いて変更内容を議論してください。

## 注意事項

- OpenAI APIキーがない場合、基本的なキーワードベースのクラスタリングが使用されます
- ニュースサイトの利用規約を遵守してください
- 本番環境では適切なセキュリティ設定を行ってください
