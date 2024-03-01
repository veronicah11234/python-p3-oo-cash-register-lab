class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
      for _ in range(quantity):
          self.items.append((title, float(price)))  
          self.total += float(price)

          
    def apply_discount(self):
      if self.discount > 0:
          discount_amount = (self.discount / 100) * self.total
          self.total -= discount_amount
          formatted_total = "${:.2f}".format(self.total) if self.total % 1 != 0 else "${:,.0f}".format(self.total)
          print(f"After the discount, the total comes to {formatted_total}.")
      else:
        print("There is no discount to apply.")


    def void_last_transaction(self):
      if self.items:
          last_item_title, last_item_price = self.items.pop()
          self.total -= last_item_price
      else:
          print("Setting total to 0.0")
          self.total = 0.0


    def reset_register_totals(self):
        self.total = 0
        self.items = []
