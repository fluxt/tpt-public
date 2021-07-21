# Twitch Predictions Tools

Twitch Predictions is a fun feature in Twitch where viewers can interact with each other by placing 'bets' with their virtual currency (No cash involved, really).

![](https://github.com/fluxt/tpt-public/blob/main/figures/channel-points-viewer-prediction-voting.gif?raw=true)

After the event ends, viewers are divided the points like horseracing does, called the [Parimutel System.](https://en.wikipedia.org/wiki/Parimutuel_betting)

## Logistic Regression over GraphQL

This repository contains code that utilizes Twitch's GraphQL API and RiotAPI to predict if a streamer playing League of Legends will win not.

![](https://github.com/fluxt/tpt-public/blob/main/figures/lol_stats.png?raw=true)

Based on these League of Legends match "event" stats and GraphQL data, based and by extrapolating useful features, we can calculate optimal p value that maximizes the EV of my virtual poitns.

Subsequently, by using a JavaScript userscript, we can observe that the program is efficient at gaining points.

![](https://github.com/fluxt/tpt-public/blob/main/figures/gains.png?raw=true)
