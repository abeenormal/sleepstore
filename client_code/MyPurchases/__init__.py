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
  def __init__(self, user_email, purchase_name, quantity, **properties):
   
       
    # Set Form properties and Data Bindings.
    self.email_name_label = user_email
    self.purchase_label = purchase_name
    self.quantity_label = quantity
    
    self.init_components(**properties)
 
    self.load_products(user_email)
  
    
  
  def load_products(self, user_email):
    user = anvil.users.get_user()
    if user:
     anvil.server.call('get_purchased_items')    
    self.repeating_panel_1.items = self.items
    
   
        
   
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  
   

   
  