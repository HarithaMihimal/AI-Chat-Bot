function addMessageToChat(role, text) {
    const chatBox = document.getElementById("chat-box");
    const message = document.createElement("div");
    message.className = role;
    message.innerText = text;
    chatBox.appendChild(message);
    chatBox.scrollTop = chatBox.scrollHeight;
}

async function sendMessage() {
    const userInput = document.getElementById("user-input");
    const userMessage = userInput.value.trim();

    if (userMessage) {
        addMessageToChat("user", userMessage);
        userInput.value = "";

        const response = await fetch("/send_message", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ message: userMessage }),
        });

        const data = await response.json();
        addMessageToChat("model", data.response);
    }
}
