def time(time):
    if time < 60:
        if time < 10:                                             return f"00:0{time}"
        else:                                                     return f"00:{time}"
    else:
        if time >= 60:                                            minute = time // 60
            second = time % 60                                    if minute < 10 and second < 10:
                return f"0{minute}:0{second}"
            elif minute >= 10 and second < 10:
                return f"{minute}:0{second}"                      elif minute >= 10 and second >= 10:
                return f"{minute}:{second}"                       else:
                return f"0{minute}:{second}"
