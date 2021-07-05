email = input("Enter Your Email: ").strip()
user_name = email[:email.index("@")]
domain_name = email[email.index("@")+1:]
format_ = (f"Your username : '{user_name}' and your domain : '{domain_name}'")
print(format_)