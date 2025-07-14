document.addEventListener('DOMContentLoaded', function () {
  const translateBtn = document.getElementById('btn_translate');
  const languageSelect = document.getElementById('language_code');
  const helloDiv = document.getElementById('hello');

  translateBtn.addEventListener('click', function () {
    const languageCode = languageSelect.value;

    if (!languageCode) {
      helloDiv.textContent = 'Please select a language';
      return;
    }

    fetch(`https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`)
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        helloDiv.textContent = data.hello || 'Translation not available';
      })
      .catch(error => {
        console.error('Error:', error);
        helloDiv.textContent = 'Error fetching translation';
      });
  });
});
