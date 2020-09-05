from flask import Flask

from .main.views import main
from .owner.views import owner
from .customer.views import customer
from .restaurant.views import restaurant

def create_app():

  app = Flask(__name__)
  app.config['SECRET_KEY'] = 'secretsecretsecret'

  app.register_blueprint(main)
  app.register_blueprint(owner, url_prefix="/owner")
  app.register_blueprint(customer, url_prefix="/customer")
  app.register_blueprint(restaurant, url_prefix="/owner")

  return app