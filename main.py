# -*- coding: utf8 -*-
import os
from flask import Flask, request, render_template, request, redirect, url_for, jsonify
from flask_discord import DiscordOAuth2Session, requires_authorization
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.partial(801329269879603281, "ZfG6b_V4UlsdZTh91poYC9nyibSvE04gsKUx1NH2Z2gPWNp6YUVXYF6zLRVs_1ut3Nnr", adapter=RequestsWebhookAdapter())

app = Flask(__name__)

app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "false"

app.config["DISCORD_CLIENT_ID"] = "801279922722045962"
app.config["DISCORD_CLIENT_SECRET"] = "zosKMQ95etnO1dZv7D5vet7TyVhyXwt5"  # Discord client secret.
app.config["DISCORD_REDIRECT_URI"] = "http://alphakr.xyz:8080/callback"  # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = "ODAxMjc5OTIyNzIyMDQ1OTYy.YAeYFA.G9TddtDdPZ3Xlb7AAHD6ddVWVbY"
discord = DiscordOAuth2Session(app)

@app.route('/', methods=['GET','POST'])
def index():
	if discord.authorized:  #로그인이 되어있는가
		try:
			discord.fetch_guilds()  #로그인정보을 가져와라
		except:
			return redirect(url_for("logout"))  #못가져오면 로그아웃
		return render_template('agreeForm.html')
	else:  #로그인이 안되어있는가?
		return redirect(url_for("login"))

@app.route("/login", methods=["GET"])
def login():
	if not discord.authorized:
		return discord.create_session(scope=['guilds', 'email', 'identify'])
	else:
		return render_template("login.html")

@app.route('/agreeAction', methods=['GET','POST'])
def agree():
	if request.method == 'GET':
		return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			user = discord.fetch_user()
			webhook.send(f'✅ `{user}` 님이 이용약관, 개인정보처리방침에 동의했습니다.')
			return render_template('agreeAction.html')
		else:  #로그인이 안되어있는가?
			return redirect(url_for("index"))

@app.route('/disagreeCheck', methods=['GET','POST'])
def disagree_check():
	if request.method == 'GET':
		return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			return render_template('disagreeCheck.html')
		else:  #로그인이 안되어있는가?
			return redirect(url_for("index"))

@app.route('/agreeCheck', methods=['GET','POST'])
def agree_check():
	if request.method == 'GET':
		return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			return render_template('agreeCheck.html')
		else:  #로그인이 안되어있는가?
			return redirect(url_for("index"))


@app.route('/disagreeAction', methods=['GET','POST'])
def disagree():
	if request.method == 'GET':
		return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			user = discord.fetch_user()
			webhook.send(f'✅ `{user}` 님이 이용약관, 개인정보처리방침에 동의하지 않았습니다.')
			return render_template('agreeAction.html')
		else:  #로그인이 안되어있는가?
			return redirect(url_for("index"))

@app.route("/callback", methods=["GET", "POST"])
def callback():
	data = discord.callback()
	redirect_to = data.get("redirect", "/")
	return redirect(redirect_to)

@app.route("/logout", methods=['GET'])
def logout():
	if discord.authorized:
		discord.revoke()
		return redirect(url_for("index"))
	else:
		return redirect(url_for("index"))

webhook.send("✅ 웹사이트가 실행이 되었습니다!")
# app.run(host='0.0.0.0', port=5000, debug=False)
app.run(host='0.0.0.0', port=8080, debug=False)
# app.run(host='0.0.0.0', port=5000, debug=True)
