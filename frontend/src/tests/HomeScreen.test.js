import React from 'react';
import { render, screen } from '@testing-library/react';
import HomeScreen from '../screens/HomeScreen';

describe('HomeScreen component', () => {

    test('renders the cards correctly', () => {
        render(<HomeScreen />);
        expect(screen.getAllByRole('img')).toHaveLength(3);
    });

    test('changes the opacity of the cards as the user scrolls', () => {
        // TODO: write this test
    });

    test('renders the images correctly', () => {
        render(<HomeScreen />);
        expect(screen.getAllByRole('img')).toHaveLength(3);
    });

    test('renders the text in the cards correctly', () => {
        render(<HomeScreen />);
        const cardHeaders = screen.queryAllByText(/end-to-end machine learning/i);
        expect(cardHeaders).toHaveLength(2);
        const cardTexts = screen.queryAllByText(/Blacklight Labs specializes in end-to-end machine learning/i);
        expect(cardTexts).toHaveLength(1);
        const tabularAndImageText = screen.queryAllByText(/tabular and image data/i);
        expect(tabularAndImageText).toHaveLength(3);
        expect(screen.getByText(/automates the machine learning model creation/i)).toBeInTheDocument();
    });
});