
def ask(message=None, default=None, required=True):
    if message:
        if default:
            var = input("{}: (default:{}) ".format(message, default))
            if not var:
                var = default
        else:
            var = input("{}: ".format(message))
            if required:
                if not var:
                    print("This value is required, please try again.")
                    ask(message, required)
    return var
