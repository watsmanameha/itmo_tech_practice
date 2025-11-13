import React from 'react';

interface HeaderProps {
  currentView: 'glossary' | 'mindmap';
  onViewChange: (view: 'glossary' | 'mindmap') => void;
  userName?: string;
}

const Header: React.FC<HeaderProps> = ({ currentView, onViewChange, userName = "Евгений Джулай" }) => {
  const handleUserClick = () => {
    window.open('https://t.me/wrxnguser', '_blank', 'noopener,noreferrer');
  };

  return (
    <header className="bg-white shadow-sm">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div className="flex justify-between items-center h-16">
          {/* Left side - Navigation tabs */}
          <div className="flex space-x-2">
            <button
              onClick={() => onViewChange('glossary')}
              className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                currentView === 'glossary'
                  ? 'bg-gray-900 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-100'
              }`}
            >
              📖 Глоссарий
            </button>
            <button
              onClick={() => onViewChange('mindmap')}
              className={`px-4 py-2 rounded-lg font-medium transition-colors ${
                currentView === 'mindmap'
                  ? 'bg-gray-900 text-white'
                  : 'bg-white text-gray-700 hover:bg-gray-100'
              }`}
            >
              🔗 Семантический граф
            </button>
          </div>

          {/* Right side - Logo and User */}
          <div className="flex items-center space-x-4">
            <div className="text-2xl font-bold">ИТМО</div>
            <div
              className="flex items-center space-x-2 cursor-pointer hover:opacity-80 transition-opacity"
              onClick={handleUserClick}
              role="button"
              tabIndex={0}
              onKeyDown={(e) => {
                if (e.key === 'Enter' || e.key === ' ') {
                  handleUserClick();
                }
              }}
            >
              <div className="w-8 h-8 rounded-full bg-primary-500 flex items-center justify-center text-white font-semibold">
                {userName.split(' ').map(n => n[0]).join('')}
              </div>
              <span className="text-sm font-medium text-gray-700">{userName}</span>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
