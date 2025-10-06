# FocusLine 開発ガイド

## システム概要

FocusLineは、日本の主要ニュースを自動収集し、AI分析で関連記事を集約してタイムライン形式で表示するシステムです。

## アーキテクチャ

### バックエンド (Python/FastAPI)

#### コンポーネント

1. **Scrapers** (`app/scrapers/`)
   - `base.py`: スクレイパーの基底クラス
   - `nhk_scraper.py`: NHKニュースのRSSスクレイパー
   - `yahoo_scraper.py`: Yahoo!ニュースのRSSスクレイパー
   - `manager.py`: スクレイパーの統合管理

2. **AI Service** (`app/services/ai_service.py`)
   - OpenAI GPT-4を使用した日本語記事分析
   - 記事のクラスタリング（同じ出来事の判定）
   - イベント要約の生成
   - タイムラインエントリーの抽出

3. **News Service** (`app/services/news_service.py`)
   - スクレイピングと処理の統合
   - イベントとタイムラインの管理
   - データベース操作

4. **API** (`app/api/endpoints.py`)
   - RESTful APIエンドポイント
   - イベント一覧・詳細取得
   - 手動スクレイピング実行

5. **Scheduler** (`app/core/scheduler.py`)
   - 1時間ごとの自動スクレイピング
   - APSchedulerを使用

6. **Models** (`app/models/`)
   - SQLAlchemyモデル定義
   - Pydanticスキーマ定義

### フロントエンド (Next.js/React)

#### コンポーネント

1. **Pages**
   - `app/page.tsx`: ホームページ（イベント一覧）
   - `app/events/[id]/page.tsx`: イベント詳細ページ

2. **Components**
   - `EventCard.tsx`: イベントカード
   - `Timeline.tsx`: インタラクティブタイムライン
   - `Header.tsx`: ヘッダーナビゲーション

3. **Utilities**
   - `lib/api.ts`: APIクライアント
   - `lib/utils.ts`: 日付フォーマットなどのユーティリティ

## データフロー

```
1. Scheduler (1時間ごと)
   ↓
2. Scrapers → 記事を収集
   ↓
3. Database → 記事を保存
   ↓
4. AI Service → 記事をクラスタリング・分析
   ↓
5. Database → イベントとタイムラインを保存
   ↓
6. API → フロントエンドに提供
   ↓
7. Frontend → ユーザーに表示
```

## 開発環境のセットアップ

### バックエンド開発

```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 環境変数を設定
cp .env.example .env
# .envファイルを編集

# 開発サーバー起動
cd app
uvicorn main:app --reload
```

### フロントエンド開発

```bash
cd frontend
npm install

# 環境変数を設定
cp .env.local.example .env.local

# 開発サーバー起動
npm run dev
```

## テスト

### バックエンドAPI テスト

```bash
# ヘルスチェック
curl http://localhost:8000/health

# イベント一覧取得
curl http://localhost:8000/api/v1/events

# 手動スクレイピング
curl -X POST http://localhost:8000/api/v1/scrape

# イベント詳細取得
curl http://localhost:8000/api/v1/events/1
```

### データベース確認

```bash
cd backend
sqlite3 focusline.db

# SQLiteプロンプトで
.tables
SELECT * FROM events;
SELECT * FROM timeline_entries;
SELECT * FROM articles;
```

## カスタマイズ

### 新しいニュースソースの追加

1. `backend/app/scrapers/` に新しいスクレイパーを作成
2. `BaseScraper` を継承
3. `scrape()` メソッドを実装
4. `manager.py` に追加

例:
```python
from app.scrapers.base import BaseScraper

class NewSourceScraper(BaseScraper):
    async def scrape(self):
        # スクレイピングロジック
        return articles
```

### AI分析のカスタマイズ

`backend/app/services/ai_service.py` のプロンプトを編集:
- `cluster_articles()`: クラスタリングのプロンプト
- `analyze_event()`: イベント分析のプロンプト

### UIのカスタマイズ

- `frontend/src/app/globals.css`: グローバルスタイル
- `frontend/tailwind.config.js`: Tailwind設定
- `frontend/src/components/`: コンポーネントのスタイル

## デプロイ

### Docker Compose (推奨)

```bash
# 本番環境用
docker-compose up -d

# ログ確認
docker-compose logs -f

# 停止
docker-compose down
```

### 個別デプロイ

#### バックエンド
```bash
cd backend
pip install -r requirements.txt
cd app
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### フロントエンド
```bash
cd frontend
npm install
npm run build
npm start
```

## トラブルシューティング

### スクレイピングが動作しない

1. インターネット接続を確認
2. ニュースサイトがアクセス可能か確認
3. User-Agentの設定を確認（`backend/app/core/config.py`）

### AI分析が動作しない

1. OPENAI_API_KEYが設定されているか確認
2. OpenAI APIの利用可能状態を確認
3. フォールバック処理が動作（基本的なキーワードマッチング）

### データベースエラー

```bash
# データベースを削除して再作成
cd backend
rm focusline.db
python -c "from app.core.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

## パフォーマンス最適化

### バックエンド

1. **データベース最適化**
   - インデックスの追加
   - 古い記事の定期削除

2. **スクレイピング最適化**
   - 並列処理の導入
   - キャッシュの活用

### フロントエンド

1. **画像最適化**
   - Next.js Image コンポーネントの使用

2. **ページング**
   - 大量イベントの分割表示

## セキュリティ

### 本番環境での注意事項

1. **環境変数**
   - 機密情報を `.env` に保存
   - `.env` をバージョン管理から除外

2. **CORS設定**
   - `backend/app/main.py` で許可オリジンを制限

3. **API制限**
   - レート制限の実装
   - 認証の追加

## ライセンス

ISC
