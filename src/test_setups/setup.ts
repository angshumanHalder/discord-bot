/* Entry point of the application */
import "dotenv/config";
import { Bot } from "../Bot";

// Uses a singleton class instance to avoid name conflicts
export const bot = Bot.getInstance();

bot.connect();
