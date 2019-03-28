from tactics import tactics


def get_1_impulse(stats1, stats2):
    """ Импульс = Своя т.атака - ( Вражеская т.защита ) * ( 1 - свой т.пробой )"""
    tactic_1 = stats1['tactic_1']
    tactic_2 = stats2['tactic_1']
    fp_attack = tactics[tactic_1]['Attack']
    sp_defence = tactics[tactic_2]['Defence']
    fp_bash = tactics[tactic_1]['Bash']
    impulse = fp_attack - sp_defence * (1 - fp_bash)
    return impulse > 0 if impulse else 0


def get_2_impulse(stats1, stats2):
    """ Импульс = Своя т.атака - ( Вражеская т.защита ) * ( 1 - свой т.пробой )"""
    tactic_1 = stats1['tactic_1']
    tactic_2 = stats2['tactic_1']
    sp_attack = tactics[tactic_2]['Attack']
    fp_defence = tactics[tactic_1]['Defence']
    sp_bash = tactics[tactic_2]['Bash']
    impulse = sp_attack - fp_defence * (1 - sp_bash)
    return impulse > 0 if impulse else 0
