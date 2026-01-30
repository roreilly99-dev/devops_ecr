'use client';

import { useState, useEffect } from 'react';
import EventsCalendar from './components/EventsCalendar';
import EventsList from './components/EventsList';
import CategoryFilter from './components/CategoryFilter';
import { getEvents, getCategories, triggerScrape } from './lib/api';

export default function Home() {
  const [events, setEvents] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState(null);
  const [view, setView] = useState('calendar'); // 'calendar' or 'list'
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [scraping, setScraping] = useState(false);

  // Load initial data
  useEffect(() => {
    loadData();
  }, [selectedCategory]);

  async function loadData() {
    try {
      setLoading(true);
      setError(null);

      // Load categories if not loaded
      if (categories.length === 0) {
        const categoriesData = await getCategories();
        setCategories(categoriesData.categories);
      }

      // Load events
      const filters = {};
      if (selectedCategory) {
        filters.category = selectedCategory;
      }
      const eventsData = await getEvents(filters);
      setEvents(eventsData.events);
    } catch (err) {
      console.error('Error loading data:', err);
      setError('Failed to load events. Please make sure the backend API is running.');
    } finally {
      setLoading(false);
    }
  }

  async function handleScrape() {
    try {
      setScraping(true);
      await triggerScrape();
      // Reload events after scraping
      await loadData();
    } catch (err) {
      console.error('Error scraping:', err);
      alert('Failed to trigger scraping. Please try again.');
    } finally {
      setScraping(false);
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100">
      {/* Header */}
      <header className="bg-white shadow-md">
        <div className="container mx-auto px-4 py-6">
          <div className="flex flex-col md:flex-row justify-between items-center gap-4">
            <div>
              <h1 className="text-3xl font-bold text-gray-900">Perth Events</h1>
              <p className="text-gray-600 mt-1">
                Discover dining, cinema, markets & sports in Perth
              </p>
            </div>
            
            <div className="flex gap-2">
              <button
                onClick={handleScrape}
                disabled={scraping}
                className="px-4 py-2 bg-green-600 text-white rounded-lg hover:bg-green-700 disabled:bg-gray-400 transition-colors"
              >
                {scraping ? 'Scraping...' : '🔄 Update Events'}
              </button>
              
              <div className="flex border border-gray-300 rounded-lg overflow-hidden">
                <button
                  onClick={() => setView('calendar')}
                  className={`px-4 py-2 font-medium transition-colors ${
                    view === 'calendar'
                      ? 'bg-blue-600 text-white'
                      : 'bg-white text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  📅 Calendar
                </button>
                <button
                  onClick={() => setView('list')}
                  className={`px-4 py-2 font-medium transition-colors ${
                    view === 'list'
                      ? 'bg-blue-600 text-white'
                      : 'bg-white text-gray-700 hover:bg-gray-100'
                  }`}
                >
                  📋 List
                </button>
              </div>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Category Filter */}
        <div className="mb-6">
          <CategoryFilter
            categories={categories}
            selectedCategory={selectedCategory}
            onCategoryChange={setSelectedCategory}
          />
        </div>

        {/* Loading State */}
        {loading && (
          <div className="text-center py-12">
            <div className="inline-block animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600"></div>
            <p className="mt-4 text-gray-600">Loading events...</p>
          </div>
        )}

        {/* Error State */}
        {error && !loading && (
          <div className="bg-red-50 border border-red-200 rounded-lg p-6 text-center">
            <p className="text-red-800 font-medium">{error}</p>
            <p className="text-red-600 text-sm mt-2">
              Make sure the backend is running on port 8000
            </p>
            <button
              onClick={loadData}
              className="mt-4 px-4 py-2 bg-red-600 text-white rounded hover:bg-red-700"
            >
              Retry
            </button>
          </div>
        )}

        {/* Events Display */}
        {!loading && !error && (
          <div>
            <div className="mb-4 text-gray-600">
              Showing {events.length} event{events.length !== 1 ? 's' : ''}
              {selectedCategory && ` in ${selectedCategory}`}
            </div>
            
            {view === 'calendar' ? (
              <EventsCalendar events={events} />
            ) : (
              <EventsList events={events} />
            )}
          </div>
        )}
      </main>

      {/* Footer */}
      <footer className="bg-white mt-12 py-6 border-t">
        <div className="container mx-auto px-4 text-center text-gray-600">
          <p>Perth Events Scraper - Discover what's happening in Perth</p>
          <p className="text-sm mt-1">
            Events are automatically updated from various sources
          </p>
        </div>
      </footer>
    </div>
  );
}
