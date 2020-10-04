import "dotenv/config";
import * as Discord from "discord.js";

const client = new Discord.Client();

client.on("ready", () => {
  // Check if the bot is connected
  console.log(`Connected as ${client.user?.tag}`);

  // List all the servers(guilds) the bot is connected to
  console.log("Servers: ");
  client.guilds.cache.forEach((guild: Discord.Guild): void => {
    console.log(`- ${guild.name}`);
  });

  // List all the channels
  client.channels.cache.forEach((channel): void => {
    console.log(`--${channel.toString()} (${channel.type}) - ${channel.id}`);
  });
});

client.login(process.env.BOT_TOKEN);
