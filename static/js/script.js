const symptomForm = document.getElementById("symptomForm");
const symptomTable = document.getElementById("symptomTable");
const diagnoseButton = document.getElementById("diagnoseButton");
const diagnosisResult = document.getElementById("diagnosisResult");

const API_BASE_URL = "http://127.0.0.1:5000/api";

// Fetch and display symptoms
async function fetchSymptoms() {
  try {
    const response = await fetch(`${API_BASE_URL}/symptoms`);
    if (!response.ok) {
      throw new Error("Failed to fetch symptoms");
    }

    const symptoms = await response.json();

    // Clear the table before repopulating
    symptomTable.innerHTML = "";

    // Populate the table with symptoms
    symptoms.forEach((symptom) => {
      const row = document.createElement("tr");

      row.innerHTML = `
        <td class="border px-4 py-2">${symptom.symptom}</td>
        <td class="border px-4 py-2">${new Date(symptom.date).toLocaleDateString()}</td>
        <td class="border px-4 py-2">
          <button class="bg-red-500 text-white px-3 py-1 rounded delete-btn" data-id="${symptom.id}">
            Delete
          </button>
        </td>
      `;

      symptomTable.appendChild(row);
    });

    // Attach event listeners to all delete buttons
    document.querySelectorAll(".delete-btn").forEach((button) => {
      button.addEventListener("click", async function () {
        const symptomId = this.getAttribute("data-id");
        await deleteSymptom(symptomId);
      });
    });
  } catch (error) {
    console.error("Error fetching symptoms:", error);
  }
}

// Delete a symptom from the database
async function deleteSymptom(symptomId) {
  try {
    const response = await fetch(`${API_BASE_URL}/symptoms/${symptomId}`, {
      method: "DELETE",
    });

    if (response.ok) {
      console.log(`Symptom ID ${symptomId} deleted.`);
      fetchSymptoms(); // Refresh the table after deletion
    } else {
      console.error("Failed to delete symptom:", await response.json());
    }
  } catch (error) {
    console.error("Error deleting symptom:", error);
  }
}

// Fetch symptoms on page load
fetchSymptoms();

// Handle form submission
symptomForm.addEventListener("submit", async (event) => {
  event.preventDefault();

  const symptomInput = document.getElementById("symptom");

  const symptomData = {
    user_id: 1, // Static user ID for now
    symptoms: [symptomInput.value], // Send symptom as an array
  };

  try {
    const response = await fetch(`${API_BASE_URL}/symptoms`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(symptomData),
    });

    if (response.ok) {
      symptomInput.value = ""; // Clear the input field
      fetchSymptoms(); // Refresh the table
    } else {
      console.error("Failed to add symptom:", await response.json());
    }
  } catch (error) {
    console.error("Error adding symptom:", error);
  }
});

// Handle diagnosis generation using ChatGPT API
diagnoseButton.addEventListener("click", async () => {
  try {
    const rows = Array.from(symptomTable.querySelectorAll("tr"));
    const symptoms = rows.map((row) => row.cells[0].innerText);

    if (symptoms.length === 0) {
      diagnosisResult.innerText = "No symptoms entered.";
      return;
    }

    const response = await fetch(`${API_BASE_URL}/diagnose`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ symptoms }),
    });

    if (response.ok) {
      const data = await response.json();
      diagnosisResult.innerHTML = `<p>Possible Diagnoses:</p><ul>${data.diagnosis
        .split("\n")
        .map((line) => `<li>${line}</li>`)
        .join("")}</ul>`;
    } else {
      diagnosisResult.innerText = "Failed to generate diagnosis.";
      console.error("Error:", await response.json());
    }
  } catch (error) {
    diagnosisResult.innerText = "Error generating diagnosis.";
    console.error("Error:", error);
  }
});

async function resetSymptomsOnLoad() {
  try {
    const response = await fetch(`${API_BASE_URL}/reset`, {
      method: "DELETE",
    });

    if (response.ok) {
      console.log("Symptoms reset successfully.");
    } else {
      console.error("Failed to reset symptoms:", await response.json());
    }
  } catch (error) {
    console.error("Error resetting symptoms:", error);
  }
}

// Call reset function on page load
document.addEventListener("DOMContentLoaded", async () => {
  await resetSymptomsOnLoad();
  symptomTable.innerHTML = "";
  diagnosisResult.innerText = "";
  fetchSymptoms();  // Fetch fresh data
});
