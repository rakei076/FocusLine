import Link from 'next/link';
import { EventListItem } from '@/types';
import { formatDate } from '@/lib/utils';

interface EventCardProps {
  event: EventListItem;
}

export default function EventCard({ event }: EventCardProps) {
  const getCategoryColor = (category?: string) => {
    const colors: { [key: string]: string } = {
      '政治': 'bg-red-100 text-red-800',
      '経済': 'bg-blue-100 text-blue-800',
      '社会': 'bg-green-100 text-green-800',
      'スポーツ': 'bg-yellow-100 text-yellow-800',
      'エンタメ': 'bg-purple-100 text-purple-800',
      '国際': 'bg-indigo-100 text-indigo-800',
      'その他': 'bg-gray-100 text-gray-800',
    };
    return colors[category || 'その他'] || colors['その他'];
  };

  return (
    <Link href={`/events/${event.id}`}>
      <div className="border border-gray-200 rounded-lg p-6 hover:shadow-lg transition-shadow cursor-pointer bg-white">
        <div className="flex items-start justify-between mb-2">
          <h2 className="text-xl font-bold text-gray-900 flex-1">{event.title}</h2>
          {event.category && (
            <span className={`ml-4 px-3 py-1 rounded-full text-sm font-medium whitespace-nowrap ${getCategoryColor(event.category)}`}>
              {event.category}
            </span>
          )}
        </div>
        
        {event.summary && (
          <p className="text-gray-600 mb-4 line-clamp-2">{event.summary}</p>
        )}
        
        <div className="flex items-center justify-between text-sm text-gray-500">
          <div className="flex items-center space-x-4">
            <span className="flex items-center">
              <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
              {formatDate(event.last_updated)}
            </span>
            <span className="flex items-center">
              <svg className="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
              </svg>
              {event.entry_count} 件の出来事
            </span>
          </div>
        </div>
      </div>
    </Link>
  );
}
