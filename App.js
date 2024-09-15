import React from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import LoginPage from './LoginPage';
import HomePage from './HomePage';
import FAQPage from './FAQPage';
import AboutPage from './AboutPage';
import ErrorBoundary from './ErrorBoundary';
import './base.css';

export default function App() {
  return (
    <ErrorBoundary>
      <Router>
        <Routes>
          <Route path="/login" element={<LoginPage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/faq" element={<FAQPage />} />
          <Route path="/about" element={<AboutPage />} />
          <Route path="/" element={<Navigate replace to="/login" />} />
          <Route path="*" element={<div>404: Not Found</div>} />
        </Routes>
      </Router>
    </ErrorBoundary>
  );
}