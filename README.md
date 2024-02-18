# Chat Application (HW_9)

This is a real-time chat application built with Django and WebSockets. It features a responsive and user-friendly interface. The application also caches chat history in the browser's local storage, so you won't lose your messages when you refresh the page.

## Features

### Real-Time Chat

The application uses WebSockets to enable real-time communication between the server and the client. Messages are sent and received instantly, providing a seamless chat experience.

### Responsive Design

The chat interface is designed to be responsive and works well on both desktop and mobile devices. It uses Bootstrap for layout and styling

### Caching Chat History

The application caches the chat history in the browser's local storage. This means that your messages are saved locally on your device and will still be there when you refresh the page or come back later.

### Scrollable Message Container

The message container is scrollable and automatically scrolls to the bottom when a new message is added. This keeps the most recent messages in view while still allowing you to scroll up to see older messages.

### Clean Chat History

There is a "Clean Chat History" button that allows you to clear the chat history from both the display and the local storage.

## How to Use

When you first load the page, you will be prompted to enter your nickname. This nickname will be used to identify your messages in the chat.

To send a message, type your message in the "Message" input field and click the "Send" button. Your message will appear in the chat box, distinguished by a specific color (white for your messages, grey for others).

You can switch between dark and light modes by clicking the "Switch to Dark Mode" or "Switch to Light Mode" button.

You can clear the chat history by clicking the "Clean Chat History" button. Please note that this will permanently delete the chat history.
