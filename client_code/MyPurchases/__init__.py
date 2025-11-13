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
  def __init__(self, order, **properties):
   
       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.item = order
   order = []
   self.load_products(order)
  
    
  
  def load_products(self, order):
    user = anvil.users.get_user()
    if user:
     anvil.server.call('get_purchased_items', order='item_name')    
    self.repeating_panel_1.items = order
    
   
        
   
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  
   

   
  