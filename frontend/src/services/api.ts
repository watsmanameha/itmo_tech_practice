import axios from 'axios';
import { Term, TermsResponse, CategoryResponse } from '../types/term';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

// Флаг для определения режима работы (статический или API)
const USE_STATIC_DATA = !import.meta.env.VITE_API_URL;

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Кеш для статических данных
let staticDataCache: { terms: Record<string, Term> } | null = null;

// Загрузка статических данных
const loadStaticData = async (): Promise<{ terms: Record<string, Term> }> => {
  if (staticDataCache) {
    return staticDataCache;
  }

  try {
    // Используем базовый путь из Vite config для корректной работы на GitHub Pages
    const basePath = import.meta.env.BASE_URL || '/';
    const dataPath = `${basePath}data/glossary.json`.replace(/\/+/g, '/');
    const response = await fetch(dataPath);
    staticDataCache = await response.json();
    return staticDataCache!;
  } catch (error) {
    console.error('Failed to load static data:', error);
    return { terms: {} };
  }
};

// Статические реализации API методов
const staticApi = {
  getAllTerms: async (skip = 0, limit = 100): Promise<TermsResponse> => {
    const data = await loadStaticData();
    const termsArray = Object.values(data.terms);
    const total = termsArray.length;
    const items = termsArray.slice(skip, skip + limit);
    return { items, total };
  },

  getTermById: async (id: string): Promise<Term> => {
    const data = await loadStaticData();
    const term = data.terms[id];
    if (!term) {
      throw new Error(`Term with id "${id}" not found`);
    }
    return term;
  },

  searchTerms: async (query: string): Promise<Term[]> => {
    const data = await loadStaticData();
    const termsArray = Object.values(data.terms);
    const lowerQuery = query.toLowerCase();
    return termsArray.filter(
      (term) =>
        term.term.toLowerCase().includes(lowerQuery) ||
        term.definition.toLowerCase().includes(lowerQuery)
    );
  },

  getCategories: async (): Promise<CategoryResponse> => {
    const data = await loadStaticData();
    const termsArray = Object.values(data.terms);
    const categories = Array.from(
      new Set(termsArray.map((term) => term.category).filter((cat): cat is string => !!cat))
    );
    return { categories };
  },

  getTermsByCategory: async (category: string): Promise<Term[]> => {
    const data = await loadStaticData();
    const termsArray = Object.values(data.terms);
    return termsArray.filter((term) => term.category === category);
  },
};

// API клиент с fallback на статические данные
export const termsApi = {
  // Получить все термины
  getAllTerms: async (skip = 0, limit = 100): Promise<TermsResponse> => {
    if (USE_STATIC_DATA) {
      return staticApi.getAllTerms(skip, limit);
    }
    try {
      const response = await api.get<TermsResponse>('/api/terms', {
        params: { skip, limit },
      });
      return response.data;
    } catch (error) {
      console.warn('API failed, falling back to static data:', error);
      return staticApi.getAllTerms(skip, limit);
    }
  },

  // Получить термин по ID
  getTermById: async (id: string): Promise<Term> => {
    if (USE_STATIC_DATA) {
      return staticApi.getTermById(id);
    }
    try {
      const response = await api.get<Term>(`/api/terms/${id}`);
      return response.data;
    } catch (error) {
      console.warn('API failed, falling back to static data:', error);
      return staticApi.getTermById(id);
    }
  },

  // Поиск терминов
  searchTerms: async (query: string): Promise<Term[]> => {
    if (USE_STATIC_DATA) {
      return staticApi.searchTerms(query);
    }
    try {
      const response = await api.get<Term[]>('/api/terms/search', {
        params: { q: query },
      });
      return response.data;
    } catch (error) {
      console.warn('API failed, falling back to static data:', error);
      return staticApi.searchTerms(query);
    }
  },

  // Получить категории
  getCategories: async (): Promise<CategoryResponse> => {
    if (USE_STATIC_DATA) {
      return staticApi.getCategories();
    }
    try {
      const response = await api.get<CategoryResponse>('/api/terms/categories');
      return response.data;
    } catch (error) {
      console.warn('API failed, falling back to static data:', error);
      return staticApi.getCategories();
    }
  },

  // Получить термины по категории
  getTermsByCategory: async (category: string): Promise<Term[]> => {
    if (USE_STATIC_DATA) {
      return staticApi.getTermsByCategory(category);
    }
    try {
      const response = await api.get<Term[]>(`/api/terms/category/${category}`);
      return response.data;
    } catch (error) {
      console.warn('API failed, falling back to static data:', error);
      return staticApi.getTermsByCategory(category);
    }
  },
};

export default api;
