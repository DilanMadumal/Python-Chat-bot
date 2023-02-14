import random

R_EATING = "I can't sing song because i'm bot!"
R_ADVICE = "You cam use internet and search that"
R_READ = "You Can buy book and read it"


def unknown():
    response = ["Could you please re-phrase that? ",
                "ops..!",
                "i can't understand.",
                ][
        random.randrange(4)]
    return response