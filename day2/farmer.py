# Land and crop details
total_acres = 80
segments = 5
acres_per_segment = total_acres / segments

# Crop details: (yield_type, yields in tonnes per acre, price per tonne)
# Tomato has two yield rates for 30% and 70% land
tomato_30_yield = 10  # ton/acre
tomato_70_yield = 12  # tonne/acre
tomato_price = 7000   # Rs per tonne

potato_yield = 10     # t/acre
potato_price = 20000  # Rs per tonne

cabbage_yield = 14    # t/acre
cabbage_price = 24000 # Rs per tonne

sunflower_yield = 0.7 # t/acre
sunflower_price = 200000 # Rs per tonne

sugarcane_yield = 45  # t/acre
sugarcane_price = 4000   # Rs per tonne

# Tomato revenue
tomato_acres_30 = 0.3 * acres_per_segment
tomato_acres_70 = 0.7 * acres_per_segment
tomato_tonnes = (tomato_acres_30 * tomato_30_yield) + (tomato_acres_70 * tomato_70_yield)
tomato_revenue = tomato_tonnes * tomato_price

# Other crops revenue
potato_revenue = acres_per_segment * potato_yield * potato_price
cabbage_revenue = acres_per_segment * cabbage_yield * cabbage_price
sunflower_revenue = acres_per_segment * sunflower_yield * sunflower_price
sugarcane_revenue = acres_per_segment * sugarcane_yield * sugarcane_price

# Overall sales
overall_sales = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue + sugarcane_revenue

# Chemical-free sales at month 11 (tomato, potato, cabbage, sunflower)
chemical_free_sales = tomato_revenue + potato_revenue + cabbage_revenue + sunflower_revenue

# Output
print("Overall Sales (Rs):", overall_sales)
print("Chemical-Free Sales at Month 11 (Rs):", chemical_free_sales)
