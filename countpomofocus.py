availableTime = int(input(f'Waktu yang anda sediakan untuk menjalankan metode (dalam satuan menit): '))
n_pomodoro = 0
n_shortBreak = 0
n_longbreak = 0
remainderTime = 0
while availableTime>0:
    # print(availableTime)
    if availableTime>=40:
        availableTime-=25
        n_pomodoro+=1
        if n_pomodoro%4 == 0:
            n_longbreak+=1
            availableTime-=15
        else:
            n_shortBreak+=1
            availableTime-=5
    elif availableTime>=30:
        availableTime-=25
        n_pomodoro+=1
        if n_pomodoro%4 == 0:
            remainderTime+=availableTime
            availableTime-=availableTime
        else:
            n_shortBreak+=1
            availableTime-=5
            remainderTime+=availableTime
            availableTime-=availableTime
    elif availableTime>=25:
        availableTime-=25
        n_pomodoro+=1
        remainderTime+=availableTime
        availableTime-=availableTime
    else:
        remainderTime+=availableTime
        availableTime-=availableTime
        
print(f"iterasi pomodoro yang bisa dihasilkan: {n_pomodoro}")
print(f"dengan waktu sisanya: {remainderTime} menit")
print(f"jumlah short break: {n_shortBreak}x")
print(f"jumlah long break {n_longbreak}x")
            
        
        
    