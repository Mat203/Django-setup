let nickname = prompt("Please enter your nickname:");

const chatSocket = new WebSocket("ws://127.0.0.1:8000/ws");

const messagesContainer = document.getElementById('messages');
const nameInput = document.getElementById('name');
const messageInput = document.getElementById('message');

nameInput.value = nickname;

const cachedMessages = JSON.parse(localStorage.getItem('chatMessages')) || [];
const cleanHistoryButton = document.getElementById('clean-history');
cachedMessages.forEach(msg => writeToScreen(msg.user, msg.text, msg.type));

messageInput.addEventListener('keydown', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault(); 
        sendMessage();
    }
});


function sendMessage() {
    const name = nameInput.value;
    const message = messageInput.value;
    console.log('messageInput', messageInput);

    if (name.trim() === '' || message.trim() === '') {
        alert('Please enter both name and message.');
        return;
    }
    chatSocket.send(JSON.stringify({
        'user': name,
        'text': message
    }));
    messageInput.value = ''
}

function writeToScreen(user, message) {
    const p = document.createElement('p');
    p.style.margin = '20px';
    p.className = user === nickname ? 'sent' : 'received';
    p.innerHTML = `<strong>${user}:</strong> ${message}`;
    messagesContainer.appendChild(p);

    messagesContainer.scrollTop = messagesContainer.scrollHeight;

    cachedMessages.push({user, text: message, type: p.className});
    localStorage.setItem('chatMessages', JSON.stringify(cachedMessages));
}

chatSocket.onmessage = function(e) {
    const message = e.data;
    const wholeMessageJSON = JSON.parse(message);
    const beMessageJSON = JSON.parse(wholeMessageJSON.yourMsg);
    
    console.log(beMessageJSON)
    const type = beMessageJSON.user === nameInput.value ? 'sent' : 'received';
    writeToScreen(beMessageJSON.user, beMessageJSON.text, type)
};

cleanHistoryButton.addEventListener('click', function() {
    while (messagesContainer.firstChild) {
        messagesContainer.removeChild(messagesContainer.firstChild);
    }

    localStorage.removeItem('chatMessages');
});
