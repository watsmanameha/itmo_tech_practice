import React, { useEffect, useState } from 'react';
import { Term } from '../../types/term';
import { termsApi } from '../../services/api';
import TermCard from './TermCard';
import SearchFilter from './SearchFilter';
import TermModal from './TermModal';

const GlossaryGrid: React.FC = () => {
  const [terms, setTerms] = useState<Term[]>([]);
  const [filteredTerms, setFilteredTerms] = useState<Term[]>([]);
  const [categories, setCategories] = useState<string[]>([]);
  const [selectedCategory, setSelectedCategory] = useState<string>('');
  const [selectedTerm, setSelectedTerm] = useState<Term | null>(null);
  const [modalTerm, setModalTerm] = useState<Term | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadData();
  }, []);

  const loadData = async () => {
    try {
      setLoading(true);
      const [termsData, categoriesData] = await Promise.all([
        termsApi.getAllTerms(),
        termsApi.getCategories(),
      ]);
      setTerms(termsData.items);
      setFilteredTerms(termsData.items);
      setCategories(categoriesData.categories);
    } catch (err) {
      setError('Ошибка загрузки данных');
      console.error('Error loading data:', err);
    } finally {
      setLoading(false);
    }
  };

  const handleSearch = async (query: string) => {
    if (!query.trim()) {
      setFilteredTerms(selectedCategory ? terms.filter(t => t.category === selectedCategory) : terms);
      return;
    }

    try {
      const results = await termsApi.searchTerms(query);
      const filtered = selectedCategory
        ? results.filter(t => t.category === selectedCategory)
        : results;
      setFilteredTerms(filtered);
    } catch (err) {
      console.error('Error searching:', err);
    }
  };

  const handleCategoryChange = (category: string) => {
    setSelectedCategory(category);
    if (category) {
      setFilteredTerms(terms.filter(t => t.category === category));
    } else {
      setFilteredTerms(terms);
    }
  };

  const handleTermClick = (term: Term) => {
    setSelectedTerm(selectedTerm?.id === term.id ? null : term);
    setModalTerm(term);
  };

  if (loading) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-gray-600">Загрузка...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className="flex items-center justify-center h-64">
        <div className="text-red-600">{error}</div>
      </div>
    );
  }

  return (
    <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <SearchFilter
        onSearch={handleSearch}
        onCategoryChange={handleCategoryChange}
        categories={categories}
        selectedCategory={selectedCategory}
      />

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {filteredTerms.map((term) => (
          <TermCard
            key={term.id}
            term={term}
            onClick={() => handleTermClick(term)}
            isHighlighted={selectedTerm?.id === term.id}
          />
        ))}
      </div>

      {filteredTerms.length === 0 && (
        <div className="text-center py-12 text-gray-500">
          Термины не найдены
        </div>
      )}

      {modalTerm && (
        <TermModal
          term={modalTerm}
          onClose={() => setModalTerm(null)}
        />
      )}
    </div>
  );
};

export default GlossaryGrid;
