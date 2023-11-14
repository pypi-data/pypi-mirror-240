from pathlib import Path
import json


CUR_DIR = Path(__file__).resolve().parent
PATH_LIST = CUR_DIR / "list.json"
PATH_LIST_TXT = CUR_DIR / "list.txt"


def save_data(data, filename):
    with open(filename, "w") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def read_data(filename):
    with open(filename, "r+") as f:
        return json.load(f)


if PATH_LIST:
    with open(PATH_LIST, "r", encoding="utf-8") as file:
        LIST = json.load(file)
else:
    LIST = []

actions = [
    "Ajouter un élément à la liste",
    "Retirer un élément de la liste",
    "Afficher la liste",
    "Vider la liste",
    "Terminer le programme",
]


while True:
    try:
        print("\nVoici les actions possibles:")

        for i, action in enumerate(actions, start=1):
            print(f"{i}. {action}")
        user_choice = input("\nQue voulez-vous faire ? ")

        if int(user_choice) not in range(1, len(actions) + 1):
            raise ValueError
    except ValueError:
        print("Veuillez choisir une option valide\n")

    if user_choice == "1":
        element = input("Entrez un élément à ajouter à la liste: ")
        print(LIST)
        LIST.append(element)
        print(f"L'élément {element} a été ajouté à la liste")
        print(LIST)

    elif user_choice == "2":
        element = input("Entrez un élément à retirer de la liste: ")
        try:
            LIST.remove(element)
        except ValueError:
            print("Cet élément n'est pas dans la liste")
            continue
        print(f"L'élément {element} a été supprimé de la liste")
        print(LIST)

    elif user_choice == "3":
        if LIST:
            for i, element in enumerate(LIST, start=1):
                print(f"{i}: {element}")
        else:
            print("La liste est vide")

    elif user_choice == "4":
        LIST.clear()
        print(LIST)

    elif user_choice == "5":
        # write on txt file
        # transform list to string
        list_str = " ".join(LIST)
        PATH_LIST_TXT.write_text(list_str)

        # write in json file
        save_data(LIST, PATH_LIST)

        print("A bientôt !")
        print("-" * 50)
        break
