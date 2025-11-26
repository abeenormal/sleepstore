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
    self.items = items
    self.order = []  
   
    if not self.items:
      self.empty_cart_panel.visible = True
      self.column_panel_1.visible = False
  
    self.repeating_panel_1.items = self.items
 
    self.total = sum(item['product']['price'] * item['quantity'] for item in self.items)
    # Any code you write here will run before the form opens.
    self.total_label.text = f"${self.total:.02f}"
    
    def add_purchase(): 
      rows_to_add = []
      for products in self.items:
        rows_to_add.append({
        'purchase_name': products['item_name'],
        'quantity': self.item['quantity'],
        'user_email': self.user['email'],
        'total': products['item_price']
    })

      app_tables.purchases.add_rows(rows_to_add)



  def shop_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    get_open_form().Shop_link()

  def checkout_button_click(self, **event_args):
    """This method is called when the button is clicked""" 
    
    
    for i in self.items:      
      self.order.append({'item_name':i['product']['item_name'], 'quantity':i['quantity']})
    
    try:     
      charge = stripe.checkout.charge(amount=self.total*100, currency="USD")
      self.add_purchase
    
      

    except:

     return
      
    anvil.server.call('add_order', charge['charge_id'], self.order)
    
  
    
    get_open_form().cart_items = []
    get_open_form().cart_click()
    Notification("Your order has been received!").show()
    
   

 