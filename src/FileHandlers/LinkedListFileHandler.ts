import { MessageAttachment } from "discord.js";
import * as path from "path";

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

  static handleDLL(): MessageAttachment {
    const fileDir = path.join(
      LinkedListFileHandler.directory,
      LinkedListFileHandler.DOUBLY_LINKED_LIST_FILE
    );
    return new MessageAttachment(fileDir);
  }

  static handleSLL(): MessageAttachment {
    const fileDir = path.join(
      LinkedListFileHandler.directory,
      LinkedListFileHandler.SINGLY_LINKED_LIST_FILE
    );
    return new MessageAttachment(fileDir);
  }
}
