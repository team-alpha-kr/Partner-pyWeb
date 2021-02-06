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
app.config["DISCORD_REDIRECT_URI"] = "http://partner.alphakr.xyz/callback"  # URL to your callback endpoint.
app.config["DISCORD_BOT_TOKEN"] = "ODAxMjc5OTIyNzIyMDQ1OTYy.YAeYFA.G9TddtDdPZ3Xlb7AAHD6ddVWVbY"
discord = DiscordOAuth2Session(app)

def on_json_loading_failed_return_dict(e):  
    return '없음'

@app.route('/', methods=['GET','POST'])
def index():
	return render_template('index.html')

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

@app.route('/form/2', methods=['GET','POST'])
def form2():
	if request.method == 'POST':
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			privacy = request.form['privacy']
			nickname = request.form['nickname']
			return render_template('form/2.html', privacy=privacy, nickname=nickname)
		else:  #로그인이 안되어있는가?
			return redirect(url_for("login"))
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			user = discord.fetch_user()
			run_webhook.send(f"⛔ [ 403 ERROR ] {user}님이 파트너 신청 2단계 페이지에 정상적이지 않은 접근을 시도 했습니다.")
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
		else:  #로그인이 안되어있는가?
			ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)
			run_webhook.send(f"⛔ [ 403 ERROR ] 비 로그인 유저({ip})가 파트너 신청 2단계 페이지에 정상적이지 않은 접근을 시도 했습니다.")
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"

@app.route('/form/3', methods=['GET','POST'])
def form3():
	if request.method == 'POST':
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			privacy = request.form['privacy']
			nickname = request.form['nickname']
			server = request.form['server']
			member = request.form['member']
			category = request.form['category']
			etc_text = request.form['etc_text']
			return render_template('form/3.html', privacy=privacy, nickname=nickname, server=server, member=member, category=category, etc_text=etc_text)
		else:  #로그인이 안되어있는가?
			return redirect(url_for("login"))
	else:
		if discord.authorized:  #로그인이 되어있는가
			try:
				discord.fetch_guilds()  #로그인정보을 가져와라
			except:
				return redirect(url_for("logout"))  #못가져오면 로그아웃
			return "<script>alert('정상적이지 않은 접근입니다.');location.replace('/');</script>"
		else:  #로그인이 안되어있는가?
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
			privacy = request.form['privacy']
			nickname = request.form['nickname']
			server = request.form['server']
			member = request.form['member']
			category = request.form['category']
			etc_text = request.form['etc_text']
			message = request.form['message']
			image = request.form['image']
			video = request.form['video']
			webhook.send(f"<@627292715956043785>\n✅ 파트너 신청이 도착했습니다.\n\n개인정보처리방침 동의 여부: {privacy}\n신청자: {nickname}\n서버(초대 링크): {server}\n멤버 수: {member}\n컨셉 정보: {category}, {etc_text}\n홍보지: {message}\n이미지: {image}\n영상: {video}")
			return render_template('form/action.html')
		else:  #로그인이 안되어있는가?
			return redirect(url_for("index"))

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