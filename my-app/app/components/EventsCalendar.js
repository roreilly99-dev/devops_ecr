'use client';

import { useState, useEffect } from 'react';
import { Calendar, dateFnsLocalizer } from 'react-big-calendar';
import { format, parse, startOfWeek, getDay } from 'date-fns';
import 'react-big-calendar/lib/css/react-big-calendar.css';

const locales = {
  'en-US': require('date-fns/locale/en-US'),
};

const localizer = dateFnsLocalizer({
  format,
  parse,
  startOfWeek,
  getDay,
  locales,
});

export default function EventsCalendar({ events }) {
  const [selectedEvent, setSelectedEvent] = useState(null);

  // Transform events for calendar
  const calendarEvents = events.map(event => ({
    id: event.id,
    title: event.title,
    start: new Date(event.start_date),
    end: event.end_date ? new Date(event.end_date) : new Date(event.start_date),
    resource: event,
  }));

  // Event style based on category
  const eventStyleGetter = (event) => {
    const categoryColors = {
      dining: '#10b981',
      cinema: '#8b5cf6',
      market: '#f59e0b',
      sports: '#3b82f6',
    };

    const backgroundColor = categoryColors[event.resource.category] || '#6b7280';

    return {
      style: {
        backgroundColor,
        borderRadius: '4px',
        opacity: 0.9,
        color: 'white',
        border: '0px',
        display: 'block',
      },
    };
  };

  const handleSelectEvent = (event) => {
    setSelectedEvent(event.resource);
  };

  return (
    <div className="relative">
      <div className="h-[600px] bg-white rounded-lg shadow-lg p-4">
        <Calendar
          localizer={localizer}
          events={calendarEvents}
          startAccessor="start"
          endAccessor="end"
          style={{ height: '100%' }}
          onSelectEvent={handleSelectEvent}
          eventPropGetter={eventStyleGetter}
        />
      </div>

      {/* Event Details Modal */}
      {selectedEvent && (
        <div 
          className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50"
          onClick={() => setSelectedEvent(null)}
        >
          <div 
            className="bg-white rounded-lg p-6 max-w-lg w-full"
            onClick={(e) => e.stopPropagation()}
          >
            <div className="flex justify-between items-start mb-4">
              <h2 className="text-2xl font-bold">{selectedEvent.title}</h2>
              <button 
                onClick={() => setSelectedEvent(null)}
                className="text-gray-500 hover:text-gray-700"
              >
                ✕
              </button>
            </div>
            
            <div className="space-y-3">
              <div>
                <span className="font-semibold">Category:</span>
                <span className="ml-2 px-3 py-1 rounded-full text-sm bg-gray-100">
                  {selectedEvent.category}
                </span>
              </div>
              
              {selectedEvent.description && (
                <div>
                  <span className="font-semibold">Description:</span>
                  <p className="mt-1 text-gray-700">{selectedEvent.description}</p>
                </div>
              )}
              
              <div>
                <span className="font-semibold">Date:</span>
                <p className="mt-1">{format(new Date(selectedEvent.start_date), 'PPpp')}</p>
              </div>
              
              <div>
                <span className="font-semibold">Location:</span>
                <p className="mt-1">
                  {selectedEvent.location.name}
                  {selectedEvent.location.suburb && `, ${selectedEvent.location.suburb}`}
                </p>
              </div>
              
              {selectedEvent.price && (
                <div>
                  <span className="font-semibold">Price:</span>
                  <p className="mt-1">{selectedEvent.price}</p>
                </div>
              )}
              
              {selectedEvent.url && (
                <div>
                  <a 
                    href={selectedEvent.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-block px-4 py-2 bg-blue-600 text-white rounded hover:bg-blue-700"
                  >
                    View Details →
                  </a>
                </div>
              )}
            </div>
          </div>
        </div>
      )}
    </div>
  );
}
