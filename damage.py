from classes.Player import Player
from tactics import tactics


def get_damage(player1: Player, player2: Player, weapon: str):
    """ Урон = Импульс * ( Вид Оружия.Урон * ( Вид Оружия.Модификатор / 100 ) + Пики - Защита врага )
     * Вид Оружия.Атаки"""
    p2_defence = player2.defence
    p1_spades = player1.spades
    p1_damage = 0
    p1_attacks = 0
    p1_mod = 0
    if weapon == 'Range':
        p1_damage = player1.range_damage
        p1_attacks = player1.range_attacks
        p1_mod = player1.range_mod
    if weapon == 'Close':
        p1_damage = player1.close_damage
        p1_attacks = player1.close_attacks
        p1_mod = player1.close_mod
    if weapon == 'Melee':
        p1_damage = player1.melee_damage
        p1_attacks = player1.melee_attacks
        p1_mod = player1.melee_mod
    return get_impulse(player1, player2) * (p1_damage * (p1_mod / 100) + p1_spades - p2_defence) * p1_attacks


def get_impulse(player1: Player, player2: Player):
    """ Импульс = Своя т.атака - ( Вражеская т.защита ) * ( 1 - свой т.пробой )"""
    # TODO To consider round's tactic, remove 1 round tactic hardcode
    p1_tactic = player1.tactic_1
    p2_tactic = player2.tactic_1
    p1_attack = tactics[p1_tactic]['Attack']
    p2_defence = tactics[p2_tactic]['Defence']
    p1_bash = tactics[p1_tactic]['Bash']
    impulse = p1_attack - p2_defence * (1 - p1_bash)
    if impulse > 0:
        return impulse
    else:
        return 0
