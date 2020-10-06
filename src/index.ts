import "dotenv/config";
import { Bot } from "./Bot";

const bot = Bot.getInstance();
bot.connect();
