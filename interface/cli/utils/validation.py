def check_if_not_empty(new_list):
    if new_list:
        return True
    else:
        input(f"List is empty, press any key to continue...")
        return False