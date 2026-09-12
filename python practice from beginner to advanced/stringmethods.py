# 1 method:title() 
my_str = 'hello world'

title_case_my_str = my_str.title()
print(title_case_my_str)

# 2 method:lower()

my_str = 'hello world'

is_all_lower = my_str.islower()
print(is_all_lower)

# 3 method:capitalize()
my_str = 'hello world'

capitalized_my_str = my_str.capitalize()
print(capitalized_my_str) 

# 4 method:count()
my_str = 'hello world'

o_count = my_str.count('o')
print(o_count)

# 5 method:find()
my_str = 'hello world'

world_index = my_str.find('world')
print(world_index) 

# 6 method:endwith()
my_str = 'hello world'

ends_with_world = my_str.endswith('world')
print(ends_with_world)

# 7 method:startswith()
my_str = 'hello world'

starts_with_hello = my_str.startswith('hello')
print(starts_with_hello)

#8 method:join()
my_list = ['hello', 'world']

joined_my_str = ' '.join(my_list)
print(joined_my_str)

# 9 method:split()
my_str = 'hello world'

split_words = my_str.split()
print(split_words)

# 10 method:replace()
my_str = 'hello world'

replaced_my_str = my_str.replace('hello', 'hi')
print(replaced_my_str)

# 11 method:upper()
my_str = '  hello world  '

trimmed_my_str = my_str.strip()
print(trimmed_my_str) 