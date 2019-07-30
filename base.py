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
            #print("#find_max " + str(find_max))
            max_sum = max(find_max)

            counter_reg = 0
            counter_pol = 0
            counter_hon = 0
            counter_hum = 0

            if sum_reg == max_sum:
                counter_reg = counter_reg + 1
            if sum_pol == max_sum:
                counter_pol = counter_pol + 1
            if sum_hon == max_sum:
                counter_hon = counter_hon + 1
            if sum_hum == max_sum:
                counter_hum = counter_hum + 1

            if counter_reg + counter_pol + counter_hon + counter_hum > 1:
                print('Невозможно определить тип речи, так как число элементов совпадает')
            elif max_sum == 0:
                print('Невозможно дать ответ')
            elif max_sum == sum_reg:
                print('Это нейтральная речь')
            elif max_sum == sum_pol:
                print('Это нейтрально-вежливая речь')
            elif max_sum == sum_hon:
                print('Это учтивая речь')
            elif max_sum == sum_hum:
                print('Это скромная речь')
            else:
                print('Определить тип речи в данном предложении пока что невозможно')

        except ValueError as v:
            print('Что-то пошло не так')

JapaneseSentiment()
