import { useState } from 'react';
import Header from './components/layout/Header';
import GlossaryGrid from './components/glossary/GlossaryGrid';
import MindMap from './components/mindmap/MindMap';

type ViewType = 'glossary' | 'mindmap';

function App() {
  const [currentView, setCurrentView] = useState<ViewType>('glossary');

  return (
    <div className="min-h-screen bg-primary-50">
      <Header currentView={currentView} onViewChange={setCurrentView} />

      <main>
        {currentView === 'glossary' ? <GlossaryGrid /> : <MindMap />}
      </main>
    </div>
  );
}

export default App;
