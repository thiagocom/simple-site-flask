# -*- coding: utf-8 -*-
from flask import Flask, render_template
import os
from config import Config, DevelopmentConfig, ProductionConfig

def select_config_class(env):
	if env == "production":
		config_class = ProductionConfig
	elif env == "development":
		config_class = DevelopmentConfig
	else:
		config_class = Config
	return config_class

config_class = select_config_class(os.getenv("FLASK_ENV"))

app = Flask(__name__)
app.config.from_object(config_class)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
	return render_template("index.html")
