def check_if_not_empty(new_list):
    if new_list:
        return True
    else:
        input(f"\nList is already empty, press any key to continue...")
        return False