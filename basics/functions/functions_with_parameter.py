
def escape_by(plan):

    if ("jump" in plan):
        print ("We cannot escape that WAY!! The boulder is too biggg")
    elif ("run" in plan or "running" in plan):
        print ("We cannot escape that way!! the boulder is moving tooooo")
    elif ("deeper" in plan):
        print ("That might just work woopity poo... LEts go Deeper")
    else:
        print ("HELL NAH I AINT TRYING THAT YOU STOOOPID??!?!?!?!?")


def run():
    plan = input("What is your escape plan? ")
    escape_by(plan)