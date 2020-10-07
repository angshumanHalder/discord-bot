import { Client, Message } from "discord.js";
import { CommandHandler } from "../CommandHandler/CommandHandler";
import { DEFAULT_MESSAGE } from "../helpers/messages";

export class MessageHandler {
  private commandHandler: CommandHandler = new CommandHandler();

  setMessageHandler(client: Client): void {
    client.on("message", async (message: Message) => {
      if (message.author.bot) return;
      else if (message.author == client.user) return;

      if (message.content.startsWith("#")) {
        this.commandHandler.processCommand(message);
      } else {
        message.channel.send(DEFAULT_MESSAGE).catch((err) => {
          console.log(err);
        });
      }
    });
  }
}
