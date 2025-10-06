import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-white shadow-sm border-b border-gray-200">
      <div className="container mx-auto px-4 py-4">
        <div className="flex items-center justify-between">
          <Link href="/" className="flex items-center space-x-3">
            <div className="w-10 h-10 bg-blue-500 rounded-lg flex items-center justify-center">
              <svg className="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M13 10V3L4 14h7v7l9-11h-7z" />
              </svg>
            </div>
            <h1 className="text-2xl font-bold text-gray-900">FocusLine</h1>
          </Link>
          
          <nav className="flex items-center space-x-6">
            <Link href="/" className="text-gray-700 hover:text-blue-600 font-medium">
              ホーム
            </Link>
            <a 
              href="http://localhost:8000/api/v1/docs" 
              target="_blank" 
              rel="noopener noreferrer"
              className="text-gray-700 hover:text-blue-600 font-medium"
            >
              API
            </a>
          </nav>
        </div>
      </div>
    </header>
  );
}
