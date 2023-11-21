// Import the necessary dependencies from React
import React, { useState } from 'react';
import './SearchBar.css';

/**
 * Represents a search bar component.
 * @returns {JSX.Element} The search bar component.
 */
function SearchBar() {
  // Define state variables for the search query and search results
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  // Define a default "no results" message
  const noResults = [
    {
      name: 'No results found',
      description: 'Try another search query',
      image_path: 'brain_deep_learning_network.png'
    }
  ];

  // Define the submit handler for the search form
  const handleSubmit = (event) => {
    event.preventDefault();
    // Make a fetch request to the API endpoint with the search query
    fetch(
        `${process.env.REACT_APP_API_ENDPOINT}/projects`,
        { headers: {
            'Authorization': `Bearer ${process.env.REACT_APP_API_TOKEN}`
            }
        }
      )
      .then(response => {
        console.log(response)
        // If the response is successful, parse the JSON data
        if (response.ok) {
          return response.json();
        }
        // If there is an HTTP error, throw an error
        throw new Error(`HTTP error! status: ${response.status}`);
      })
      .then(data => {
        // If there is data returned, set the results state variable
        if (data) {
          setResults(data);
        } else {
          // If there is no data, set the results state variable to the default "no results" message
          setResults(noResults);
        }
      }).catch(error => {
        // If there is an error, log the error and set the results state variable to the default "no results" message
        console.log(error);
        setResults(noResults);
      });
  };

  return (
    <div className="SearchBar"> 
      <form onSubmit={handleSubmit}>  
        <div>
          {/* Input field for the search query */}
          <input type="text" value={query} onChange={e => setQuery(e.target.value)} className="search-bar" />
          <button type="submit">Search</button>
          {/* Display the search results */}
          <div className="results-grid">
            {results.map((result, index) => (
              <div key={index} className="result-card">
                <img src={`/images/${result.image_path}`} alt={result.name} style={{maxWidth: '100%', maxHeight: '100%'}} />
                <h2>{result.name}</h2>
                <h3>{result.year}</h3>
                <p>{result.description}</p>
              </div>
            ))}
          </div>
        </div>
      </form> 
    </div>
  );
}

// Export the SearchBar component as the default export
export default SearchBar;