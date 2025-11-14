import React, { useEffect } from 'react';
import { Term } from '../../types/term';

interface TermModalProps {
  term: Term;
  onClose: () => void;
}

const TermModal: React.FC<TermModalProps> = ({ term, onClose }) => {
  useEffect(() => {
    const handleEscape = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleEscape);
    return () => window.removeEventListener('keydown', handleEscape);
  }, [onClose]);

  return (
    <div
      className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4"
      onClick={onClose}
    >
      <div
        className="bg-white rounded-xl max-w-2xl w-full max-h-[90vh] overflow-y-auto shadow-2xl"
        onClick={(e) => e.stopPropagation()}
      >
        {/* Header */}
        <div className="sticky top-0 bg-white border-b border-gray-200 px-6 py-4 flex justify-between items-start">
          <div className="flex-1">
            <h2 className="text-2xl font-bold text-gray-900 mb-2">{term.term}</h2>
            {term.category && (
              <span className="inline-block px-3 py-1 text-sm rounded-full bg-primary-100 text-primary-900">
                {term.category}
              </span>
            )}
          </div>
          <button
            onClick={onClose}
            className="ml-4 text-gray-400 hover:text-gray-600 transition-colors"
            aria-label="Закрыть"
          >
            <svg className="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>

        {/* Content */}
        <div className="px-6 py-6">
          {/* Definition */}
          <div className="mb-6">
            <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-2">
              Определение
            </h3>
            <p className="text-gray-700 leading-relaxed">{term.definition}</p>
          </div>

          {/* Relations */}
          {term.relations && term.relations.length > 0 && (
            <div>
              <h3 className="text-sm font-semibold text-gray-500 uppercase tracking-wide mb-3">
                Связи ({term.relations.length})
              </h3>
              <div className="space-y-2">
                {term.relations.map((relation, index) => (
                  <div
                    key={index}
                    className="flex items-start p-3 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors"
                  >
                    <div className="flex-1">
                      <div className="flex items-center gap-2 mb-1">
                        <span className="text-sm font-medium text-primary-600">
                          {relation.relation_type}
                        </span>
                        <svg className="w-4 h-4 text-gray-400" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                          <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M9 5l7 7-7 7" />
                        </svg>
                      </div>
                      <div className="text-sm text-gray-600">
                        ID: <span className="font-mono text-xs bg-gray-200 px-1.5 py-0.5 rounded">{relation.target_term_id}</span>
                      </div>
                      {relation.description && (
                        <p className="text-sm text-gray-500 mt-1">{relation.description}</p>
                      )}
                    </div>
                  </div>
                ))}
              </div>
            </div>
          )}

          {(!term.relations || term.relations.length === 0) && (
            <div className="text-center py-4 text-gray-400 text-sm">
              Нет связей с другими терминами
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default TermModal;
