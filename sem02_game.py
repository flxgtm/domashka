import random
from colorama import Fore, Style, init
init(autoreset=True)
class Backpack:
    def __init__(self):
        self.items = {
            "грин шот": 2,
            "адреналин раш": 1,
            "зелье силы": 1
        }

    def show_items(self):
        return ", ".join([f"{k} ({v})" for k, v in self.items.items() if v > 0]) or "пусто"

    def use_item(self, name):
        if name in self.items and self.items[name] > 0:
            self.items[name] -= 1
            return True
        return False
class Character:
    base_health = 100
    base_adrenaline = 50
    base_strength = 15

    def __init__(self, name):
        self.name = name
        self.max_health = self.base_health
        self.health = self.max_health
        self.max_adrenaline = self.base_adrenaline
        self.adrenaline = self.max_adrenaline
        self.strength = self.base_strength
        self.backpack = Backpack()

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)
        return self.health <= 0
class Puppet(Character):
    def __init__(self, name, role, health=1.0, adrenaline=1.0, strength=1.0):
        super().__init__(name)
        self.role = role
        self.health_coef = health
        self.adrenaline_coef = adrenaline
        self.strength_coef = strength

        self.max_health *= self.health_coef
        self.health = self.max_health
        self.max_adrenaline *= self.adrenaline_coef
        self.adrenaline = self.max_adrenaline
        self.strength *= self.strength_coef

    def greet(self):
        greetings = {
            "волшебник": "вжух!",
            "боец": "никак вы не научитесь!"
        }
        return greetings.get(self.role, f"{self.role} готов к бою!")

    def attack(self):
        base = random.randint(8, 18) + self.strength * 0.4
        adrenaline_cost = 5
        bonus_scale = 0.15

        if self.adrenaline >= adrenaline_cost:
            self.adrenaline -= adrenaline_cost
            bonus = self.adrenaline * bonus_scale
            base += bonus
            print(f"{Fore.YELLOW}({self.name} тратит {adrenaline_cost} адреналина и получает +{bonus:.1f} урона){Style.RESET_ALL}")

        if random.random() < 0.2:
            crit = base * 1.5
            print(f"{Fore.RED} критический удар! {self.name} наносит {crit:.1f} урона! {Style.RESET_ALL}")
            return crit

        return base

    def use_potion(self, potion_type):
        if potion_type not in self.backpack.items or self.backpack.items[potion_type] == 0:
            return f"{Fore.YELLOW}такого нет в рюкзаке!{Style.RESET_ALL}"

        self.backpack.use_item(potion_type)

        if potion_type == "грин шот":
            heal = 42
            self.health = min(self.max_health, self.health + heal)
            return f"{self.name} восстанавливает {heal} здоровья!"
        elif potion_type == "адреналин раш":
            adrenaline_restore = 30
            self.adrenaline = min(self.max_adrenaline, self.adrenaline + adrenaline_restore)
            return f"{self.name} восстанавливает {adrenaline_restore} адреналина!"
        elif potion_type == "зелье силы":
            self.strength += 5
            return f"{self.name} чувствует прилив сил!"
        else:
            return "неизвестное зелье!"
class Monster:
    def __init__(self, health, strength, name, ability_name, color=Fore.MAGENTA):
        self.max_health = health
        self.health = health
        self.strength = strength
        self.name = name
        self.ability_name = ability_name
        self.color = color

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)

    def attack(self):
        base = random.randint(4, 14) + self.strength * 0.3
        if random.random() < 0.3:
            return self.use_special_ability(base)
        return base

    def use_special_ability(self, base):
        print(f"{self.color}{self.name} использует {self.ability_name}!{Style.RESET_ALL}")
        return base + random.randint(5, 12)

    def greet(self):
        return f"{self.color}{self.name}{Style.RESET_ALL} угрожающе на вас"


class Drowner(Monster):
    def __init__(self):
        super().__init__(70, 12, "утопец", "водный удар", Fore.CYAN)


class Ghoul(Monster):
    def __init__(self):
        super().__init__(60, 15, "гуль", "ядовитые когти", Fore.GREEN)


class Wyvern(Monster):
    def __init__(self):
        super().__init__(90, 18, "виверна", "огонь", Fore.RED)


class Leshen(Monster):
    def __init__(self):
        super().__init__(120, 20, "леший", "призыв пней", Fore.LIGHTBLACK_EX)


def generate_random_monster():
    return random.choice([Drowner, Ghoul, Wyvern, Leshen])()
def game():
    print(Fore.GREEN + "добро пожаловать в игру!" + Style.RESET_ALL)
    
    classes = {
        "волшебник": {"health": 1.0, "adrenaline": 1.5, "strength": 1.0},
        "боец": {"health": 1.5, "adrenaline": 1.0, "strength": 1.3}
    }

    while True:
        new_c = input("хотите добавить новый класс героя? (да/нет): ").strip().lower()
        if new_c in ("да", "нет"):
            break

    while new_c == "да":
        new_class = input("введите название нового класса: ").strip().lower()

        def safe(prompt):
            while True:
                value = input(prompt).strip().replace(",", ".")
                try:
                    return float(value)
                except ValueError:
                    print("введите число")

        h = safe("введите коэффициент здоровья: ")
        a = safe("введите коэффициент адреналина: ")
        s = safe("введите коэффициент силы: ")
        classes[new_class] = {"health": h, "adrenaline": a, "strength": s}

        print(f"добавлен новый класс: {new_class} (здоровье={h}, адреналин={a}, сила={s})")
        new_c = input("добавить ещё один класс? (да/нет): ").strip().lower()

    print("\nвыберите класс:")
    for i, cls_name in enumerate(classes.keys(), 1):
        print(f"{i} - {cls_name}")
    
    try:
        choice = int(input("ваш выбор: "))
        role = list(classes.keys())[choice - 1]
    except (ValueError, IndexError):
        print("неверный выбор, выбран класс 'боец'")
        role = "боец"

    name = input("введите имя героя: ")
    coefs = classes[role]
    hero = Puppet(name, role, **coefs)
    monster = generate_random_monster()

    print(f"\n{Fore.CYAN}{hero.greet()}{Style.RESET_ALL}")
    print(f"на вас нападает {monster.name}")

    while True:
        print(f"\n{Fore.CYAN}{hero.name}: hp {hero.health:.1f}/{hero.max_health} | adr {hero.adrenaline:.1f}/{hero.max_adrenaline}{Style.RESET_ALL}")
        print(f"{monster.color}{monster.name}: hp {monster.health:.1f}/{monster.max_health}{Style.RESET_ALL}")
        print(f"рюкзак: {hero.backpack.show_items()}")
        print("\n1 - атаковать")
        print("2 - выпить грин шот")
        print("3 - выпить адреналин раш") 
        print("4 - выпить зелье силы")
        print("5 - отдохнуть")
        
        action = input("ваш выбор: ").strip()

        if action == "1":
            damage = hero.attack()
            monster.take_damage(damage)
            print(f"вы нанесли {damage:.1f} урона!")

            if monster.health <= 0:
                print(Fore.GREEN + "победа!" + Style.RESET_ALL)
                break

            damage = monster.attack()
            hero.take_damage(damage)
            print(f"{monster.name} наносит вам {damage:.1f} урона!")

            if hero.health <= 0:
                print(Fore.RED + "вы пали в бою..." + Style.RESET_ALL)
                break

        elif action == "2":
            print(hero.use_potion("грин шот"))

        elif action == "3":
            print(hero.use_potion("адреналин раш"))

        elif action == "4":
            print(hero.use_potion("зелье силы"))

        elif action == "5":
            heal = 10
            adren = 5
            hero.health = min(hero.max_health, hero.health + heal)
            hero.adrenaline = min(hero.max_adrenaline, hero.adrenaline + adren)
            print(f"{hero.name} отдыхает: +{heal} HP, +{adren} адреналина.")
            damage = monster.attack()
            hero.take_damage(damage)
            print(f"пока вы отдыхали, {monster.name} нанес {damage:.1f} урона!")

            if hero.health <= 0:
                print(Fore.RED + "вы пали в бою..." + Style.RESET_ALL)
                break

        else:
            print("неверное действие!")


if __name__ == "__main__":
    game()
