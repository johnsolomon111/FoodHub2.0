from flask import Blueprint, render_template, url_for, session

from app.restaurant.forms import LoginForm
from app.services import get_all_resto

restaurant = Blueprint('restaurant', __name__)

@restaurant.route('/my-restaurants', methods=['GET','POST'])
def restaurants():
  # if session['user'] is None:
  #   form = LoginForm()
  #   message = 'Session expired! Please sign-in again.'
  #   return render_template('login.html', title="Login", form=form, message=message)
  # else:
  #   data = session['user']
  #   restaurants = get_all_resto(data['user_id'])
  #   if restaurants:
  #     restaurant_data = restaurants[0]
  #   else:
  #     restaurant_data = []
  # return render_template('restaurant.html',data=data, resto=restaurant_data, restaurants=restaurants, title='Restaurants')
  return render_template('restaurant.html', title='Restaurants')

