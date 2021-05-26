while[  # 延々と回す
    print(
        '相手の手 >> {}\n{}'.format(  # 相手の手
            your_hand,  # 相手の手
            ['引き分け', 'あなたの負け', 'あなたの勝ち'][
                hands[idx]-hands[your_hand]  # 勝敗判定(0:引き分け，1,-2:負け，2,-1:勝ち)
            ]
        )
    )
    for idx, your_hand, hands in  # 変数の代入代わりにforを使用
    zip(
        [input('あなたの手(グー，チョキ，パー) >> ')],  # 手を選択
        [__import__('random')  # random ライブラリをインポート
         .choice(['グー', 'チョキ', 'パー'])  # 手を選択
         ],
        [{'グー': -1, 'チョキ': 0, 'パー': 1}]  # 勝敗判定で必要な数値
    )
]:
    pass
