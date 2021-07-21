from flask import Flask, render_template, jsonify, request
import logging
import os
from FetchData.Fetch import *


def create_server():
    app = Flask(__name__)


    @app.route('/')
    def main_page():
        return render_template("index.html")

    @app.route('/upload-file', methods=['POST'])
    def get_file():
        dfile = request.files['dfile']

        file_name = dfile.filename
        file_extension = file_name.split(".")[-1]

        response = fetch_extension_data(file_extension)
        data = {
            "extension":file_extension,
            "isProgramming": False,
            "status": True,
            "summary": "",
        }

        print(len(response))

        if len(response) == 0:
            data["status"] = False
        if len(response) == 1:
            data["summary"] = response[0]
        if len(response) == 2:
            data["summary"] = response[0]
            data["isProgramming"] = True

        return jsonify(data)

    app.run("127.0.0.1", 5000)

def create_summary_stats_server(extension_summary,extension_count,program_supported_temp):
    print(program_supported_temp)
    app = Flask(__name__)

    @app.route('/')
    def main_page():
        return render_template("stats.html",extension_count=extension_count,extension_summary=extension_summary,
                            programs = program_supported_temp)

    app.run("127.0.0.1", 8000)

