// JavaScript - frontend/src/App.js
import React from 'react';
import './App.css';
import SearchBar from './SearchBar';

/**
 * Renders the main application component.
 * @returns {JSX.Element} The rendered App component.
 */
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Fredrik Lundberg</h1>
      </header>
      <nav className="App-nav">
        <a href="#articles">Articles</a>
        <a href="#cv">CV</a>
        <a href="#contact">Contact</a>
      </nav>
      <main className="App-main">
      <header className="App-subheader">
        <h2>Explore My Projects</h2>
      </header>
      <SearchBar/>
     </main>
      <footer className="App-footer">
      </footer>
    </div>
  );
}

export default App;