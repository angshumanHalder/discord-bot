import { Message, MessageAttachment } from "discord.js";
import { LinkedListFileHandler } from "../FileHandlers/LinkedListFileHandler";
import { Commands } from "./Commands";
import { COMMAND_NOT_FOUND, HELP } from "../helpers/messages";

type replyMessage = string | MessageAttachment;

export class CommandHandler {
  processCommand(receivedMessage: Message): void {
    let fullCommand = receivedMessage.content.substr(1);
    let splitCommand = fullCommand.split(" ");
    let primaryCommand = splitCommand[0];

    const message = this.handleCommand(primaryCommand);
    receivedMessage.channel.send(message);
  }

  private handleHelpCommand(): replyMessage {
    return HELP;
  }

  private handleCommand(command: string): replyMessage {
    switch (command) {
      case Commands.DLL:
        return LinkedListFileHandler.handleDLL();
      case Commands.SLL:
        return LinkedListFileHandler.handleSLL();
      case Commands.HELP:
        return this.handleHelpCommand();
      default:
        return COMMAND_NOT_FOUND;
    }
  }
}
