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
- 🤖 **Dialogflow**: For NLP and handling user interactions.
- 🌍 **Ngrok**: To expose the local server to the internet.
- 🖥️ **PyCharm**: Development environment for coding and debugging.
- 💰 **Currency Converter API**: To fetch live exchange rates.
- 🐍 **Python & Flask**: Backend server to process requests.
- ✈️ **Telegram Bot API**: To communicate with Telegram users.

## Installation & Setup ⚙️

### Prerequisites 📌
Ensure you have the following installed:
- 🐍 Python 3.x
- 🔥 Flask
- 🌍 Ngrok
- 🤖 A Telegram bot token (from @BotFather)
- 🧠 Dialogflow agent setup
- 💰 Currency Converter API key

### Steps 🏗️
1. 📥 Clone this repository:
   ```sh
   git clone https://github.com/yourusername/currency-converter-chatbot.git
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



