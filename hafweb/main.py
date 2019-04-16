# encoding = 'utf-8'
import argparse

from hafweb.route.route import *
from hafweb.route.route_api import *
from hafweb.route.route_token import *
from hafweb.controller.controller import *


def main():

    arg_program = argparse.ArgumentParser(prog="python -m hafweb", add_help=True)

    sub_all_arg_program = arg_program.add_subparsers(dest="all")

    sub_run_arg_program = sub_all_arg_program.add_parser("run",
                                                         help="run web, using `python -m hafweb run` to run the web server ")
    sub_run_arg_program.add_argument("--port", "-p", dest="port", type=int, default="8081",
                                     help="the port of web server")
    sub_run_arg_program.add_argument("--sql-server", "-ss", dest="sql_server", type=str, default="", required=True,
                                     help="db sql server : user:pass@host:port/db")
    args = arg_program.parse_args()
    engine_maker.bind_sql_server(args)
    Controller.bind_all()
    ControllerApi.bind_all()
    if hasattr(args, 'port'):
        app.run(host='0.0.0.0', debug=False, port=WEB_SERVER_PORT if args.port==8081 else args.port)
    else:
        app.run(host='0.0.0.0', debug=False, port=WEB_SERVER_PORT)


if __name__ == "__main__":
    main()