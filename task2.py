
def get_total_score(part2=False):
    with open('inputs/input2.txt', 'r') as f:
        input_rounds = f.read().split('\n')
        me_wins = {'A': 'Y', 'B': 'Z', 'C': 'X'}
        op_plays, me_plays = ['A', 'B', 'C'], ['X', 'Y', 'Z']
        score_total = 0
        for r in input_rounds:
            op, me = r.split(' ')  # split line into me, op play
            op_i = op_plays.index(op)  # get index for op play

            if part2:  # part 2 - overwrite my play
                me_win, me_draw = me_wins.get(op), me_plays[op_i]  # win from wins, draw the same as op
                me_loss = list(set(me_plays).difference({me_win, me_draw}))[0]  # if not win or draw it's loss
                me = me_draw if me == 'Y' else (me_win if me == 'Z' else me_loss)  # X=loss, Y=draw, Z=win

            me_i = me_plays.index(me)  # get index for op play
            score_partial = ((me_wins.get(op) == me) * 6) + ((op_i == me_i) * 3)  # 0=loss, 3=draw, 6=win; 1|0 * 3|6
            score_round = (me_i + 1) + score_partial  # 1=rock, 2=paper, 3=scissor; index + 1
            score_total = score_total + score_round

        print(f'Part {2 if part2 else 1}: {score_total}')


get_total_score()
get_total_score(part2=True)
