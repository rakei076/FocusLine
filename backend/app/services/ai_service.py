from typing import List, Dict, Any, Optional
from datetime import datetime
import json
from openai import OpenAI
from app.core.config import settings


class AIAnalyzer:
    """AI service for analyzing Japanese news articles"""
    
    def __init__(self):
        self.client = None
        if settings.OPENAI_API_KEY:
            self.client = OpenAI(api_key=settings.OPENAI_API_KEY)
    
    async def cluster_articles(self, articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Cluster articles about the same event
        
        Args:
            articles: List of article dictionaries
            
        Returns:
            List of event clusters with associated articles
        """
        if not self.client or not articles:
            return self._fallback_clustering(articles)
        
        try:
            # Prepare article summaries for clustering
            article_summaries = [
                f"{i}. {article['title']}" 
                for i, article in enumerate(articles)
            ]
            
            prompt = f"""以下は日本のニュース記事のタイトルリストです。同じ出来事に関する記事をグループ化してください。

記事:
{chr(10).join(article_summaries[:50])}  # Limit to 50 articles

以下のJSON形式で回答してください:
{{
  "clusters": [
    {{
      "event_title": "イベントのタイトル",
      "article_indices": [0, 1, 2],
      "category": "カテゴリ"
    }}
  ]
}}
"""
            
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "あなたは日本のニュース分析の専門家です。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            
            # Build event clusters
            clusters = []
            for cluster_info in result.get('clusters', []):
                cluster_articles = [
                    articles[i] for i in cluster_info['article_indices']
                    if i < len(articles)
                ]
                if cluster_articles:
                    clusters.append({
                        'title': cluster_info['event_title'],
                        'category': cluster_info.get('category', 'その他'),
                        'articles': cluster_articles
                    })
            
            return clusters
            
        except Exception as e:
            print(f"Error in AI clustering: {e}")
            return self._fallback_clustering(articles)
    
    async def analyze_event(
        self, 
        articles: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Analyze event and extract timeline information
        
        Args:
            articles: List of articles about the same event
            
        Returns:
            Event analysis with timeline entries
        """
        if not self.client or not articles:
            return self._fallback_analysis(articles)
        
        try:
            # Prepare article content
            article_texts = []
            for i, article in enumerate(articles[:10]):  # Limit to 10 articles
                article_texts.append(
                    f"記事{i+1}:\n"
                    f"タイトル: {article['title']}\n"
                    f"内容: {article.get('content', '')[:500]}\n"
                    f"ソース: {article.get('source', '')}\n"
                )
            
            prompt = f"""以下の記事は同じニュースイベントに関するものです。分析して以下の情報を抽出してください:

{chr(10).join(article_texts)}

以下のJSON形式で回答してください:
{{
  "summary": "イベントの要約（200文字以内）",
  "description": "イベントの詳細説明（500文字以内）",
  "timeline": [
    {{
      "timestamp": "YYYY-MM-DD HH:MM:SS",
      "title": "出来事のタイトル",
      "description": "出来事の説明"
    }}
  ]
}}

タイムラインには、記事から抽出できる時系列の出来事を含めてください。
"""
            
            response = self.client.chat.completions.create(
                model=settings.OPENAI_MODEL,
                messages=[
                    {"role": "system", "content": "あなたは日本のニュース分析とタイムライン生成の専門家です。"},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            return result
            
        except Exception as e:
            print(f"Error in AI analysis: {e}")
            return self._fallback_analysis(articles)
    
    def _fallback_clustering(self, articles: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """Simple keyword-based clustering when AI is not available"""
        # Group by similar keywords in titles
        clusters = {}
        
        for article in articles:
            title = article.get('title', '')
            # Simple clustering: use first 3 words as key
            words = title.split()[:3]
            key = ' '.join(words) if words else title[:20]
            
            if key not in clusters:
                clusters[key] = {
                    'title': title,
                    'category': 'ニュース',
                    'articles': []
                }
            clusters[key]['articles'].append(article)
        
        # Filter clusters with at least 2 articles
        return [
            cluster for cluster in clusters.values()
            if len(cluster['articles']) >= 2
        ]
    
    def _fallback_analysis(self, articles: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Simple analysis when AI is not available"""
        if not articles:
            return {
                'summary': '',
                'description': '',
                'timeline': []
            }
        
        # Use first article's title and content
        first_article = articles[0]
        
        timeline = []
        for article in articles[:5]:
            timeline.append({
                'timestamp': article.get('published_at', datetime.utcnow()).strftime('%Y-%m-%d %H:%M:%S'),
                'title': article['title'],
                'description': article.get('content', '')[:200]
            })
        
        return {
            'summary': first_article['title'],
            'description': first_article.get('content', '')[:500],
            'timeline': timeline
        }


ai_analyzer = AIAnalyzer()
