from flask import Flask, render_template, request
import stats, impulse, damage

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
    stats1 = stats.get_first_player_stats(request)
    stats2 = stats.get_second_player_stats(request)

    impulse1 = impulse.get_1_impulse(stats1, stats2)
    impulse2 = impulse.get_2_impulse(stats1, stats2)

    damage1 = damage.get_1_damage(stats1, stats2)
    damage2 = damage.get_2_damage(stats1, stats2)

    effect1 = impulse1 * damage1
    effect2 = impulse2 * damage2

    if effect1 > effect2:
        return '1 player wins'
    else:
        return '2 player wins'


if __name__ == '__main__':
    app.run(debug=True)
