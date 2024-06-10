def BMI(person_height_cm, person_weight):
    m = person_height_cm/100
    personBMI = person_weight/pow(m, 2)

    # 理想體重算法
    best_weight = pow(m, 2) * 22

    if  personBMI < 18.5:
        increase = best_weight - person_weight
        weigh_info = f" 體重過輕!"
        advice = f" 建議增重{increase:.2f}公斤, 為您的理想體重！"
        return person_height_cm, person_weight, personBMI, weigh_info, advice
    elif personBMI >= 18.5 and personBMI < 24:
        weigh_info = f" 恭喜~「健康體重」!"
        advice = f" 請繼續保持！"
        return person_height_cm, person_weight, personBMI, weigh_info, advice
    elif personBMI >= 24 and personBMI < 27:
        reduce_weight = person_weight - best_weight
        weigh_info = f"「過重」，小心囉！"
        advice = f" 建議減少{reduce_weight:.2f}公斤, 為理想體重！"
        return person_height_cm, person_weight, personBMI, weigh_info, advice
    elif personBMI >= 27 and personBMI < 30:
        reduce_weight = person_weight - best_weight
        weigh_info = f"「輕度肥胖」了，要小心囉！ "
        advice = f" 建議減少{reduce_weight:.2f}公斤, 為理想體重！"
        return person_height_cm, person_weight, personBMI, weigh_info, advice
    elif personBMI >= 30 and personBMI < 35:
        reduce_weight = person_weight - best_weight
        weigh_info = f" 啊～「中度肥胖」，需要注意囉!"
        advice = f" 建議減少{reduce_weight:.2f}公斤, 為理想體重！"
        return person_height_cm, person_weight, personBMI, weigh_info, advice
    else:
        reduce_weight = person_weight - best_weight
        weigh_info = f" 天啊～「重度肥胖」，趕緊減重！"
        advice = f" 建議減少{reduce_weight:.2f}公斤, 為理想體重！"
        return person_height_cm, person_weight, personBMI, weigh_info, advice

def dict_info(name, height_cm, weight) -> list[dict]:

    person_height_cm, weight, personBMI, weigh_info, advice = BMI(height_cm, weight)
    info = {}
    info['name'] = name
    info['height_cm'] = person_height_cm
    info['weight'] = weight
    info['BMI'] = f"{personBMI:.2f}"
    info['weigh_info'] = weigh_info
    info['advice'] = advice
    lis:list[dict] = [info]
    return lis