function performOperation(operation) {
    let num1 = parseFloat(document.getElementById('num1').value);
    let num2 = parseFloat(document.getElementById('num2').value);

    if (isNaN(num1) || isNaN(num2)) {
        alert("Please enter valid numbers!");
        return;
    }

    let url = `/api/${operation}`;
    let data = { num1: num1, num2: num2 };

    fetch(url, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        if (data.result !== undefined) {
            document.getElementById('result').innerText = data.result;
        } else {
            document.getElementById('result').innerText = "Error: " + data.error;
        }
    })
    .catch(error => {
        console.error("Error:", error);
        document.getElementById('result').innerText = "An error occurred.";
    });
}
