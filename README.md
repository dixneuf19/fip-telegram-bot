# FIP Telegram Bot

[![Test](https://github.com/dixneuf19/SpotifyAPI/workflows/Test/badge.svg)](https://github.com/dixneuf19/SpotifyAPI/actions?query=workflow%3ATest) [![Build and release](https://github.com/dixneuf19/SpotifyAPI/workflows/Build%20and%20release/badge.svg)](https://github.com/dixneuf19/SpotifyAPI/actions?query=workflow%3A"Build+and+release") [![CodeQL](https://github.com/dixneuf19/SpotifyAPI/workflows/CodeQL/badge.svg)](https://github.com/dixneuf19/SpotifyAPI/actions?query=workflow%3ACodeQL)

A Telegram bot to share your love of FIP

## Env variables

- **BOT_TELEGRAM_TOKEN**: the token for the bot
- **FIP_API_HOST** and **FIP_API_PORT** : for the RadioFrance/FIP service
- **SPOTIFY_API_HOST** and **SPOTIFY_API_PORT**: for the Spotify API service

## Local development

You can run locally with `make dev`

You can build the *Docker* image with `make build` and then run it with `make run`.

## Create k8s secret

Add your BOT_TELEGRAM_TOKEN token into your `.env` file for development (**don't commit this file**).

Then you can create the secret with `kubectl create secret generic spotify-api-access --from-env-file=.env`.
