```javascript
document.addEventListener('DOMContentLoaded', (event) => {
    const userInput = document.getElementById('user-input');
    const submitButton = document.getElementById('submit-button');
    const chatOutput = document.getElementById('chat-output');
    const exitButton = document.getElementById('exit-button');

    submitButton.addEventListener('click', () => {
        fetch('/api/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                user_input: userInput.value,
            }),
        })
        .then(response => response.json())
        .then(data => {
            chatOutput.innerHTML += `<p>User: ${userInput.value}</p>`;
            chatOutput.innerHTML += `<p>Bot: ${data.response}</p>`;
            userInput.value = '';
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });

    exitButton.addEventListener('click', () => {
        fetch('/api/exit', {
            method: 'POST',
        })
        .then(() => {
            chatOutput.innerHTML += `<p>Goodbye!</p>`;
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    });
});
```