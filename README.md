# RhodiumCoin Tip Bot

This is a Discord bot that can transfer RHOX between users. It supports:

- Deposit RHOX
- Tip RHOX to Discord users
- See your account info and RHOX balance
- Withdraw RHOX to your wallet

## Installation

**Requirements**

- MongoDB
- walletd (wallet daemon)
- RhodiumCoind (coin daemon)
- Python 3.6
- [Discord Bot Token](https://discordapp.com/developers/applications/me)

I recommend using `supervisor` to keep `RhodiumCoind`, `walletd`
and `bot.py` running.

Here are some sample configs:

```ini
[program:bot]
command = /path/to/bin/python /path/to/rhodiumcoin-tip-bot/rhodiumcoin_tip_bot/bot.py
user = user
autostart = yes
autorestart = yes
environment = LC_ALL="C.UTF-8",LANG="C.UTF-8"

[program:RhodiumCoind]
command = /path/to/RhodiumCoind
user = user
autostart = true
autorestart = true
directory = /path/to
environment=HOME="/home/user"

[program:walletd]
command = /path/to/walletd --container-file wallet/tip_wallets --container-password ******
user = user
autostart = true
autorestart = true
directory = /path/to
environment=HOME="/home/user"
```

You will also need to make a copy of `config.yml.sample` to `config.yml` and
change the values so they work with your setup.

## CryptoNote compatibility

This project can most certainly be adapted to any
[CryptoNote](https://github.com/forknote/cryptonote-generator) coin.
You most likely won't have to change much.

- Change or remove the regex validation in `rhodiumcoin_tip_bot.models:WalletAddressField`
to match the address prefix of your coin.
- Adapt the `RHODIUMCOIN_DIGITS` and `RHODIUMCOIN_REPR` to match your coin.

## Usage

**Discord Commands**

- `$register <wallet_address>`: Register a wallet to your account.
Will be used to withdraw later.
- `$info`: See your deposit and withdrawal addresses.
- `$balance`: See your current available and pending balance.
- `$tip <user_mention> <amount>`: Tip `<amount>` RHOX to `<user_mention>`.
- `$withdraw <amount>`: Withdraws `<amount>` to your registered
withdrawal address.

## Local Env. Setup

This project uses `Pipfile`, `pipenv` and `tox`. To setup your environment
simply run `tox`. You can check the `tox.ini` file to see available environments
and commands that run within each of them.
