# -*- coding: utf8 -*-
import os
from flask import Flask, request, render_template, request, redirect, url_for, jsonify
from flask_discord import DiscordOAuth2Session, requires_authorization
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.partial(804563160521900092, "BzNJjxg3-3uxBL6DtSZysERyr5ZmvvZz1yJ0AH05N_v5DBH7ssfqmuU6QUKfp3cYp_3P", adapter=RequestsWebhookAdapter())
run_webhook = Webhook.partial(804602090537091072, "6ZMww14Nh7OVeeHUt5bWeixreoWQmSzPVfFmIpU3BEr8OYLGqickY1VyoqH2IeMs1Kd8", adapter=RequestsWebhookAdapter())
app = Flask(__name__)

app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "false"

app.config["DISCORD_CLIENT_ID"] = "801279922722045962"
app.config["DISCORD_CLIENT_SECRET"] = "zosKMQ95etnO1dZv7D5vet7TyVhyXwt5"  # Discord client secret.
# app.config["DISCORD_REDIRECT_URI"] = "http://localhost:2052/callback"  # URL to your callback endpoint.
# app.config["DISCORD_REDIRECT_URI"] = "http://partner.alphakr.xyz/callback"  # URL to your callback endpoint.
app.config["DISCORD_REDIRECT_URI"] = "http://alphakr.xyz:2052/callback"  # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = "ODAxMjc5OTIyNzIyMDQ1OTYy.YAeYFA.G9TddtDdPZ3Xlb7AAHD6ddVWVbY"
discord = DiscordOAuth2Session(app)

def on_json_loading_failed_return_dict(e):  
    return '없음'
	
@app.route('/', methods=['GET','POST'])
def index():
	return render_template('serverfix.html')

@app.route('/api/ip', methods=['GET', 'POST'])
def ip():
    return request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

@app.errorhandler(404)
def page_not_found(error):
	return render_template("error/404.html")

@app.errorhandler(500)
def servererror(error):
	run_webhook.send(f"<@673776952578146315> ⛔ [ 500 ERROR ] 서버에 오류가 발생했습니다.")
	return render_template("error/500.html")

@app.errorhandler(400)
def badrequest(error):
	run_webhook.send(f"<@673776952578146315> ⛔ [ 400 ERROR ] 서버에 오류가 발생했습니다.")
	return render_template("error/400.html")

run_webhook.send("✅ 웹사이트가 실행이 되었습니다!")

# app.run(host='0.0.0.0', port=5000, debug=False)
app.run(host='0.0.0.0', port=2052, debug=False)
# app.run(host='0.0.0.0', port=5000, debug=True)