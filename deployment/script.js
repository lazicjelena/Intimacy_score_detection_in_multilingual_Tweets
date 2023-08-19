const outputMessage = document.getElementById('outputMessage');
const searchForm = document.getElementById('searchForm');
const searchInput = document.getElementById('searchInput');

searchForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  const inputValue = searchInput.value;

  // Send the input value to the server for prediction
  const response = await fetch('/predict', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ inputText: inputValue })
  });

  if (response.ok) {
    const result = await response.json();

    // Update the output message with the predicted score
    const outputText = `Predicted Intimacy Score: ${result.score.toFixed(2)}<br>For the message:<br>${inputValue}`;
    outputMessage.innerHTML = outputText;
  } else {
    outputMessage.innerHTML = 'Error predicting the score.';
  }

  // Clear the search input
  searchInput.value = '';
});
