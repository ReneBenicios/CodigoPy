def relogio():
        h = 24
        while h >= 0:
            m = 59
            while m >= 0:
                s = 59
                while s >= 0:
                    print(f"{h:02}:{m:02}:{s:02}")
                    s -= 1
                    #sleep(1)
                m -= 1
            h -= 1
    
