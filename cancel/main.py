# -*- coding: utf8 -*-
import os
from flask import Flask, request, render_template, request, redirect, url_for, jsonify
from flask_discord import DiscordOAuth2Session, requires_authorization
from discord import Webhook, RequestsWebhookAdapter
webhook = Webhook.partial(814742019489660939, "rvSBVHtGPflSASjeGEEKdZxC5Z_w1UM_ovc_xD0ZPcFy1UeUybFM4ClGANu6CEWTQame", adapter=RequestsWebhookAdapter())
run_webhook = Webhook.partial(804602090537091072, "6ZMww14Nh7OVeeHUt5bWeixreoWQmSzPVfFmIpU3BEr8OYLGqickY1VyoqH2IeMs1Kd8", adapter=RequestsWebhookAdapter())
app = Flask(__name__)

app.secret_key = b"%\xe0'\x01\xdeH\x8e\x85m|\xb3\xffCN\xc9g"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "false"

app.config["DISCORD_CLIENT_ID"] = "801279922722045962"
app.config["DISCORD_CLIENT_SECRET"] = "zosKMQ95etnO1dZv7D5vet7TyVhyXwt5"  # Discord client secret.
# app.config["DISCORD_REDIRECT_URI"] = "http://localhost:2222/callback"  # URL to your callback endpoint.
app.config["DISCORD_REDIRECT_URI"] = "https://partner-c.alphakr.xyz/callback"  # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = "ODAxMjc5OTIyNzIyMDQ1OTYy.YAeYFA.G9TddtDdPZ3Xlb7AAHD6ddVWVbY"
discord = DiscordOAuth2Session(app)

def on_json_loading_failed_return_dict(e):  
    return '없음'

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('form/1.html')

@app.route("/login", methods=["GET"])
def login():
	if not discord.authorized:
		return discord.create_session(scope=['guilds', 'email', 'identify'])
	else:
		return render_template("login.html")

@app.route("/callback", methods=["GET", "POST"])
def callback():
	data = discord.callback()
	redirect_to = data.get("redirect", "/form/1")
	return redirect(redirect_to)

@app.route("/logout", methods=['GET', 'POST'])
def logout():
	if discord.authorized:
		discord.revoke()
		return redirect(url_for("index"))
	else:
		return redirect(url_for("index"))

@app.route('/form/1', methods=['GET','POST'])
def form1():
	if request.method == 'GET':
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			user = discord.fetch_user()
			return render_template('form/1.html', user=user)
		else:  #로그인이 안되어있는가?
			return redirect(url_for("login"))
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			user = discord.fetch_user()
			run_webhook.send(f"⛔ [ 403 ERROR ] {user}님이 파트너 신청 1단계 페이지에 정상적이지 않은 접근을 시도 했습니다.")
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
		else:  #로그인이 안되어있는가?
			ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
			run_webhook.send(f"⛔ [ 403 ERROR ] 비 로그인 유저({ip})가 파트너 신청 1단계 페이지에 정상적이지 않은 접근을 시도 했습니다.")
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"

@app.route('/form/action', methods=['GET','POST'])
def action():
	if request.method == 'GET':
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			user = discord.fetch_user()
			run_webhook.send(f"⛔ [ 403 ERROR ] {user}님이 파트너 신청 결과 전송 페이지에 정상적이지 않은 접근을 시도 했습니다.")
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
		else:  #로그인이 안되어있는가?
			ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
			run_webhook.send(f"⛔ [ 403 ERROR ] 비 로그인 유저({ip})가 파트너 신청 결과 전송 페이지에 정상적이지 않은 접근을 시도 했습니다.")
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			code = request.form['code']
			nickname = request.form['nickname']
			if etc_text == '':
				etc_text = 'Unknown'
			webhook.send(f"<@627292715956043785>\n✅ 파트너 철회 신청이 도착했습니다.\n\n파트너 코드: {code}, 신청자: {nickname}")
			return render_template('form/action.html')
		else:  #로그인이 안되어있는가?
			return redirect(url_for("index"))

@app.route('/guide/<id>', methods=['GET', 'POST'])
def guide(id):
	return f"<script>location.replace('https://team-alpha-kr.github.io/Partner-Guide/{id}.html');</script>"
		
# S: 2021 파트너 웹사이트 개편 코드

# S: 210210 공지사항
@app.route('/notice/<id>', methods=['GET', 'POST'])
def notice(id):
	return render_template(f"2021temp/notice/{id}.html")
# E: 210210 공지사항

# E: 2021 파트너 웹사이트 개편 코드

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

run_webhook.send("✅ 파트너 신청 철회 - 웹사이트가 실행이 되었습니다!")

app.run(host='0.0.0.0', port=2222, debug=False)