
def forest_path():
    """
    Winning Path A:
      1. Follow the marked trail
      2. Use the fallen log
      3. Climb the tree
      4. Signal for help
      5. Wave arms

    Winning Path B:
      1. Follow the marked trail
      2. Build a raft
      3. Paddle hard
      4. Jump before the waterfall
      5. Enter the cave
    """
    print("You step into the forest, the air is fresh and mysterious.")
    # Level 1: Forest Entrance
    choice1 = input("Do you follow the marked trail or venture into the thick bushes? (trail/bushes): ").strip().lower()
    if choice1 != "trail":
        print("You get hopelessly lost in the thick bushes. Wild animals surround you. Game over.")
        return

    # Level 2: River Crossing
    choice2 = input("You reach a river. Do you use the fallen log or build a raft? (log/raft): ").strip().lower()
    if choice2 == "log":
        # Path A
        # Level 3A: Ancient Oak
        choice3 = input("You find an ancient oak tree. Do you climb the tree or search the roots? (climb/roots): ").strip().lower()
        if choice3 != "climb":
            print("You search the roots and disturb a nest of venomous snakes. Game over.")
            return
        # Level 4A: Tree Canopy
        choice4 = input("High in the canopy, do you signal for help or explore the canopy? (signal/explore): ").strip().lower()
        if choice4 != "signal":
            print("You explore the canopy and slip, falling to the forest floor. Game over.")
            return
        # Level 5A: Rescue Helicopter
        choice5 = input("A rescue helicopter appears. Do you wave your arms or light a fire? (wave/fire): ").strip().lower()
        if choice5 == "wave":
            print("You wave your arms and the helicopter spots you! As you are airlifted, you spot a hidden valley below, sparkling with treasure. You are the ultimate treasure hunter!")
        else:
            print("You light a fire, but the smoke attracts a swarm of angry bees. Game over.")
        return
    elif choice2 == "raft":
        # Path B
        # Level 3B: Rapids
        choice3 = input("You build a raft and hit the rapids. Do you paddle hard or let the current take you? (paddle/current): ").strip().lower()
        if choice3 != "paddle":
            print("You let the current take you and crash into rocks. Game over.")
            return
        # Level 4B: Waterfall
        choice4 = input("A waterfall looms ahead. Do you jump before the waterfall or stay on the raft? (jump/stay): ").strip().lower()
        if choice4 != "jump":
            print("You stay on the raft and go over the waterfall. The raft shatters and you are swept away. Game over.")
            return
        # Level 5B: Hidden Cave
        choice5 = input("You land near a hidden cave. Do you enter the cave or rest outside? (enter/rest): ").strip().lower()
        if choice5 == "enter":
            print("You enter the cave and discover ancient treasures! You are the ultimate treasure hunter!")
        else:
            print("You rest outside and are discovered by a band of mischievous monkeys who steal your supplies. Game over.")
        return
    else:
        print("Confused, you wander in circles until night falls. Game over.")
        return
