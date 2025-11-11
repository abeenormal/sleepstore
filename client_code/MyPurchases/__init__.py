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
  def __init__(self,user_email,order, **properties):

       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)
   self.order = order
   self.order = [] 

 
   if not self.order:
      self.empty_purchase_panel.visible = True
      self.purchase_panel.visible = False
      anvil.server.call.get_user_purchases(user_email, order)
    


      
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  
   

   
  