from ._anvil_designer import CartTemplate
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
from ..Product import Product
from ..OurProducts import OurProducts



class Cart(CartTemplate):
  def __init__(self, items, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.order = []
    self.items = items
   
      

    if not self.items:
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
  
    self.repeating_panel_1.items = self.items
 
    self.total = sum(item['product']['price'] * item['quantity'] for item in self.items)
    # Any code you write here will run before the form opens.
    self.total_label.text = f"${self.total:.02f}"

  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    for i in self.items: 
     
      self.order.append({'order':i['product']['item_name'], 'quantity':i['quantity']})
    try:
       charge = stripe.checkout.charge(amount=self.total*100, currency="USD")
  
    except:
       return

       anvil.server.call('add_order', charge['charge_id'], self.order)
       anvil.server.call('add_to_purchases')
      
     

    get_open_form().cart_items = []
    get_open_form().cart_click()
    Notification("Your order has been received!").show()
    
   

 