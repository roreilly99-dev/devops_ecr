'use client';

export default function EventsList({ events }) {
  const categoryColors = {
    dining: 'bg-green-100 text-green-800',
    cinema: 'bg-purple-100 text-purple-800',
    market: 'bg-yellow-100 text-yellow-800',
    sports: 'bg-blue-100 text-blue-800',
  };

  if (events.length === 0) {
    return (
      <div className="text-center py-12 text-gray-500">
        <p className="text-lg">No events found.</p>
        <p className="text-sm mt-2">Try adjusting your filters or check back later!</p>
      </div>
    );
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
      {events.map(event => (
        <div 
          key={event.id}
          className="bg-white rounded-lg shadow-md p-4 hover:shadow-lg transition-shadow"
        >
          <div className="flex justify-between items-start mb-2">
            <h3 className="text-lg font-semibold text-gray-900 flex-1">
              {event.title}
            </h3>
            <span className={`px-2 py-1 rounded text-xs font-medium ${categoryColors[event.category] || 'bg-gray-100 text-gray-800'}`}>
              {event.category}
            </span>
          </div>
          
          {event.description && (
            <p className="text-gray-600 text-sm mb-3 line-clamp-2">
              {event.description}
            </p>
          )}
          
          <div className="space-y-1 text-sm text-gray-700">
            <div className="flex items-start">
              <span className="mr-2">📍</span>
              <span>
                {event.location.name}
                {event.location.suburb && `, ${event.location.suburb}`}
              </span>
            </div>
            
            <div className="flex items-start">
              <span className="mr-2">📅</span>
              <span>{new Date(event.start_date).toLocaleDateString()}</span>
            </div>
            
            {event.price && (
              <div className="flex items-start">
                <span className="mr-2">💰</span>
                <span>{event.price}</span>
              </div>
            )}
          </div>
          
          {event.url && (
            <div className="mt-3">
              <a 
                href={event.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-600 hover:text-blue-800 text-sm font-medium"
              >
                Learn More →
              </a>
            </div>
          )}
        </div>
      ))}
    </div>
  );
}
