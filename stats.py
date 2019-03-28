def get_first_player_stats(request) -> dict:
    first_player_stats = {
        'hit_points': request.form["fpHitPoints"],
        'spades': request.form["fpSpades"],
        'defence': request.form["fpDefence"],
        'range_damage': request.form["fpRangeDamage"],
        'range_attacks': request.form["fpRangeAttacks"],
        'range_mod': request.form["fpRangeMod"],
        'close_damage': request.form["fpCloseDamage"],
        'close_attacks': request.form["fpCloseAttacks"],
        'close_mod': request.form["fpCloseMod"],
        'melee_damage': request.form["fpMeleeDamage"],
        'melee_attacks': request.form["fpMeleeAttacks"],
        'melee_mod': request.form["fpMeleeMod"],
        'weapon_1': request.form["fpWeapon1"],
        'weapon_2': request.form["fpWeapon2"],
        'weapon_3': request.form["fpWeapon3"],
        'tactic_1': request.form["fpTactic1"],
        'tactic_2': request.form["fpTactic2"],
        'tactic_3': request.form["fpTactic3"],
    }
    return first_player_stats


def get_second_player_stats(request) -> dict:
    second_player_stats = {
        'hit_points': request.form["spHitPoints"],
        'spades': request.form["spSpades"],
        'defence': request.form["spDefence"],
        'range_damage': request.form["spRangeDamage"],
        'range_attacks': request.form["spRangeAttacks"],
        'range_mod': request.form["spRangeMod"],
        'close_damage': request.form["spCloseDamage"],
        'close_attacks': request.form["spCloseAttacks"],
        'close_mod': request.form["spCloseMod"],
        'melee_damage': request.form["spMeleeDamage"],
        'melee_attacks': request.form["spMeleeAttacks"],
        'melee_mod': request.form["spMeleeMod"],
        'weapon_1': request.form["spWeapon1"],
        'weapon_2': request.form["spWeapon2"],
        'weapon_3': request.form["spWeapon3"],
        'tactic_1': request.form["spTactic1"],
        'tactic_2': request.form["spTactic2"],
        'tactic_3': request.form["spTactic3"],
    }
    return second_player_stats

