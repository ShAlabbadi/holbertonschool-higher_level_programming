// Wait for the DOM to be fully loaded before executing
document.addEventListener('DOMContentLoaded', function () {
  // Fetch the translation from the API
  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => {
      if (!response.ok) {
        throw new Error('Network response was not ok');
      }
      return response.json();
    })
    .then(data => {
      // Display the translation in the #hello element
      document.getElementById('hello').textContent = data.hello;
    })
    .catch(error => {
      console.error('There was a problem with the fetch operation:', error);
      document.getElementById('hello').textContent = 'Error loading translation';
    });
});
