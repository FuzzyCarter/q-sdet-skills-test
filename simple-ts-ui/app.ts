// app.ts

// Select DOM elements
const nameForm = document.getElementById("nameForm") as HTMLFormElement;
const nameInput = document.getElementById("inputName") as HTMLInputElement;
const responseMessage = document.getElementById("responseMessage") as HTMLDivElement;
const errorMessage = document.getElementById("errorMessage") as HTMLDivElement;

// Function to handle form submission
nameForm?.addEventListener("submit", async (event) => {
  event.preventDefault();

  // Reset messages
  responseMessage.textContent = "";
  errorMessage.textContent = "";

  const name = nameInput.value.trim();

  if (!name) {
    errorMessage.textContent = "Name is required.";
    return;
  }

  try {
    // Make POST request to Flask API
    const response = await fetch("http://127.0.0.1:5000/submit-name", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Origin": "*", // Allow CORS
      },
      body: JSON.stringify({ name }),
    });

    // Handle successful response
    if (response.ok) {
      const data = await response.json();
      responseMessage.textContent = data.message;
      responseMessage.style.color = "green";
    } else {
      // Handle errors from the API
      const data = await response.json();
      errorMessage.textContent = data.error || "An unexpected error occurred.";
      errorMessage.style.color = "red";
    }
  } catch (error) {
    // Handle network or other errors
    errorMessage.textContent = "There was an error communicating with the server.";
    errorMessage.style.color = "red";
  }
});

