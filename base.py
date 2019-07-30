import suffixes
import extraconditions

def JapaneseSentiment():
    while True:
        try:
            text = input('Введите текст на японском языке: ')
            punct = ['、', ',', '…', '.', '‥', '。', '〜', '!', '?', ':', '？', '！', '「', '」', '『', '』', '・', '【', '】', '｛', '｝', '[', ']']
            no_punct = ""
            for sym in text:
                if sym not in punct:
                    no_punct += sym
            words = no_punct.split(' ')

            suffRegular = suffixes.SuffRegular.copy()
            suffPolite = suffixes.SuffPolite.copy()
            suffHonorific = suffixes.SuffHonorific.copy()
            suffHumble = suffixes.SuffHumble.copy()
            rootsVerbsHonorific = suffixes.RootsVerbsHonorific.copy()
            rootsVerbsHumble = suffixes.RootsVerbsHumble.copy()
            ExtraConditions = extraconditions.extraConditions

            j_suffixes = [suffRegular, suffPolite, suffHonorific, suffHumble]
            j_roots = [rootsVerbsHonorific, rootsVerbsHumble]
            for word in words:
                for suff in j_suffixes:
                    for key in suff.keys():
                        if key in word:
                            isExtraCondition = False
                            for a,b in ExtraConditions:
                                if key == a and b in word:
                                    isExtraCondition = True
                            if isExtraCondition == False:
                                print("#suffix " + key)
                                suff[key] = suff[key] + 1

                for root in j_roots:
                    for key in root.keys():
                        if key in word:
                            root[key] = root[key] + 1

            sum_reg = sum(suffRegular.values())
            sum_pol = sum(suffPolite.values())
            sum_hon = sum(suffHonorific.values()) + sum(rootsVerbsHonorific.values())
            sum_hum = sum(suffHumble.values()) + sum(rootsVerbsHumble.values())

            find_max = [sum_reg, sum_pol, sum_hon, sum_hum]
            print("#find_max " + str(find_max))
            max_sum = max(find_max)
            if max_sum == 0:
                print('Невозможно дать ответ')
            elif max_sum == sum_reg:
                print('Это нейтральная речь')
            elif max_sum == sum_pol:
                print('Это нейтрально-вежливая речь')
            elif max_sum == sum_hon:
                print('Это учтивая речь')
            elif max_sum == sum_hum:
                print('Это скромная речь')

        except ValueError as v:
            print('Что-то пошло не так')

JapaneseSentiment()
