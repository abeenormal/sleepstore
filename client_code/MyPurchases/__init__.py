from ._anvil_designer import MyPurchasesTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.facebook.auth
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..OurProducts import OurProducts
from ..Product import Product






class MyPurchases(MyPurchasesTemplate):
  def __init__(self, order, user_email, **properties):
   
       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.order = order
   self.load_products(order, user_email)
  

  
  def load_products(self, order, user_email):
   self.repeating_panel_1.items = anvil.server.call('get_purchased_items', order='item_name', user_email="user")
   
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  
   

   
  