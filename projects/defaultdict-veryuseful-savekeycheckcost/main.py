from collections import defaultdict

# Group trade fills by ticker
fills_by_symbol = defaultdict(list)
fills_by_symbol["MSFT"].append(400.5)
print(fills_by_symbol)

# Running balance tracker
net_positions = defaultdict(int)
net_positions["NVDA"] += 100
net_positions["NVDA"] -= 40  # net_positions['NVDA'] == 60
print(net_positions)