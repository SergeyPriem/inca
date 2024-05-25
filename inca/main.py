import writer as wf

# This is a placeholder to get you started or refresh your memory.
# Delete it or adapt it as necessary.
# Documentation is available at https://developer.writer.com/framework

# Shows in the log when the app starts
print("Hello world!")


# Its name starts with _, so this function won't be exposed
def _update_message(state):
    is_even = state["counter"] % 2 == 0
    message = ("+Even" if is_even else "-Odd")
    state["message"] = message


def decrement(state):
    state["counter"] -= 1
    _update_message(state)


def increment(state):
    state["counter"] += 1
    # Shows in the log when the event handler is run
    print("The counter has been incremented.")
    _update_message(state)


def to_usd(state):
    state["currency"] = "USD"
    print("Currency changed to USD")


def to_eur(state):
    state["currency"] = "EUR"
    print("Currency changed to EUR")


def to_uah(state):
    state["currency"] = "UAH"
    print("Currency changed to UAH")


def to_sum(state):
    state["currency"] = "SUM"
    print("Currency changed to SUM")


# Initialise the state

# "_my_private_element" won't be serialised or sent to the frontend,
# because it starts with an underscore

initial_state = wf.init_state({
    "my_app": {
        "title": "M-Balance"
    },
    "_my_private_element": 1337,
    "message": None,
    "counter": 26,
    "currency": "USD"
})

_update_message(initial_state)
