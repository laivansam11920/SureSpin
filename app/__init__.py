from flask import Flask, render_template

def create_app() -> Flask:
    app = Flask(__name__)

    @app.route('/')
    def index():
        WHEEL_ITEMS = [
            {"id": 1, "label": "10.000đ", "color": "#FF5733"},
            {"id": 2, "label": "Chúc may mắn", "color": "#2ECC71"},
            {"id": 3, "label": "50.000đ", "color": "#3498DB"},
            {"id": 4, "label": "Voucher 20%", "color": "#F1C40F"},
            {"id": 5, "label": "Mất lượt", "color": "#E74C3C"},
            {"id": 6, "label": "100.000đ", "color": "#9B59B6"},
        ]
        return render_template('index.html', items=WHEEL_ITEMS)

    return app