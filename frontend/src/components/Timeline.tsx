import { TimelineEntry } from '@/types';
import { formatDateTime } from '@/lib/utils';

interface TimelineProps {
  entries: TimelineEntry[];
}

export default function Timeline({ entries }: TimelineProps) {
  // Sort entries by timestamp descending (newest first)
  const sortedEntries = [...entries].sort((a, b) => 
    new Date(b.timestamp).getTime() - new Date(a.timestamp).getTime()
  );

  return (
    <div className="relative">
      {/* Timeline line */}
      <div className="absolute left-4 top-0 bottom-0 w-0.5 bg-gray-200"></div>

      <div className="space-y-8">
        {sortedEntries.map((entry, index) => (
          <div key={entry.id} className="relative pl-12">
            {/* Timeline dot */}
            <div className="absolute left-0 top-1 w-8 h-8 rounded-full bg-blue-500 border-4 border-white shadow flex items-center justify-center">
              <div className="w-2 h-2 rounded-full bg-white"></div>
            </div>

            {/* Content */}
            <div className="bg-white rounded-lg border border-gray-200 p-6 shadow-sm hover:shadow-md transition-shadow">
              <div className="flex items-start justify-between mb-2">
                <h3 className="text-lg font-semibold text-gray-900 flex-1">
                  {entry.title}
                </h3>
                {entry.source_name && (
                  <span className="ml-4 px-3 py-1 bg-gray-100 text-gray-700 text-sm rounded-full whitespace-nowrap">
                    {entry.source_name}
                  </span>
                )}
              </div>

              <div className="text-sm text-gray-500 mb-3 flex items-center">
                <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                {formatDateTime(entry.timestamp)}
              </div>

              {entry.description && (
                <p className="text-gray-700 mb-3 whitespace-pre-wrap">
                  {entry.description}
                </p>
              )}

              {entry.source_url && (
                <a
                  href={entry.source_url}
                  target="_blank"
                  rel="noopener noreferrer"
                  className="inline-flex items-center text-blue-600 hover:text-blue-800 text-sm font-medium"
                >
                  記事を読む
                  <svg className="w-4 h-4 ml-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14" />
                  </svg>
                </a>
              )}
            </div>
          </div>
        ))}
      </div>

      {sortedEntries.length === 0 && (
        <div className="text-center py-12 text-gray-500">
          <svg className="w-16 h-16 mx-auto mb-4 text-gray-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
          </svg>
          <p>タイムラインエントリーがまだありません</p>
        </div>
      )}
    </div>
  );
}
