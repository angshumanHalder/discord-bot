import { MessageAttachment } from 'discord.js';
import * as path from "path";
import { ReplyMessage } from "../CommandHandler/CommandHandler";
import { FILE_NOT_FOUND } from "../helpers/messages";

export class FileHandler {
    
    public static instance: FileHandler;

    private directory = path.join(__dirname, '/../', process.env.FILE_DIRECTORY!)

    handleFile(filename: string): ReplyMessage {
        const fileDir = path.join(this.directory, filename);
        try {
            return new MessageAttachment(fileDir);
        } catch(err) {
            return FILE_NOT_FOUND;
        }
    }

    static getInstance(): FileHandler {
        if(!FileHandler.instance) {
            FileHandler.instance = new FileHandler();
        }
        return this.instance;
    }
}