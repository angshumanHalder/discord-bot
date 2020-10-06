import * as Discord from "discord.js";
import { MessageHandler } from "./MessageHandler/MessageHandler";

export class Bot {
  private static instance: Bot;

  private client: Discord.Client = new Discord.Client();
  private messageHandler: MessageHandler = new MessageHandler();

  private constructor() {
    this.initializeClient();
  }

  private initializeClient(): void {
    if (!this.client) return;

    this.setReadyHandler();
    this.messageHandler.setMessageHandler(this.client);
  }

  private setReadyHandler(): void {
    this.client.on("ready", () => {
      console.log(`Logged in as ${this.client.user?.tag}!`);
    });
  }

  static getInstance(): Bot {
    if (!Bot.instance) {
      Bot.instance = new Bot();
    }
    return Bot.instance;
  }

  connect(): void {
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
