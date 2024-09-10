// chat.js
document.getElementById('chat-form').onsubmit = function(event) {
    event.preventDefault();
    const messageInput = document.getElementById('message-input');
    const message = messageInput.value.trim();
    messageInput.value = '';

    if (message) {
        const chatBox = document.getElementById('chat-box');
        const userMessage = document.createElement('div');
        userMessage.textContent = `You: ${message}`;
        chatBox.appendChild(userMessage);

        // Send the message to the server
        fetch('/send_message', {
            method: 'POST',
            body: new URLSearchParams({'message': message}),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
        .then(response => response.json())
        .then(data => {
            const serverMessage = document.createElement('div');
            serverMessage.textContent = `Server: ${data.message}`;
            chatBox.appendChild(serverMessage);
        })
        .catch((error) => {
            console.error('Error:', error);
        });
    }
};
