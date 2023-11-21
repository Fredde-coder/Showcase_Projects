// JavaScript - frontend/src/Repo.js

/**
 * React component that displays information about a GitHub repository.
 * @param {string} url - The URL of the GitHub repository.
 * @returns {JSX.Element|null} - The rendered React component.
 */
import React, { useEffect, useState } from 'react';

function Repo({ url }) {
  const [repo, setRepo] = useState(null);

  /**
   * Fetches repository data from the GitHub API and updates the state.
   */
  useEffect(() => {
    fetch(`https://api.github.com/repos/${url}`)
      .then(response => response.json())
      .then(data => setRepo(data));
  }, [url]);

  // If repository data is not available, return null.
  if (!repo) return null;

  return (
    <div>
      <h2>{repo.name}</h2>
      <p>{repo.description}</p>
      <img src={`/images/${repo.name}.png`} alt={repo.name} />
    </div>
  );
}

export default Repo;