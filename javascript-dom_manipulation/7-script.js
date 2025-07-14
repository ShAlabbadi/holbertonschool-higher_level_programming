document.addEventListener('DOMContentLoaded', function () {
  const listMovies = document.getElementById('list_movies');
  const apiUrl = 'https://swapi-api.hbtn.io/api/films/?format=json';

  fetch(apiUrl)
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      // Clear any existing content
      listMovies.innerHTML = '';

      // Loop through each movie and add it to the list
      data.results.forEach(movie => {
        const listItem = document.createElement('li');
        listItem.textContent = movie.title;
        listMovies.appendChild(listItem);
      });
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      listMovies.innerHTML = '<li>Error loading movies</li>';
    });
});
