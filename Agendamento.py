import schedule
import time


#tomar banho de 8 em 8h
def fazerTarefa():
    print("Tomar Banho")

#schedule.cada.tempo.fazer
schedule.every(8).hours.do(fazerTarefa)

#acordar as 8 todo dia
def Acordar():
    print("ACORDAAAA!!!!")

schedule.every().day.at('08:00').do(Acordar)


while 1:
    schedule.run_pending()
    time.sleep(1)