1. HTML: Structure
Create a basic HTML structure with:

An input box where users type their search query.

A container to display movie results.

html

<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Movie Search</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>
  <div class="search-container">
    <input type="text" id="searchInput" placeholder="Search movies..." />
  </div>

  <div id="moviesList" class="movies-list"></div>

  <script src="script.js"></script>
</body>
</html>
2. CSS: Styling
Basic styling for the input box and movie results:

css

/* styles.css */

body {
  font-family: Arial, sans-serif;
  margin: 20px;
  background-color: #f2f2f2;
}

.search-container {
  margin-bottom: 20px;
}

#searchInput {
  width: 100%;
  padding: 10px;
  font-size: 16px;
}

.movies-list {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
}

.movie-item {
  background-color: white;
  padding: 15px;
  border-radius: 6px;
  width: 200px;
  box-shadow: 0 2px 5px rgba(0,0,0,0.1);
}

.movie-title {
  font-weight: bold;
  margin-bottom: 5px;
}

.movie-year {
  color: gray;
}
3. JavaScript: Logic
We will have a list of movies stored in a JavaScript array.

When the user types in the input box, we filter the movies based on the input and display the results.

We add an event listener to the input box to trigger search on each key press.

js

// script.js

// Sample movie data
const movies = [
  { title: "The Shawshank Redemption", year: 1994 },
  { title: "The Godfather", year: 1972 },
  { title: "The Dark Knight", year: 2008 },
  { title: "Pulp Fiction", year: 1994 },
  { title: "The Lord of the Rings: The Return of the King", year: 2003 },
  { title: "Forrest Gump", year: 1994 },
  { title: "Inception", year: 2010 },
  { title: "Fight Club", year: 1999 },
];

// Reference to DOM elements
const searchInput = document.getElementById("searchInput");
const moviesList = document.getElementById("moviesList");

// Function to display movies
function displayMovies(filteredMovies) {
  // Clear previous results
  moviesList.innerHTML = "";

  if (filteredMovies.length === 0) {
    moviesList.innerHTML = "<p>No movies found.</p>";
    return;
  }

  // Add movie items to container
  filteredMovies.forEach(movie => {
    const movieDiv = document.createElement("div");
    movieDiv.classList.add("movie-item");

    movieDiv.innerHTML = `
      <div class="movie-title">${movie.title}</div>
      <div class="movie-year">${movie.year}</div>
    `;

    moviesList.appendChild(movieDiv);
  });
}

// Function to handle search input
function handleSearch() {
  const query = searchInput.value.toLowerCase();

  const filteredMovies = movies.filter(movie =>
    movie.title.toLowerCase().includes(query)
  );

  displayMovies(filteredMovies);
}

// Initial display of all movies
displayMovies(movies);

// Listen for input event on search box
searchInput.addEventListener("input", handleSearch);
How it works:
When the page loads, it shows all the movies.

When you start typing in the input box, the handleSearch function filters the movies array based on the search text.

The displayMovies function updates the DOM to show only the filtered movies.

