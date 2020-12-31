import { Message, MessageAttachment } from "discord.js";
import { Commands } from "./Commands";
import { COMMAND_NOT_FOUND, FILE_NOT_FOUND, HELP } from "../helpers/messages";
import { FileHandler } from "../FileHandlers/FileHandler";
import { Locations } from "../helpers/fileLocations";

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
        return FileHandler.getInstance().handleFile(
          Locations.DOUBLY_LINKED_LIST_FILE
        );
      case Commands.SLL:
        return FileHandler.getInstance().handleFile(
          Locations.SINGLY_LINKED_LIST_FILE
        );
      case Commands.UNF:
        return FileHandler.getInstance().handleFile(Locations.UNION_FIND);
      case Commands.PQ:
        return FileHandler.getInstance().handleFile(Locations.PRIORITY_QUEUE);
      case Commands.IPQ:
        return FileHandler.getInstance().handleFile(
          Locations.INDEXED_PRIORITY_QUEUE
        );
      case Commands.BST:
        return FileHandler.getInstance().handleFile(
          Locations.BINARY_SEARCH_TREE
        );
      case Commands.STACK:
        return FileHandler.getInstance().handleFile(Locations.STACK);
      case Commands.QUE:
        return FileHandler.getInstance().handleFile(Locations.QUEUE);
      case Commands.HASHTABLE:
        return FileHandler.getInstance().handleFile(Locations.HASH_TABLE);
      case Commands.FTREE:
        return FileHandler.getInstance().handleFile(Locations.FENWICK_TREE);
      case Commands.HELP:
        return this.handleHelpCommand();
      default:
        return COMMAND_NOT_FOUND;
    }
  }
}
