def get_1_damage(stats1: dict, stats2: dict):
    """ Урон = Импульс * ( Вид Оружия.Урон * ( Вид Оружия.Модификатор / 100 ) + Пики - Защита врага )
     * Вид Оружия.Атаки"""
    sp_defence = stats2['defence']
    spade = stats1['spades']
    damage = 0
    attacks = 0
    mod = 0
    if stats1['weapon_1'] == 'Range':
        damage = stats1['range_damage']
        attacks = stats1['range_attacks']
        mod = stats1['range_mod']
    if stats1['weapon_1'] == 'Close':
        damage = stats1['close_damage']
        attacks = stats1['close_attacks']
        mod = stats1['close_mod']
    if stats1['weapon_1'] == 'Melee':
        damage = stats1['melee_damage']
        attacks = stats1['melee_attacks']
        mod = stats1['melee_mod']
    return (damage * (mod / 100) + spade - sp_defence) * attacks


def get_2_damage(stats1: dict, stats2: dict):
    """ Урон = Импульс * ( Вид Оружия.Урон * ( Вид Оружия.Модификатор / 100 ) + Пики - Защита врага )
     * Вид Оружия.Атаки"""
    fp_defence = stats1['defence']
    spade = stats2['spades']
    damage = 0
    attacks = 0
    mod = 0
    if stats2['weapon_1'] == 'Range':
        damage = stats2['range_damage']
        attacks = stats2['range_attacks']
        mod = stats2['range_mod']
    if stats2['weapon_1'] == 'Close':
        damage = stats2['close_damage']
        attacks = stats2['close_attacks']
        mod = stats2['close_mod']
    if stats2['weapon_1'] == 'Melee':
        damage = stats2['melee_damage']
        attacks = stats2['melee_attacks']
        mod = stats2['melee_mod']
    return (damage * (mod / 100) + spade - fp_defence) * attacks
