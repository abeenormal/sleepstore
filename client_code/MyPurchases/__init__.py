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
  def __init__(self, email, purchased_items, **properties):
    self.items = anvil.app.tables.users.get(purchased_items)
       
    # Set Form properties and Data Bindings.   
    self.init_components(**properties)
    self.items = purchased_items
    self.load_products(email, purchased_items)
  
    
  
  def load_products(self, email, purchased_items):
   anvil.server.call('get_purchased_items', email, purchased_items)
   print(purchased_items)
   if purchased_items == None:
    self.purchase_panel.visible = False
    self.purchase_panel.visible = True
 
    self.repeating_panel_1.items = purchased_items
    
   
        
   
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  
   

   
  