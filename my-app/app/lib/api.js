/**
 * API client for Perth Events backend
 */

const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function getEvents(filters = {}) {
  const params = new URLSearchParams();
  
  if (filters.category) params.append('category', filters.category);
  if (filters.startDate) params.append('start_date', filters.startDate);
  if (filters.endDate) params.append('end_date', filters.endDate);
  if (filters.limit) params.append('limit', filters.limit);
  
  const url = `${API_BASE_URL}/api/events${params.toString() ? '?' + params.toString() : ''}`;
  
  const response = await fetch(url, {
    cache: 'no-store'
  });
  
  if (!response.ok) {
    throw new Error('Failed to fetch events');
  }
  
  return response.json();
}

export async function getEvent(eventId) {
  const response = await fetch(`${API_BASE_URL}/api/events/${eventId}`, {
    cache: 'no-store'
  });
  
  if (!response.ok) {
    throw new Error('Failed to fetch event');
  }
  
  return response.json();
}

export async function getCategories() {
  const response = await fetch(`${API_BASE_URL}/api/categories`, {
    cache: 'no-store'
  });
  
  if (!response.ok) {
    throw new Error('Failed to fetch categories');
  }
  
  return response.json();
}

export async function triggerScrape() {
  const response = await fetch(`${API_BASE_URL}/api/scrape`, {
    method: 'POST',
    cache: 'no-store'
  });
  
  if (!response.ok) {
    throw new Error('Failed to trigger scrape');
  }
  
  return response.json();
}
