def check_if_not_empty(list):
    if list:
        return True
    else:
        input(f"\nList is already empty, press any key to continue...")
        return False