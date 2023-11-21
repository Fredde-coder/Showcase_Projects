// JavaScript - App.test.js
import React from 'react';
import { render, screen } from '@testing-library/react';
import App from '../App';

test('renders Fredrik Lundberg header', () => {
  render(<App />);
  const linkElement = screen.getByText(/Fredrik Lundberg/i);
  expect(linkElement).toBeInTheDocument();
});