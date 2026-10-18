from app import create_app
from app.utils.cron_job import self_ping

from configs import Config
from threading import Thread

app = create_app()

if Config.RENDER_EXTERNAL_URL:
    Thread(target=self_ping, daemon=True).start()

if __name__ == "__main__":
    app.run()
