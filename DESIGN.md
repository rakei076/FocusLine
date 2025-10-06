# FocusLine - Visual Design Specification

## Color Palette

### Primary Colors
- Blue: `#3B82F6` (Primary action, links)
- White: `#FFFFFF` (Background)
- Gray: `#F9FAFB` to `#111827` (Text, borders)

### Category Colors
- 政治 (Politics): Red `#FEE2E2` / `#991B1B`
- 経済 (Economy): Blue `#DBEAFE` / `#1E3A8A`
- 社会 (Social): Green `#D1FAE5` / `#065F46`
- スポーツ (Sports): Yellow `#FEF3C7` / `#92400E`
- エンタメ (Entertainment): Purple `#EDE9FE` / `#5B21B6`
- 国際 (International): Indigo `#E0E7FF` / `#3730A3`

## Homepage Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  ┌─────┐ FocusLine                          ホーム    API        │
│  │ ⚡  │                                                         │
│  └─────┘                                                         │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  追跡中のニュースイベント                    [今すぐ更新 🔄]     │
│  日本の主要ニュースを自動収集し、タイムラインで追跡しています     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────┐
│ 重要な政治ニュース    │ │ 経済動向について     │ │ スポーツイベント  │
│ [政治]              │ │ [経済]             │ │ [スポーツ]      │
│                     │ │                    │ │                 │
│ このイベントの要約    │ │ このイベントの要約   │ │ このイベントの要約│
│ が表示されます...    │ │ が表示されます...   │ │ が表示されます... │
│                     │ │                    │ │                 │
│ 🕒 2時間前          │ │ 🕒 5時間前         │ │ 🕒 1日前        │
│ 📋 12 件の出来事    │ │ 📋 8 件の出来事    │ │ 📋 15 件の出来事│
└─────────────────────┘ └─────────────────────┘ └─────────────────┘

┌─────────────────────┐ ┌─────────────────────┐ ┌─────────────────┐
│ 国際ニュース         │ │ 技術革新について     │ │ その他のニュース  │
│ [国際]             │ │ [IT]               │ │ [その他]        │
│                     │ │                    │ │                 │
│ ...                │ │ ...                │ │ ...             │
└─────────────────────┘ └─────────────────────┘ └─────────────────┘
```

## Event Detail Page Layout

```
┌─────────────────────────────────────────────────────────────────┐
│  ┌─────┐ FocusLine                          ホーム    API        │
│  │ ⚡  │                                                         │
│  └─────┘                                                         │
└─────────────────────────────────────────────────────────────────┘

  ← イベント一覧に戻る

┌─────────────────────────────────────────────────────────────────┐
│  重要な政治ニュースイベント                           [政治]      │
│                                                                 │
│  このイベントの要約が表示されます。主要なポイントを簡潔に説明。   │
│                                                                 │
│  このイベントの詳細説明が表示されます。背景や経緯、現在の状況    │
│  などをより詳しく説明します。                                   │
│                                                                 │
│  🕒 最初の報道: 2日前    🔄 最終更新: 2時間前    📋 12 件の出来事│
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│  🕒 タイムライン                                                 │
│                                                                 │
│  ●─────────────────────────────────────────────────────────────│
│  │  ┌──────────────────────────────────────────────────────┐   │
│  │  │ 最新の展開                               [nhk]        │  │
│  │  │ 🕒 2024年1月1日 15時00分                              │  │
│  │  │                                                       │  │
│  │  │ 最新の出来事の詳細な説明がここに表示されます。        │  │
│  │  │                                                       │  │
│  │  │ 記事を読む →                                          │  │
│  │  └──────────────────────────────────────────────────────┘   │
│  │                                                             │
│  ●─────────────────────────────────────────────────────────────│
│  │  ┌──────────────────────────────────────────────────────┐   │
│  │  │ 政府が対応を発表                         [yahoo]      │  │
│  │  │ 🕒 2024年1月1日 12時00分                              │  │
│  │  │                                                       │  │
│  │  │ 政府の対応についての詳細...                           │  │
│  │  │                                                       │  │
│  │  │ 記事を読む →                                          │  │
│  │  └──────────────────────────────────────────────────────┘   │
│  │                                                             │
│  ●─────────────────────────────────────────────────────────────│
│  │  ┌──────────────────────────────────────────────────────┐   │
│  │  │ 事件が発生                               [nhk]        │  │
│  │  │ 🕒 2024年1月1日 10時00分                              │  │
│  │  │                                                       │  │
│  │  │ 事件発生時の詳細な状況...                            │  │
│  │  │                                                       │  │
│  │  │ 記事を読む →                                          │  │
│  │  └──────────────────────────────────────────────────────┘   │
│  │                                                             │
└─────────────────────────────────────────────────────────────────┘
```

## Component Specifications

### EventCard Component

**Dimensions:**
- Width: Flexible (grid-based)
- Padding: 24px
- Border: 1px solid #E5E7EB
- Border Radius: 8px
- Shadow: Hover effect

**Typography:**
- Title: 20px, bold, #111827
- Summary: 16px, regular, #4B5563
- Metadata: 14px, regular, #6B7280

**Interactive States:**
- Default: White background
- Hover: Shadow increases, slight scale
- Active: Blue border

### Timeline Component

**Dimensions:**
- Timeline Line: 2px width, #E5E7EB
- Timeline Dot: 32px diameter, #3B82F6
- Entry Card: Full width, 24px padding

**Typography:**
- Entry Title: 18px, semibold, #111827
- Timestamp: 14px, regular, #6B7280
- Description: 16px, regular, #374151

**Spacing:**
- Between entries: 32px
- Left margin for content: 48px

### Header Component

**Dimensions:**
- Height: 64px
- Logo: 40px × 40px
- Padding: 16px

**Typography:**
- Brand Name: 24px, bold, #111827
- Navigation: 16px, medium, #374151

## Responsive Breakpoints

```css
/* Mobile */
@media (max-width: 640px) {
  /* Single column layout */
  /* Stack timeline entries */
}

/* Tablet */
@media (min-width: 641px) and (max-width: 1024px) {
  /* 2-column grid for events */
}

/* Desktop */
@media (min-width: 1025px) {
  /* 3-column grid for events */
}
```

## Animations

### Loading State
- Spinner: 48px diameter, rotating animation
- Duration: Continuous until loaded

### Hover Effects
- EventCard: 0.2s ease transition
- Buttons: 0.15s ease transition
- Timeline entries: 0.2s ease shadow

### Transitions
- Page load: Fade in 0.3s
- Event list: Stagger animation 0.1s per item

## Icons

All icons use Heroicons (outline style):
- Clock: Timeline timestamps
- Document: Entry count
- Refresh: Update button
- External link: Article links
- Lightning bolt: Logo
- Arrow: Navigation

## Accessibility

- All colors meet WCAG 2.1 AA contrast requirements
- Focus indicators on all interactive elements
- ARIA labels on icon-only buttons
- Semantic HTML structure
- Keyboard navigation support
