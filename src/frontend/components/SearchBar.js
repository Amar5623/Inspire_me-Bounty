// src/frontend/components/SearchBar.js
import React from "react";

const SearchBar = ({ query, setQuery, onSearch }) => {
    return (
        <div>
            <input
                type="text"
                placeholder="Enter your query..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button onClick={onSearch}>Search</button>
        </div>
    );
};

export default SearchBar;
