"""
Route Configuration for home app
"""
from .views import DashboardView

def init_routes(app):
    app.add_url_rule('/', view_func=DashboardView.as_view('root'))
    app.add_url_rule('/dashboard', view_func=DashboardView.as_view('dashboard'))

if __name__ == "__main__":
    print("Something went wrong...")
