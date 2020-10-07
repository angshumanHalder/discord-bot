import { MessageAttachment } from "discord.js";
import * as path from "path";
import { ReplyMessage } from "../CommandHandler/CommandHandler";
import { FILE_NOT_FOUND } from "../helpers/messages";

export class LinkedListFileHandler {
  private static directory = path.join(
    __dirname,
    `/../`,
    process.env.FILE_DIRECTORY!,
    "data-structures"
  );

  private static DOUBLY_LINKED_LIST_FILE =
    "/DoublyLinkedList/DoublyLinkedList.py";
  private static SINGLY_LINKED_LIST_FILE =
    "/SinglyLinkedList/SinglyLinkedList.py";

  static handleDLL(): ReplyMessage {
    const fileDir = path.join(
      LinkedListFileHandler.directory,
      LinkedListFileHandler.DOUBLY_LINKED_LIST_FILE
    );
    try {
      return new MessageAttachment(fileDir);
    } catch (err) {
      return FILE_NOT_FOUND;
    }
  }

  static handleSLL(): ReplyMessage {
    const fileDir = path.join(
      LinkedListFileHandler.directory,
      LinkedListFileHandler.SINGLY_LINKED_LIST_FILE
    );
    try {
      return new MessageAttachment(fileDir);
    } catch (err) {
      return FILE_NOT_FOUND;
    }
  }
}
