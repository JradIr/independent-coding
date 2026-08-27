def show_intro(player_health, enemy_health, book_pages):
    print("Welcome to the Magic Book Duel!")
    print("You are a wizard with", player_health, "health points.")
    print("The enemy has", enemy_health, "health points.")
    print("You have", book_pages, "pages of magic in your book.")
    print("The enemy has", book_pages, "pages of magic in their book.")
    print("You will take turns casting spells.")
    print("The first one to reach 0 health loses!")


def player_turn(player_health, enemy_health, book_pages):
    print("\nYour turn:")
    print("1. Cast a spell (1 page)")
    print("2. Heal yourself (1 page)")
    print("3. Do nothing")
    player_choice = input("Enter your choice (1-3): ")

    if player_choice == "1":
        enemy_health -= 10
        print("You cast a spell on the enemy! Enemy health:", enemy_health)
    elif player_choice == "2":
        player_health += 5
        print("You heal yourself! Your health:", player_health)
    elif player_choice == "3":
        print("You do nothing.")

    book_pages -= 1
    print("You have", book_pages, "pages of magic left.")
    return player_health, enemy_health, book_pages


def enemy_turn(player_health, enemy_health, book_pages):
    print("\nEnemy's turn:")
    print("1. Cast a spell (1 page)")
    print("2. Heal themselves (1 page)")
    print("3. Do nothing")
    enemy_choice = input("Enter your choice (1-3): ")

    if enemy_choice == "1":
        player_health -= 10
        print("The enemy casts a spell on you! Your health:", player_health)
    elif enemy_choice == "2":
        enemy_health += 5
        print("The enemy heals themselves! Enemy health:", enemy_health)
    elif enemy_choice == "3":
        print("The enemy does nothing.")

    book_pages -= 1
    print("The enemy has", book_pages, "pages of magic left.")
    return player_health, enemy_health, book_pages


def show_result(player_health):
    if player_health > 0:
        print("You win!")
    else:
        print("You lose!")


def play_game():
    player_health = 50
    enemy_health = 40
    book_pages = 5

    show_intro(player_health, enemy_health, book_pages)

    while player_health > 0 and enemy_health > 0:
        player_health, enemy_health, book_pages = player_turn(
            player_health, enemy_health, book_pages
        )
        if enemy_health <= 0:
            break

        player_health, enemy_health, book_pages = enemy_turn(
            player_health, enemy_health, book_pages
        )

    show_result(player_health)


play_game()

#this is a comment
