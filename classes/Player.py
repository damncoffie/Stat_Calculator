class Player:
    def __init__(
            self,
            hit_points: int = 0,
            spades: int = 0,
            defence: int = 0,
            range_damage: int = 0,
            range_attacks: int = 0,
            range_mod: int = 0,
            close_damage: int = 0,
            close_attacks: int = 0,
            close_mod: int = 0,
            melee_damage: int = 0,
            melee_attacks: int = 0,
            melee_mod: int = 0,
            weapon_1: str = 'Range',
            weapon_2: str = 'Range',
            weapon_3: str = 'Range',
            tactic_1: str = 'Careful',
            tactic_2: str = 'Careful',
            tactic_3: str = 'Careful'
    ):
        self.hit_points = float(hit_points)
        self.spades = int(spades)
        self.defence = int(defence)
        self.range_damage = int(range_damage)
        self.range_attacks = int(range_attacks)
        self.range_mod = int(range_mod)
        self.close_damage = int(close_damage)
        self.close_attacks = int(close_attacks)
        self.close_mod = int(close_mod)
        self.melee_damage = int(melee_damage)
        self.melee_attacks = int(melee_attacks)
        self.melee_mod = int(melee_mod)
        self.weapon_1 = weapon_1
        self.weapon_2 = weapon_2
        self.weapon_3 = weapon_3
        self.tactic_1 = tactic_1
        self.tactic_2 = tactic_2
        self.tactic_3 = tactic_3

