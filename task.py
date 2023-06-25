from random import randint, choice
from enum import Enum


class SuperAbility(Enum):
    CRITICAL_DAMAGE = 1
    BOOST = 2
    HEAL = 3
    SAVE_DAMAGE_AND_REVERT = 4
    STUN = 5
    GUARD_FOR_ALL = 6
    REVIVE = 7
    INVISIBILITY = 8
    LUCK = 9
    POISON_HEAL_SHURIKENS = 10
    SELF_DESTRUCTION = 11
    ONE_FOR_ALL = 12
    SIZE_INCREASE_AND_REDUCTION = 13
    OPOSSUM = 14
    VAMPIRISM = 15
    ANGEL_CROW = 16


class GameEntity:
    def __int__(self, name, health, damage):
        self.__name = name
        self.__health = health
        self.__damage = damage

    @property
    def name(self):
        return self.__name

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if value < 0:
            self.__health = 0
        else:
            self.__health = value


    @property
    def damage(self):
        return self.__damage

    @damage.setter
    def damage(self, value):
        self.__damage = value


    def __str__(self):
        return f'{self.__name} health: {self.__health} damage: {self.__damage}'


class Boss(GameEntity):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage)
        self.__defence = None


    @property
    def defence(self):
        return self.__defence

    def choose_defence(self, heroes):
        hero = choice(heroes)
        if hero.health <= 0:
            self.choose_defence(heroes)
        else:
            self.__defence = hero.super_ability


    def hit(self, herous):
        for hero in herous:
            if hero.health > 0:
                hero.health = hero.health - self.damage



    def __str__(self):
        return f'BOOS ' + super().__str__() + f' defence: {self.__defence}'


class Hero(GameEntity):
    def __init__(self, name, health, damage, super_ability):
        super().__init__(name, health, damage)
        if not isinstance(super_ability, SuperAbility):
            raise ValueError("Ability must be of type  SuperAbility")
        else:
            self.__super_ability = super_ability

    def hit(self, boss):
        boss.health = boss.health - self.damage

    @property
    def super_ability(self):
        return self.__super_ability

    def apply_super_power(self, boss, heroes):
        pass



class Warrior(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.CRITICAL_DAMAGE)

    def apply_super_power(self, boss, heroes):
        coeffient = randint(2, 5)
        boss.health = boss.health - self.damage * coeffient
        print(f'Warrior hits critically: {self.damage * coeffient}')


class Magic(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.BOOST)

    def apply_super_power(self, boss, heroes):
        for hero in heroes:
            hero.damage += int(hero.damage * 0.25)
        print(f'Power fo each heroes was increased!')


class Berserk(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.SAVE_DAMAGE_AND_REVERT)

    def apply_super_power(self, boss, heroes):
        self.health = self.health - int(boss.damage * 0.95)
        self.__saved_damage = int(boss.damage * 0.05)
        self.damage = self.damage + self.__saved_damage
        print(f"Berserk's power was increased")


class Thor(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.STUN)

    def apply_super_power(self, boss, heroes):
        stun_chance = randint(1, 11)
        if stun_chance == 3:
            print('Boss has been stunned')
            for hero in heroes:
                hero.health = hero.health + boss.damage


class Golem(Hero):
    def __init__(self, name, health, damage):
        super().__init__(name, health, damage, SuperAbility.GUARD_FOR_ALL)

    def apply_super_power(self, boss, heroes):
        self.health = self.health - (boss.damage + int(boss.damage * 0.8))
        for hero in heroes:
            if hero.health > 0 and hero != self:
                hero.health = hero.health + int(boss.damage * 0.2)
        print(f'GUARDED!')

"""#### продолжить """


