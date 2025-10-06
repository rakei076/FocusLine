# FocusLine Frontend

This is the frontend application for FocusLine, built with Next.js 14, React, and TypeScript.

## Features

- Event list page with auto-refresh
- Interactive timeline detail view
- Real-time news updates
- Responsive design with Tailwind CSS
- Japanese language support

## Setup

1. Install dependencies:
```bash
npm install
```

2. Create `.env.local` file:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000/api/v1
```

3. Run the development server:
```bash
npm run dev
```

4. Open [http://localhost:3000](http://localhost:3000) in your browser

## Build for Production

```bash
npm run build
npm start
```

## Project Structure

```
src/
├── app/              # Next.js app directory
│   ├── events/      # Event detail pages
│   ├── layout.tsx   # Root layout
│   ├── page.tsx     # Home page
│   └── globals.css  # Global styles
├── components/      # React components
│   ├── EventCard.tsx
│   ├── Timeline.tsx
│   └── Header.tsx
├── lib/             # Utilities
│   ├── api.ts       # API client
│   └── utils.ts     # Helper functions
└── types/           # TypeScript types
    └── index.ts
```

## Features

### Home Page
- Lists all active news events
- Shows event summaries and metadata
- Manual refresh button
- Auto-refresh every 5 minutes

### Event Detail Page
- Interactive timeline visualization
- Event summary and description
- Links to original news sources
- Chronological ordering of events
