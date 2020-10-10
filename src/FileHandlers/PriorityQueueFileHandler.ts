import { MessageAttachment } from "discord.js";
import * as path from "path";
import { ReplyMessage } from "../CommandHandler/CommandHandler";

export class PriorityQueueFileHandler {
  private static directory = path.join(
    __dirname,
    `/../`,
    process.env.FILE_DIRECTORY!,
    "data-structures"
  );

  private static PRIORITY_QUEUE = "/PriorityQueue/PriorityQueue.py";

  static handlePQ(): ReplyMessage {
    const fileDir = path.join(
      PriorityQueueFileHandler.directory,
      PriorityQueueFileHandler.PRIORITY_QUEUE
    );
    return new MessageAttachment(fileDir);
  }
}
