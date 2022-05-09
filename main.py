from uwutilities.uwutilities import Import

test = Import("uwutilities/test.txt")

test.get_all()

print(test.dictionary)

test.dictionary["bonjour"] = "dzqkoà"
test.dictionary["dzq"] = "salut"

test.save("bonjour")

test.dictionary["salut"] = "salut"

