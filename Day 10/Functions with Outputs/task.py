def format_name(f_name, l_name):
    titled_f_name = f_name.title()
    titled_l_name = l_name.title()
    whole_name = f"{titled_f_name} {titled_l_name}"
    return whole_name

formatted = format_name("SELIN", "sevim")
print(formatted)
