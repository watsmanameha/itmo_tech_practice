import React from 'react';
import { Term } from '../../types/term';

interface TermCardProps {
  term: Term;
  onClick?: () => void;
  isHighlighted?: boolean;
}

const TermCard: React.FC<TermCardProps> = ({ term, onClick, isHighlighted = false }) => {
  return (
    <div
      onClick={onClick}
      className={`
        rounded-lg p-6 shadow-sm hover:shadow-md transition-all cursor-pointer
        border-2 ${isHighlighted ? 'border-primary-500 bg-primary-50' : 'border-transparent bg-white'}
      `}
    >
      <h3 className={`text-lg font-semibold mb-2 ${isHighlighted ? 'text-primary-900' : 'text-gray-900'}`}>
        {term.term}
      </h3>
      <p className={`text-sm ${isHighlighted ? 'text-primary-700' : 'text-gray-600'} line-clamp-3`}>
        {term.definition}
      </p>
      {term.category && (
        <div className="mt-4">
          <span className={`inline-block px-2 py-1 text-xs rounded ${
            isHighlighted
              ? 'bg-primary-200 text-primary-900'
              : 'bg-gray-100 text-gray-700'
          }`}>
            {term.category}
          </span>
        </div>
      )}
    </div>
  );
};

export default TermCard;
