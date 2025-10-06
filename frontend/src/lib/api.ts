import axios from 'axios';
import { Event, EventListItem } from '@/types';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000/api/v1';

const api = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const eventsApi = {
  getEvents: async (status?: string): Promise<EventListItem[]> => {
    const params = status ? { status } : {};
    const response = await api.get('/events', { params });
    return response.data;
  },

  getEvent: async (id: number): Promise<Event> => {
    const response = await api.get(`/events/${id}`);
    return response.data;
  },

  triggerScrape: async (): Promise<{ message: string }> => {
    const response = await api.post('/scrape');
    return response.data;
  },
};

export default api;
