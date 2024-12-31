import matplotlib.pyplot as plt

class SmartphoneTradingAgent:
    def __init__(self, initial_stock, average_price):
        self.stock = initial_stock  # Initial amount of stock
        self.price = average_price  # The average price of the smartphone
        self.history_stock = []  # To store stock history for plotting
        self.history_price = []  # To store price history for plotting

    def update_price(self, current_price):

        self.price = current_price  #Update the price.

    def decide_order(self):
        price_threshold = 480           #Avg 600 & 80% of 600 BDT is 480
        critical_stock_level = 10       #stock<10 then order at least 10 units

        print(f"Price: {self.price} BDT, Price Threshold: {price_threshold} BDT, Stock: {self.stock}")

        if self.price <= price_threshold and self.stock >= critical_stock_level:
            to_buy = 15
            print(f"Conditions met: Price below threshold and stock above critical level. Ordering {to_buy} units.")
        elif self.stock < critical_stock_level:
            to_buy = 10
            print(f"Stock below critical level. Ordering {to_buy} units.")
        else:
            to_buy = 0
            print("Conditions not met. No order placed.")

        return to_buy

    def place_order(self, to_buy):
        if to_buy > 0:
            self.stock += to_buy
            print(f"Ordered {to_buy} units. New stock: {self.stock}")
        else:
            print("No order placed.")

    def simulate_day(self, current_price):
        self.update_price(current_price)
        to_buy = self.decide_order()
        self.place_order(to_buy)
        self.history_stock.append(self.stock)  #  stock for plotting
        self.history_price.append(self.price)  #  price for plotting

    def plot_stock_and_price_history(self):
        fig, ax1 = plt.subplots()

        ax1.set_xlabel('Day')  # Set x-axis label
        ax1.set_ylabel('Stock Level', color='tab:blue')    # Plotting stock level
        ax1.plot(self.history_stock, color='tab:blue', label='Stock Level')
        ax1.tick_params(axis='y', labelcolor='tab:blue')

        ax2 = ax1.twinx()
        ax2.set_ylabel('Price (BDT)', color='tab:green')    # y-axis to plot the price
        ax2.plot(self.history_price, color='tab:green', label='Price', linestyle='--')
        ax2.tick_params(axis='y', labelcolor='tab:green')

        plt.title('Stock Level and Price Over Time')     # Title and labels
        fig.tight_layout()
        plt.show()
def run_simulation(initial_stock, average_price, price_changes):
    agent = SmartphoneTradingAgent(initial_stock, average_price)

    for day, price in enumerate(price_changes, start=1):
        print(f"\nDay {day}: Price = {price} BDT")
        agent.simulate_day(price)

    agent.plot_stock_and_price_history()     # Plot the stock and price history over time
# Example
initial_stock = 20  # Initial stock level
average_price = 600  # Average price of the smartphone
price_changes = [
    600,  # Day 1: No discount
    500,  # Day 2: Price drops 20%
    550,  # Day 3: Price increases slightly
    450,  # Day 4: Significant price drop (to 20% discount)
    600,  # Day 5: Price returns to original
]

run_simulation(initial_stock, average_price, price_changes)
