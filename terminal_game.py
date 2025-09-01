import random


dmg = random.randint(0,5)

lives_of_Lyra = 5
lyra_alive = True

print("")
print("The starship Aurora drifts silently through the violet haze of an unexplored galaxy. Captain Lyra wakes in her quarters to the soft hum of the ship’s engines." \
" Today, like every day, offers choices—each one shaping the crew’s path through the unknown.")
print("")
print("Morning")
print("The ship’s AI gently wakes her: “Captain, it’s 07:00 shiptime. Would you like a status report or a quiet breakfast first?”")


while True:
    morning_choice=input("status or breakfast?")
    if morning_choice == "status":
        print("")
        print("The ship's AI: We have found an unusual energy signal on a nearby moon, explration awaits.")
        break
    elif morning_choice == "breakfast":
        print("")
        print("Lyra shares stories with the pilot, Taro, bonding over stale coffee and starfruit jam. The pilot Taro tells her about a energy signal on a nearby moon, that should be investigated")
        break
    else:
        print("status or breakfast ?")

print("")

print("Midday")
print("The Aurora descends toward the moon. Its surface glows faintly, scarred with craters that pulse with strange blue light. Lyra and a landing team suit up and step onto the dust. The silence is overwhelming—until it isn’t.")
print("Shadows slither from the rocks. Forms emerge: tall, insectoid creatures with chitinous armor and eyes that shine like cold fire. They screech, and the ground trembles.")

while True:
    midday_choice = input("Draw weapons or try communication (draw or communicate)")
    if midday_choice == "draw":
        print("")
        print("The crew opens fire, plasma bolts sparking against alien carapaces. The fight is brutal, claws against steel, but the Aurora’s crew holds their ground.")
        dmg_on_lyra = dmg
        print(f"Lyra lost {dmg_on_lyra} of her {lives_of_Lyra} lives")
        print("")
        if dmg_on_lyra >= lives_of_Lyra:
            lyra_alive = False
            print("Lyra was hit pretty bad, Taro fight's his way out but has to leave back Lyra to escape.")
            print("")
            print("The END")
            break
        if dmg_on_lyra <= lives_of_Lyra:
            print("Lyra got hit, but not as bad as the alien's first thought. With an quick counter attack Lyra manages to take out the Alien Leader, forcing the remaining aliens to retrieve where they've come from")
            print("They left behind a few shards of glowing crystals - Powerful fuel.")
            break
    elif midday_choice == "communicate":
        print("")
        print("Lyra raises her hands, projecting calm through the translator. The creatures hesitate, their screeches softening into a low hum. Perhaps they can be reasoned with—if she’s careful.")
        print("The aliens grant them a fragment of crystal willingly, warning in fractured words of greater dangers hidden in the galaxy’s dark reaches.")
        break
    else:
        print("draw or communicate?")

if lyra_alive == True:
    print("")
    print("Night")
    print("")
    print("Back aboard the Aurora, Lyra looks at the crystal in her hands. Was it a victory? Or the first step into a war they don’t yet understand?")
    print("She closes her eyes, knowing tomorrow will bring new choices—new dangers—out here among the stars.")
