import numpy as np

def random_predict(number:int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        if number == predict_number:
            break # выход из цикла, если угадали
    return(count)

print(f'Количество попыток: {random_predict()}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.
    Returns:
        int: Число попыток
    Method: дихотомии, делим отрезок на двое до тех пор  пока не сойдется к числу. 
    """

    # Ваш код начинается здесь
    
    def div_list(a_list):
      """
      деление отрезка на 2 части
      Args: a_list (int, list): Список int от 0 до 100
      Returns: две части от начального  списка 
      """  
      
      if len(a_list)>=2:
          return a_list[0:int(len(a_list)/2)] , a_list[int(len(a_list)/2):]
      else:
          return a_list,a_list
    
    a_list=list(range(0,101))  #   формируем список чисел который далее будем разбивать на части     
    b_part,c_part =  div_list(a_list)    

    count=0 
    while len(b_part)>=2 or len(c_part)>=2:  #цикл разбиения начального списка на части, включающие заданное число
        count+=1
        if number in b_part:
            b_part,c_part =  div_list(b_part) 
        else:    
            b_part,c_part =  div_list(c_part)
      
    # if b[0]==number:
    #     count+=1
    #     print(b[0])
    # else: print(c[0])

    count+=1   # увеличиваем на 1 т.к. для точного ответа необходима доп проверка  какое именно число из двух списоков соответствует

    # Ваш код заканчивается здесь

    return count



# RUN
if __name__ == '__main__':
    score_game(game_core_v3)