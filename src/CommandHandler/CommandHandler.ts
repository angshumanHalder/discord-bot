import { Client, Message } from "discord.js";

export class CommandHandler {
  processCommand(receivedMessage: Message) {
    let fullCommand = receivedMessage.content.substr(1);
  }
}
