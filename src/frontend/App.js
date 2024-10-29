// src/frontend/App.js
import React, { useState } from "react";
import ReactDOM from "react-dom";
import SearchBar from "./components/SearchBar";
import ResultsList from "./components/ResultsList";

const App = () => {
    const [query, setQuery] = useState("");
    const [results, setResults] = useState([]);

    const handleSearch = async () => {
        const response = await fetch("/search/", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ query_text: query }),
        });
        const data = await response.json();
        setResults(data.results);
    };

    return (
        <div className="App">
            <h1>InspireMe Multimedia Search</h1>
            <SearchBar query={query} setQuery={setQuery} onSearch={handleSearch} />
            <ResultsList results={results} />
        </div>
    );
};

ReactDOM.render(<App />, document.getElementById("root"));
export default App;
