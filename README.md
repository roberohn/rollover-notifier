# rollover-notifier
Scrapes the national lottery website and notify users through a Discord webhook of any rollovers happening. Runs in a docker container scheduled on a cronjob daily.

v1 returns the following in the notification:

🎰 National Lottery Weekly Update DD/MM/YYYY
- Lotto: £11.3M
- Lotto Hotpicks: £350K
- Euromillions: £119M
- Euromillions Hotpicks: £1M
- Thunderball: £500K

v2 TBC
I want to next have the app show the days each draw is run on and if the value for an upcoming jackpot is higher than averge.
