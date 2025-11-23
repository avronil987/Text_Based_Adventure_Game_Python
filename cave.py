
def cave_path():
    """
        Winning Path A:
            1. Enter quietly
            2. Left tunnel
            3. Build a raft
            4. Examine crystals
            5. Sneak past dragon
            6. Use crystal to open exit

        Winning Path B:
            1. Enter quietly
            2. Right tunnel
            3. Swim across
            4. Force open ancient door
            5. Take golden idol
            6. Place idol on pedestal
    """
    print("You step into the cave, darkness surrounds you.")
    # Level 1: Cave Entrance
    choice1 = input("Do you enter quietly or shout to check for echoes? (quietly/shout): ").strip().lower()
    if choice1 != "quietly":
        print("Your shout echoes through the cave. Wild animals sense your presence and attack! You are eaten alive. Game over.")
        return

    # Level 2: Forked Tunnel
    choice2 = input("You reach a fork. Do you take the left tunnel (smells damp) or right tunnel (feels breezy)? (left/right): ").strip().lower()
    if choice2 == "left":
        # Left Tunnel Path (A)
        # Level 3A: Subterranean River
        choice3 = input("A river blocks your path. Do you build a raft or try to jump across? (raft/jump): ").strip().lower()
        if choice3 != "raft":
            print("You leap for the other side, but fall into the river and are swept away by the current. Game over.")
            return
        # Level 4A: Crystal Chamber
        choice4 = input("You enter a chamber filled with glowing crystals. Do you examine the crystals or ignore and move on? (examine/ignore): ").strip().lower()
        if choice4 != "examine":
            print("You ignore the crystals and step on a hidden trap. The floor collapses beneath you! Game over.")
            return
        # Level 5A: Sleeping Dragon
        choice5 = input("A sleeping dragon blocks the exit. Do you sneak past or attack the dragon? (sneak/attack): ").strip().lower()
        if choice5 != "sneak":
            print("You charge at the sleeping dragon. It wakes up furious and incinerates you with its fiery breath! Game over.")
            return
        # Level 6A: Secret Exit
        choice6 = input("You find a secret exit sealed by magic. Do you use a crystal to open it or search for another way? (crystal/search): ").strip().lower()
        if choice6 == "crystal":
            print("You use the magical crystal to open the secret exit. Behind it lies a chamber filled with glittering treasure! You are the ultimate treasure hunter!")
        else:
            print("You search for another exit, but get hopelessly lost in the maze of tunnels. Game over.")
        return
    elif choice2 == "right":
        # Right Tunnel Path (B)
        # Level 3B: Underground Lake
        choice3 = input("You reach an underground lake. Do you swim across or use the old boat? (swim/boat): ").strip().lower()
        if choice3 != "swim":
            print("You step into the old boat, but it sinks instantly. You drown in the cold, dark lake. Game over.")
            return
        # Level 4B: Ancient Door
        choice4 = input("A massive ancient door blocks your way. Do you try to force it open or search for a hidden lever? (force/lever): ").strip().lower()
        if choice4 != "force":
            print("You search for a hidden lever, but trigger a trap. Poison darts shoot from the walls! Game over.")
            return
        # Level 5B: Treasure Chamber
        choice5 = input("You enter a treasure chamber. Do you take the golden idol or the silver key? (idol/key): ").strip().lower()
        if choice5 != "idol":
            print("You take the silver key, but the idol was the real treasure. The chamber collapses! Game over.")
            return
        # Level 6B: Idol Pedestal
        choice6 = input("You find a pedestal with a slot for the idol. Do you place the idol on the pedestal or try to break the pedestal? (place/break): ").strip().lower()
        if choice6 == "place":
            print("You place the golden idol on the pedestal. The ground shakes and a wall slides open, revealing a room overflowing with treasure! You are the ultimate treasure hunter!")
        else:
            print("You try to break the pedestal, but set off an alarm. The cave seals shut, trapping you forever. Game over.")
        return
    else:
        print("Confused, you wander into darkness and are never seen again. Game over.")
        return
