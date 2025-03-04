def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # We can combine several literals in a single pattern using | ("or")
        case 401 | 403 | 405:
            return "Not allowed"
        case _:
            return "Something's wrong with the internet"

# Three of these values will print the same output
print(http_error(401))
print(http_error(403))
print(http_error(405))
