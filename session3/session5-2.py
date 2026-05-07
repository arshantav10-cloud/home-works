from cobra_color import cstr, safe_print

c_text_1 = cstr("Hello World!", fg="g", styles=["bold"])
# Print directly from the terminal
print(c_text_1)

c_text_2 = cstr("Hello World!", fg=(255, 255, 0), styles=["udl", "bold"])

print(c_text_2)