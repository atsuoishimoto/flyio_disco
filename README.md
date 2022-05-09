1. flyctl.launch

`? Overwrite "/????????/flyio_disco/Dockerfile"?` で、必ず `No` を選択する。

```
Creating app in /Users/ishimoto/src/flyio/flyio_disco
Scanning source code
Detected a Django app
? Overwrite "/Users/ishimoto/src/flyio/flyio_disco/Dockerfile"? No
? App Name (leave blank to use an auto-generated name):
Automatically selected personal organization: Atsuo Ishimoto
? Select region: nrt (Tokyo, Japan)
Created app crimson-thunder-6278 in organization personal
Set secrets on crimson-thunder-6278: SECRET_KEY
Wrote config file fly.toml
? Would you like to setup a Postgresql database now? No
Your app is ready. Deploy with `flyctl deploy`
```

2. 1.で生成される `fly.toml` はbot用としては不適切なので、`samle.fly.toml` を参照に修正する

3. flyctl volumes create bot_data --region nrt --size 1

4. flyctl secrets set DISCORDBOT_TOKEN=xxxxxxxxxxxxxxxxxxxx

5. flyctl deploy
