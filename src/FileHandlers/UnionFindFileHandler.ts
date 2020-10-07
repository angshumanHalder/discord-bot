import { MessageAttachment } from "discord.js";
import * as path from "path";
import { ReplyMessage } from "../CommandHandler/CommandHandler";

export class UnionFindFileHandler {
  private static directory = path.join(
    __dirname,
    `/../`,
    process.env.FILE_DIRECTORY!,
    "data-structures"
  );

  private static UNION_FIND = "/UnionFind/UnionFind.py";

  static handleUnf(): ReplyMessage {
    const fileDir = path.join(
      UnionFindFileHandler.directory,
      UnionFindFileHandler.UNION_FIND
    );
    return new MessageAttachment(fileDir);
  }
}
