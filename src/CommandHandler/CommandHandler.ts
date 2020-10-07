import { Message, MessageAttachment } from "discord.js";
import { LinkedListFileHandler, UnionFindFileHandler } from "../FileHandlers";
import { Commands } from "./Commands";
import { COMMAND_NOT_FOUND, FILE_NOT_FOUND, HELP } from "../helpers/messages";

export type ReplyMessage = string | MessageAttachment;

export class CommandHandler {
  async processCommand(receivedMessage: Message): Promise<Message> {
    let fullCommand = receivedMessage.content.substr(1);
    let splitCommand = fullCommand.split(" ");
    let primaryCommand = splitCommand[0];

    try {
      const message = this.handleCommand(primaryCommand);
      return await receivedMessage.channel.send(message);
    } catch (err) {
      return await receivedMessage.channel.send(FILE_NOT_FOUND);
    }
  }

  private handleHelpCommand(): ReplyMessage {
    return HELP;
  }

  private handleCommand(command: string): ReplyMessage {
    switch (command) {
      case Commands.DLL:
        return LinkedListFileHandler.handleDLL();
      case Commands.SLL:
        return LinkedListFileHandler.handleSLL();
      case Commands.UNF:
        return UnionFindFileHandler.handleUnf();
      case Commands.HELP:
        return this.handleHelpCommand();
      default:
        return COMMAND_NOT_FOUND;
    }
  }
}
