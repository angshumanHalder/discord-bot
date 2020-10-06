import { Client, Message } from "discord.js";
import { CommandHandler } from "../CommandHandler/CommandHandler";

export class MessageHandler {
  private commandHandler: CommandHandler = new CommandHandler();

  setMessageHandler(client: Client): void {
    client.on("message", async (message: Message) => {
      if (message.author.bot) return;

      if (message.content.startsWith("#")) {
        this.commandHandler.processCommand(message);
      }
    });
  }
}
