"""
Views for home app
"""

import datetime, json
import dateutil.relativedelta

from flask import request, render_template, url_for, redirect, jsonify

from src.libs import AuthorizedView, WatsonMixin
from .modules import DashboardModule

class DashboardView(AuthorizedView, WatsonMixin):
    """
    View for dashboard
    """
    def __init__(self):
        super().__init__()
        self.module = DashboardModule()

    def get(self):
        context = locals()
        return render_template("home/index.html", title = "Dashbaord", **context)

    def post(self):
        data = request.form.to_dict()
        url = data.get("url")
        if len(url.strip()) > 0:
            result = self.get_authors(url)
        context = locals()
        return render_template("home/index.html", title = "Dashbaord", **context)

