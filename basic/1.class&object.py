class goa:
    name=""
    drink=""
    def party(self):
        print("lets party....")
    def beach(self):
        print("Enjoying the beach")

ramesh = goa()
suresh = goa()

ramesh.name="Ramesh"
suresh.name="suresh"

ramesh.drink="Yes"
suresh.drink="he dont drink"
print(ramesh.name)
print("drink: "+ramesh.drink)
print(suresh.name)
print("drink: "+suresh.drink)


