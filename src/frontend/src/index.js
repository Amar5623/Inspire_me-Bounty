// index.js

import React from 'react';
import { createRoot } from 'react-dom/client';
import App from './App';

const container = document.getElementById('root');
const root = createRoot(container); // createRoot is used instead of ReactDOM.render
root.render(<App />);
