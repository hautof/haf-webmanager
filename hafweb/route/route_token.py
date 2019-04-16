from hafweb.app import app
from haf.config import BANNER_STRS
from hafweb.generator import GeneratorHtml, GeneratorApi
from hafweb.controller.controller import *
from flask import request
from hafweb.error import *
import json


@app.route("/api/v1/token", methods=['GET', 'POST'])
def get_token() -> str:
    if request.method == "POST":
        user_name = request.form.get("username")
        password = request.form.get("password")
        if not user_name or not password:
            request_data = json.loads(request.data)
            user_name = request_data.get("username") or user_name
            password = request_data.get("password") or password
    elif request.method == "GET":
        user_name = request.args.get("username")
        password = request.args.get("password")
    else:
        return GeneratorApi.genrate_api_pure("tokens", status=200)

    print(f"{user_name} -- {password}")
    if not user_name or not password:
        return GeneratorApi.generate_error(ErrorHandler("get_token", "123456", status=401))
    else:
        all_users = ControllerToken.get_user_name_all()
        for user in all_users:
            if user.username == user_name:
                if user.password == password:
                    return GeneratorApi.genrate_api_pure(user.token, status=200)
                else:
                    return GeneratorApi.generate_error(ErrorHandler("get_token", "password is wrong!", status=401))

@app.route("/api/v1/users/me", methods=['GET', 'POST'])
def get_user_me() -> str:
    if request.method == "POST":
        user_name = request.form.get("username")
        password = request.form.get("password")
        if not user_name or not password:
            request_data = json.loads(request.data)
            user_name = request_data.get("username") or user_name
            password = request_data.get("password") or password
    elif request.method == "GET":
        user_name = request.args.get("username")
        password = request.args.get("password")
    else:
        return GeneratorApi.genrate_api_pure("tokens", status=200)

    print(f"{user_name} -- {password}")
    if not user_name or not password:
        return GeneratorApi.generate_error(ErrorHandler("get_token", "123456", status=401))
    else:
        all_users = ControllerToken.get_user_name_all()
        for user in all_users:
            if user.username == user_name:
                if user.password == password:
                    return GeneratorApi.genrate_api_pure(user.token, status=200)
                else:
                    return GeneratorApi.generate_error(ErrorHandler("get_token", "password is wrong!", status=401))