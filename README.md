# Currency Converter Savage Chatbot
Name - AKBot

This is a Telegram chatbot that provides currency conversion with a twist—it delivers savage responses while giving you the exchange rates you need. Built using Dialogflow, ngrok, PyCharm, and a currency converter API, this chatbot is both functional and entertaining.

## Features 🚀
- 🔄 Converts currency values between different currencies.
- 😈 Gives sarcastic, witty, and savage responses.
- 🤖 Deployed on Telegram for easy access.
- 🧠 Uses Dialogflow for natural language understanding.
- 🌐 Integrated with a currency converter API for real-time exchange rates.
- 🏠 Hosted locally and exposed to the web via ngrok.

## Technologies Used 🛠️

* 🤖 **Dialogflow:** This platform provides the Natural Language Processing (NLP) capabilities for the chatbot. It handles user interactions by:
    * 🗣️ Understanding Natural Language: Processing user input (text or voice) to discern the meaning.
    * 🎯 Intent Recognition: Identifying the user's goal, which in this case is currency conversion.
    * 🔑 Entity Extraction: Identifying and extracting key pieces of information from the user's query, such as the numerical amount, the source currency, and the target currency.
    * 🔗 Webhook Integration: Facilitating communication with the backend server (built with Python and Flask) by sending structured data about the user's request for fulfillment.

* 🌍 **Ngrok:** This is a reverse proxy tool used primarily during development. It creates a secure tunnel from a public URL to your locally running server. This is essential for:
    * 🏠 Exposing Localhost: Allowing external services like the Telegram Bot API and Dialogflow to send HTTP requests to your bot running on your local machine.
    * 🧪 Simplified Testing: Enabling easy testing and debugging of the chatbot with external platforms without needing to deploy to a public server for every change.

* 🖥️ **PyCharm:** This is the Integrated Development Environment (IDE) used for developing the chatbot's code. It offers features that aid in:
    * ✍️ Code Editing: Providing syntax highlighting, code completion, and error detection for Python development.
    * 🐞 Debugging: Offering tools to step through code, inspect variables, and identify and resolve issues in the bot's logic.
    * 📂 Project Management: Organizing project files, managing dependencies, and integrating with version control systems like Git.

* 💰 **Currency Converter API:** This is a third-party Application Programming Interface that provides real-time currency exchange rates. The chatbot relies on this API to:
    *  # Fetch Live Rates: Obtain the most current exchange rates between different currencies.
    * ⚙️ Data Integration: Allow the backend to programmatically query for specific exchange rates based on the user's request.
    * ✅ Conversion Accuracy: Ensure the chatbot provides accurate currency conversions based on up-to-date market data.

* 🐍 **Python & Flask:** These form the backend of the chatbot, responsible for the core logic and communication:
    * 🐍 Python: The programming language used to write the backend code due to its versatility and extensive libraries.
    * Flask: A lightweight and flexible micro web framework for Python. It is used to:
        * 🔗 Handle Webhooks: Create endpoints (URLs) that can receive HTTP POST requests from Dialogflow containing the user's intent and entities.
        * 🧠 Process Logic: Implement the code to take the extracted information, query the Currency Converter API, perform the calculation, and format the response.
        * ✈️ Interact with Telegram API: Use libraries to communicate with the Telegram Bot API for sending messages back to the user.

* ✈️ **Telegram Bot API:** This is the interface provided by Telegram that allows developers to create and interact with Telegram bots. It enables the chatbot to:
    * 📥 Receive Updates: Get notifications when users interact with the bot (e.g., send a message).
    * 📤 Send Messages: Programmatically send text messages and other content back to the users in Telegram chats, including the converted currency result.
    * 📡 Webhook Registration: Allow the bot to register a URL (often provided by Ngrok during development or a public server in production) where Telegram can send incoming messages and events.

## Installation & Setup ⚙️

### Prerequisites 📌
Ensure you have the following installed:
- 🐍 Python 3.11
- 🔥 Flask
- 🌍 Ngrok
- 🤖 A Telegram bot token (from @BotFather)
- 🧠 Dialogflow agent setup
- 💰 Currency Converter API key

### Steps 🏗️
1. 📥 Clone this repository:
   ```sh
   git clone https://github.com/ArpitKharwade/currency-converter-chatbot.git
   cd currency-converter-chatbot
   ```
2. 📦 Install dependencies:
   ```sh
   pip install flask requests python-telegram-bot google-cloud-dialogflow
   ```
3. 🛠️ Set up Dialogflow:
   - Create an agent in Dialogflow.
   - Train it with custom intents for currency conversion.
   - Get the JSON credentials for authentication.
   
4. 🤖 Set up Telegram bot:
   - Create a bot using @BotFather on Telegram.
   - Get the bot token and add it to your environment variables.
   
5. 💰 Configure the Currency Converter API:
   - Get an API key from a currency conversion service.
   - Store it in the project settings.
   
6. ▶️ Run the Flask server:
   ```sh
   python bot.py
   ```
7. 🌍 Expose the server using ngrok:
   ```sh
   ngrok http 5000
   ```
   - Copy the HTTPS URL and set it as the webhook for your Telegram bot.

## Live Preview 🎥
🔗 [Click here to try the bot](https://t.me/Ak_04_bot)

## Usage 🎯
- 📲 Open Telegram and start chatting with your bot.
- 🔄 Ask for currency conversion, e.g., `Convert 10 USD to EUR`.
- 🤯 Get your exchange rate along with a savage remark.

## Example Interaction 💬
**User:** Convert 100 USD to INR  
**Bot:** Oh, so you're rich now? Fine. 100 USD = 8,300 INR. Don't spend it all at once! 💸

## Contributing 🤝
Feel free to fork this repository and add more savage responses, improve API handling, or enhance NLP.

## License 📜
This project is licensed under the MIT License.

---
Enjoy the sass while converting your cash! 😎



