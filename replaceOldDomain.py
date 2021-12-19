def replace_domain(email, old_domain, new_domain):
    if "@" + old_domain in email:
        index = email.index("@" + old_domain)
        new_email = email[:index] + "@" + new_domain
        return new_email
    return email

    
if __name__ == "__main__":
    print(replace_domain("habib@hotmail.com", "hotmail.com", "hotmail.fr"))