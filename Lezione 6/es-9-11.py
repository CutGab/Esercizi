from Users import*

u1 = Users ("Mario", "Rossi", "SuperMario", "Mario.Rossi@gmail.com")

pu = Privileges (["View Audit Log", "See History", "Manage Channels"])

a1 = Admin (u1, pu)

a1.describe_user()
a1.show_privileges()