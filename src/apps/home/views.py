"""
Views for home app
"""

import datetime, json
import dateutil.relativedelta

from flask import render_template, url_for, redirect, jsonify

from src.libs import AuthorizedView
from .modules import DashboardModule

class DashboardView(AuthorizedView):
    """
    View for dashboard
    """
    def __init__(self):
        self.module = DashboardModule()

    def get(self):
        context = locals()
        return render_template("home/dashboard.html", title = "Dashbaord", **context)

    def post(self):
        pass

