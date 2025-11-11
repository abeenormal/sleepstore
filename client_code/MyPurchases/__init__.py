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






class MyPurchases(MyPurchasesTemplate):
  def __init__(self, user_email, **properties):

       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)

  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  def add_purchases(self, user_email,order):
  
   anvil.users.get_user(email=user_email)
   if user_email:
     self.items = order
     order = anvil.server.call('get_user_purchases', user_email)
      
   if 'user_email'== None:
     self.empty_purchase_panel.visible = True
     self.purchase_panel.visible = False
     
   if 'user_email' != None:
     return
     self.purchase_panel.self.repating_panel_1.items=anvil.server.call('get_user_purchases')  
    
   