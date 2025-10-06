export interface TimelineEntry {
  id: number;
  timestamp: string;
  title: string;
  description?: string;
  source_url?: string;
  source_name?: string;
  created_at: string;
}

export interface Event {
  id: number;
  title: string;
  summary?: string;
  description?: string;
  category?: string;
  status: string;
  first_seen: string;
  last_updated: string;
  timeline_entries: TimelineEntry[];
}

export interface EventListItem {
  id: number;
  title: string;
  summary?: string;
  category?: string;
  status: string;
  first_seen: string;
  last_updated: string;
  entry_count: number;
}
