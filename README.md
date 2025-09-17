<img width="262" height="262" alt="lotto-bot" src="https://github.com/user-attachments/assets/0f842724-50c0-460d-96f0-78917f348884" />

# rollover-notifier
Scrapes the national lottery website for the current jackpots and notify users through a Discord webhook of any national lottery rollovers. Runs in a docker container scheduled on a cron job on the days the draws are run on. For the national lottery that's Wednesday and Saturday. For the Euromillions that's Tuesday and Fridays.

Generate your webhook on Discord and set an environment variable of `WEBHOOK_URL` in your .env file.

Jackpot data for both games are logged on a Sqlite database called `jackpots.db` with one table named `jackpots`.

The following is returned in the Discord notification:

🎰 National Lottery Daily Update DD/MM/YYYY
- Lotto: £11.3M
- Euromillions: £119M
