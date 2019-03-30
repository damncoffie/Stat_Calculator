from flask import Flask, render_template, request

import damage
from classes.Player import Player

app = Flask(__name__)


# change
# @app.route('/')
# def hello() -> '302':
#     return redirect('/entry')


@app.route('/')
def welcome_page() -> 'html':
    return render_template('calc.html')


@app.route('/calculate', methods=['POST'])
def calculate() -> str:
    first_player = Player(request.form["fpHitPoints"],
                          request.form["fpSpades"],
                          request.form["fpDefence"],
                          request.form["fpRangeDamage"],
                          request.form["fpRangeAttacks"],
                          request.form["fpRangeMod"],
                          request.form["fpCloseDamage"],
                          request.form["fpCloseAttacks"],
                          request.form["fpCloseMod"],
                          request.form["fpMeleeDamage"],
                          request.form["fpMeleeAttacks"],
                          request.form["fpMeleeMod"],
                          request.form["fpWeapon1"],
                          request.form["fpWeapon2"],
                          request.form["fpWeapon3"],
                          request.form["fpTactic1"],
                          request.form["fpTactic2"],
                          request.form["fpTactic3"],
                          )

    second_player = Player(request.form["spHitPoints"],
                           request.form["spSpades"],
                           request.form["spDefence"],
                           request.form["spRangeDamage"],
                           request.form["spRangeAttacks"],
                           request.form["spRangeMod"],
                           request.form["spCloseDamage"],
                           request.form["spCloseAttacks"],
                           request.form["spCloseMod"],
                           request.form["spMeleeDamage"],
                           request.form["spMeleeAttacks"],
                           request.form["spMeleeMod"],
                           request.form["spWeapon1"],
                           request.form["spWeapon2"],
                           request.form["spWeapon3"],
                           request.form["spTactic1"],
                           request.form["spTactic2"],
                           request.form["spTactic3"],
                           )

    first_round_result = get_round_result(first_player,
                                          second_player,
                                          first_player.weapon_1,
                                          second_player.weapon_1,
                                          first_player.tactic_1,
                                          second_player.tactic_1,
                                          'Раунд 1')

    second_round_result = get_round_result(first_player,
                                           second_player,
                                           first_player.weapon_2,
                                           second_player.weapon_2,
                                           first_player.tactic_2,
                                           second_player.tactic_2,
                                           'Раунд 2')
    third_round_result = get_round_result(first_player,
                                          second_player,
                                          first_player.weapon_3,
                                          second_player.weapon_3,
                                          first_player.tactic_3,
                                          second_player.tactic_3,
                                          'Раунд 3')

    return first_round_result + '<br>' + second_round_result + '<br>' + third_round_result + '<br>'


def get_round_result(first_player, second_player, p1_weapon, p2_weapon, p1_tactic, p2_tactic, round):
    p1_damage = damage.get_damage(first_player, second_player, p1_weapon, p1_tactic, p2_tactic)
    p2_damage = damage.get_damage(second_player, first_player, p2_weapon, p1_tactic, p2_tactic)

    first_player.hit_points = first_player.hit_points - p2_damage
    second_player.hit_points = second_player.hit_points - p1_damage

    result = round + '<br>' + '====================================' + '<br>'
    result = result + 'Первый игрок: ' + p1_weapon + ' ' + p1_tactic + '<br>'
    result = result + 'Второй игрок: ' + p2_weapon + ' ' + p2_tactic + '<br>'
    result = result + 'Первый игрок наносит урон: ' + str(p1_damage) + '<br>'
    result = result + 'Второй игрок наносит урон: ' + str(p2_damage) + '<br>'
    result = result + 'Первый игрок хп: ' + str(first_player.hit_points) + '<br>'
    result = result + 'Второй игрок хп: ' + str(second_player.hit_points) + '<br>'
    return result


if __name__ == '__main__':
    app.run(debug=True)
