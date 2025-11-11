from ._anvil_designer import RowTemplate1Template
from anvil import *
import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class RowTemplate1(RowTemplate1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    user_email = orders('user_email')
    self.data_grid_1.self.repeating_panel_1.items=anvil.server.call('get_user_purchases', user_email)

    # Any code you write here will run before the form opens.
     