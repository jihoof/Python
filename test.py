# 승리 규칙 딕셔너리 (key가 value를 이김)
rules = {
    '가위': '보',
    '바위': '가위',
    '보': '바위'
}

if comp_choice == player_choice:
    print('[결과] 무승부입니다.')
    enter()
else:
    if rules[comp_choice] == player_choice:
        print('[결과] 컴퓨터 공격, 플레이어 수비입니다.')
        enter()
        who_win = 'comp'
    else:
        print('[결과] 플레이어 공격, 컴퓨터 수비입니다.')
        enter()
        who_win = 'player'
