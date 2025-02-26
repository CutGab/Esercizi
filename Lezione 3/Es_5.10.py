current_users: list = ["LUCA", "ALESSIO", "FRANCESCO", "PAOLO"]

current_users: list = ["luca", "alessio", "francesco", "paolo"]

new_users: list = ["luca", "alessio", "SigmaBoy", "IgorMiti"]

for i in new_users:
    if i in current_users:
        print(f"{i} will need a new username")

    else:
        print(f"{i} is available!")