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
  def __init__(self, **properties):
  
       
    # Set Form properties and Data Bindings.
   self.init_components(**properties)


    
  def purchased_items(self):
    app.tables.orders.search(order='purchased_items', user_email='user_email')
    return
    self.repeating_panel_1.self_label_1 = "user_email" 
    self.repeating_panel_1.self_label_2 = 'purchased_items'
  

    


      
  def shop_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  
   

   
  