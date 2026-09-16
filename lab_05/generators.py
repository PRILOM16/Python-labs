def computer_type_generator(computers, target_class):
    for comp in computers:
        if isinstance(comp, target_class):
            yield comp