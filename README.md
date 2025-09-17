# rollover-notifier
Scrapes the national lottery website and notify users through a Discord webhook of any national lottery rollovers. Runs in a docker container scheduled on a cron job on the days the draws are run on. For the national lottery that's Wednesday and Saturday. For the Euromillions that's Tuesday and Fridays.

The following is returned in the Discord notification:

🎰 National Lottery Daily Update DD/MM/YYYY
- Lotto: £11.3M
- Euromillions: £119M
