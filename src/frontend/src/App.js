// App.js

import React, { useState } from 'react';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const handleSearch = async () => {
    try {
      const response = await fetch(`http://localhost:8000/search?query=${query}`);
      const data = await response.json();

      // Assuming `data.results` is now a flat array of objects
      setResults(data.results || []); // Fallback to empty array if no results
    } catch (error) {
      console.error("Error fetching search results:", error);
      setResults([]); // Fallback to empty array in case of an error
    }
  };

  return (
    <div>
      <input 
        type="text" 
        value={query} 
        onChange={(e) => setQuery(e.target.value)} 
        placeholder="Search..."
      />
      <button onClick={handleSearch}>Search</button>
      <div>
        {results.length > 0 ? (
          results.map((result) => (
            <div key={result.id}>
              <h2>{result.text}</h2>
              <img src={`http://localhost:8000/${result.image_path}`} alt={result.text} />
              <p>Source: {result.source}</p>
            </div>
          ))
        ) : (
          <p>No results found.</p>
        )}
      </div>
    </div>
  );
}

export default App;
