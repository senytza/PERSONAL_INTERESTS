#Created for an undisclosed person.
#I shouldn't even be showing this but no NDA was signed so here it is LOL
#plus i want that additional contribution points ykyk B)
#okay how about this:
#LET ME TRY BRO.
#WILL THE CALL HAPPEN?
#This script is subject to change and is NOT final. I will add things as time goes on just because I can hehaeaeae

#CONDITIONS TBA
#VARIABLES
print("-------------------------------------")
print("----------INPUT INFORMATION----------")
person = input("Who are you? -> ").lower()
partner = input("Who's your partner? -> ").lower()
canPersonCall = input(f"Can {person} call with {partner} right now?(True/False) -> ").lower() == "true"
canPartnerCall = input(f"Can {partner} call with {person} right now? (True/False) -> ").lower() == "true"
canPersonAFK = input(f"Can {person} go AFK without {partner} minding it? (True/False) -> ").lower() == "true"
canPartnerAFK = input(f"Can {partner} go AFK without {person} minding it? (True/False) -> ").lower() == "true"
hasPersonEaten = input(f"Has {person} eaten anything within the past 5 hours? (True/False) -> ").lower() =="true"
hasPartnerEaten = input(f"Has {partner} eaten anything within the past 5 hours? (True/False) -> ").lower() =="true"
sleepTimePerson = eval(input(f"How long did {person} sleep today? -> "))
sleepTimePartner = eval(input(f"How long did {partner} sleep today? -> "))


#PRINTED INFORMATION
print("----------------------------------------")
print("----------INPUTTED INFORMATION----------")
print("Name of User:",person)
print("Name of Partner:",partner)
print(person,"call status:",canPersonCall)
print(partner,"call status:",canPartnerCall)
print(person,"can AFK status:",canPersonAFK)
print(partner,"can AFK status:",canPartnerAFK)
print(person,"has eaten within 5 hours:",hasPersonEaten)
print(partner,"has eaten within 5 hours:",hasPartnerEaten)
print(person,"sleep duration:",sleepTimePerson)
print(partner,"sleep duration:",sleepTimePartner)
