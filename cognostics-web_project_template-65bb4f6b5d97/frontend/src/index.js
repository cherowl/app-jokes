import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import AuthService from './services/AuthService';
import registerServiceWorker from './registerServiceWorker';
import './index.css';

registerServiceWorker();

// Try to establish socket connection before rendering
// to establish authentication status
AuthService.connect().then(() => {
  ReactDOM.render(<App />, document.getElementById('root'));
});

