"""
Database utilities for storing and retrieving events
"""
import os
from typing import List, Optional
from datetime import datetime
import json
from models.event import Event, EventCategory


class EventDatabase:
    """
    Abstract database class for event storage
    Can be implemented with DynamoDB, MongoDB, or other databases
    """
    
    def __init__(self):
        self.storage_type = os.getenv('STORAGE_TYPE', 'memory')
        self._memory_store = []  # In-memory storage for development
    
    def save_event(self, event: Event) -> str:
        """Save a single event"""
        if self.storage_type == 'memory':
            # Generate simple ID if not present
            if not event.id:
                event.id = f"event_{len(self._memory_store) + 1}"
            self._memory_store.append(event)
            return event.id
        # TODO: Implement DynamoDB/MongoDB storage
        return event.id
    
    def save_events(self, events: List[Event]) -> List[str]:
        """Save multiple events"""
        return [self.save_event(event) for event in events]
    
    def get_event(self, event_id: str) -> Optional[Event]:
        """Get a single event by ID"""
        if self.storage_type == 'memory':
            for event in self._memory_store:
                if event.id == event_id:
                    return event
        return None
    
    def get_events(
        self,
        category: Optional[EventCategory] = None,
        start_date: Optional[datetime] = None,
        end_date: Optional[datetime] = None,
        limit: int = 100
    ) -> List[Event]:
        """Get events with optional filters"""
        if self.storage_type == 'memory':
            filtered = self._memory_store
            
            if category:
                filtered = [e for e in filtered if e.category == category]
            
            if start_date:
                filtered = [e for e in filtered if e.start_date >= start_date]
            
            if end_date:
                filtered = [e for e in filtered if e.start_date <= end_date]
            
            return filtered[:limit]
        
        return []
    
    def delete_event(self, event_id: str) -> bool:
        """Delete an event"""
        if self.storage_type == 'memory':
            self._memory_store = [e for e in self._memory_store if e.id != event_id]
            return True
        return False
    
    def clear_all(self) -> bool:
        """Clear all events (for testing)"""
        if self.storage_type == 'memory':
            self._memory_store = []
            return True
        return False


# Singleton instance
_db_instance = None


def get_database() -> EventDatabase:
    """Get database singleton instance"""
    global _db_instance
    if _db_instance is None:
        _db_instance = EventDatabase()
    return _db_instance
