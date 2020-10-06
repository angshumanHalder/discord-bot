import * as Discord from "discord.js";
import { MessageHandler } from "./MessageHandler/MessageHandler";

// Main Bot class.
export class Bot {
  // Singleton instance that will be used accross the application
  private static instance: Bot;

  // client instance
  private client: Discord.Client = new Discord.Client();

  // handles message
  private messageHandler: MessageHandler = new MessageHandler();

  private constructor() {
    this.initializeClient();
  }

  private initializeClient(): void {
    if (!this.client) return;

    // sets on ready listener to client.
    this.setReadyHandler();

    // Every message that is sent to the bot is passed to message handler
    this.messageHandler.setMessageHandler(this.client);
  }

  private setReadyHandler(): void {
    // Here we can do initial setup of the client
    this.client.on("ready", () => {
      console.log(`Logged in as ${this.client.user?.tag}!`);
    });
  }

  static getInstance(): Bot {
    // Static method to get the instance of Bot
    if (!Bot.instance) {
      Bot.instance = new Bot();
    }
    return Bot.instance;
  }

  connect(): void {
    // The methods logs in to discord
    this.client
      .login(process.env.BOT_TOKEN)
      .then((_) => {
        console.log("Bot connected successfully to Discord!");
      })
      .catch((err) => {
        console.log(`Could not connect to Discord. Error: ${err}`);
      });
  }
}
