from ast import keyword


defaul_order = "{},{} and {}".format('john','bill','sean')
print("\n-- Default Order ---")
print(defaul_order)

positional_order = "{1},{0} and {2}".format('john','bill','sean')
print('\n-- Positional Order ---')
print(positional_order)

keyword_order = "{s}, {b} and {j}".format(j='john',b='bill',s='sean')
print('\n--- Keyword Order ---')
print(keyword_order)