// src/frontend/components/ResultsList.js
import React from "react";

const ResultsList = ({ results }) => {
    return (
        <div className="results">
            {results.map((result, index) => (
                <div key={index} className="result-item">
                    <p>{result.content}</p>
                    <span>Score: {result.score.toFixed(2)}</span>
                </div>
            ))}
        </div>
    );
};

export default ResultsList;
