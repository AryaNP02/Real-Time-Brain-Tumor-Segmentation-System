
const result = {
    prediction: "Brain Tumor Detected",
    probability: "80%"
};

// Update the page with the result
document.getElementById("prediction").textContent = result.prediction;
document.getElementById("probability").textContent = result.probability;
