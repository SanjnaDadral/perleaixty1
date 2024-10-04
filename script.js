async function submitGuess() {
  const guess = document.getElementById("guess").value;

  const response = await fetch("/guess", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ guess: parseInt(guess) }),
  });

  const data = await response.json();
  document.getElementById("result").innerText = data.result;
}
