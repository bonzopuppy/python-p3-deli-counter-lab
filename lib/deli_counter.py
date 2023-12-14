katz_deli = []


def line(katz_deli):
    if not katz_deli:
        print("The line is currently empty.")
    else:
        line_status = "The line is currently: "
        line_items = [f"{i}. {person}" for i,
                      person in enumerate(katz_deli, start=1)]
        line_status += " ".join(line_items)
        print(line_status)


def take_a_number(katz_deli, name):
    katz_deli.append(name)
    position = len(katz_deli)
    print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(katz_deli):
    if not katz_deli:
        print("There is nobody waiting to be served!")
    else:
        next_up = katz_deli[0]
        print(f"Currently serving {next_up}.")
        katz_deli.pop(0)
