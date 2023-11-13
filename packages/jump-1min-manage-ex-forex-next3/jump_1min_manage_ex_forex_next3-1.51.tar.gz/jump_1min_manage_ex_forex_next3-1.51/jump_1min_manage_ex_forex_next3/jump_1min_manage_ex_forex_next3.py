import MetaTrader5 as mt5
import json

from decimal import Decimal


class Jump_1mine_manage:

    def __init__(self):
       fileObject = open("login.json", "r")
       jsonContent = fileObject.read()
       aList = json.loads(jsonContent)
       
       self.symbol_EURUSD = aList['symbol_EURUSD'] 
       self.decimal_sambol = int (aList['decimal_sambol'] )
       self.ratio_jump_1mine = float (aList['ratio_jump_1mine_manage'])
       self.ratio_jump_1mine_pip = float (aList['ratio_jump_1mine_pip'])
       self.max_body_1mine_jump_pip = float (aList['max_body_1mine_jump_pip'])
    
    def decimal(num , decimal_sambol):
        telo = '0.0'
        for i in range(decimal_sambol - 2):  
          telo = telo + "0"
        telo = telo + "1" 
        telo = float (telo)
        decimal_num = Decimal(str(num))
        rounded_num = decimal_num.quantize(Decimal(f'{telo}'))
        rounded_num = float(rounded_num)
        return rounded_num  

    def decimal_mov(decimal_sambol):
        x = 10
        for i in range(decimal_sambol):
           x = x * 10

        x = x / 10   

        return x    
    
    def avg_close_open():
     
     timecandel_1mine = mt5.copy_rates_from_pos(Jump_1mine_manage().symbol_EURUSD, mt5.TIMEFRAME_M1, 1 , 1000)

     difference_candels = []
     for candel_difference in timecandel_1mine:
            
           point_close = candel_difference[4]
           point_close = Jump_1mine_manage.decimal(point_close , Jump_1mine_manage().decimal_sambol)
           point_close = float(point_close) 

           point_open = candel_difference[1]
           point_open = Jump_1mine_manage.decimal(point_open , Jump_1mine_manage().decimal_sambol)
           point_open = float(point_open)
           
           difference = abs(point_close - point_open)
           difference = difference * Jump_1mine_manage.decimal_mov(Jump_1mine_manage().decimal_sambol)
           difference = int(difference)

           if Jump_1mine_manage().max_body_1mine_jump_pip > difference:
                 
                 difference_candels.append(difference)
     
     avg = sum(difference_candels)/len(difference_candels)
     
     avg = avg * Jump_1mine_manage().ratio_jump_1mine
     avg = round(avg , 1)
     print(avg)
     return avg
   
    def result_jump(timestamp_pulback):
       
       result = Jump_1mine_manage.avg_close_open() 
       result = float (result)
      #  print("result:" , result)

       timecandel = mt5.copy_rates_from(Jump_1mine_manage().symbol_EURUSD, mt5.TIMEFRAME_M1 , timestamp_pulback , 1)
    #    print("timecandel:" , timecandel)

       point_close = timecandel[0][4]
       point_close = Jump_1mine_manage.decimal(point_close , Jump_1mine_manage().decimal_sambol)  
       point_close = float(point_close) 
    #    print("point_close:" ,point_close)

       point_open = timecandel[0][1]
       point_open = Jump_1mine_manage.decimal(point_open , Jump_1mine_manage().decimal_sambol)
       point_open = float(point_open)
    #    print("point_open:" ,point_open)

       difference = abs(point_close - point_open)
       difference = difference * Jump_1mine_manage.decimal_mov(Jump_1mine_manage().decimal_sambol)
      #  difference = float(difference)
       difference = round(difference , 1)
       difference = float(difference)
      #  print("difference:" ,difference)

       candel_state = ""

       if point_open > point_close:
            candel_state = "red"
    
       elif point_open < point_close:
           candel_state = "green"
               
       elif point_open == point_close:
           candel_state = "doji"

      #  print("candel_state:" , candel_state)  
      #  print("ratio_jump_1mine_pip:" , Jump_1mine_manage().ratio_jump_1mine_pip)  


       if difference <= result and result < Jump_1mine_manage().ratio_jump_1mine_pip:
          return False
       
       elif (difference > result or difference > Jump_1mine_manage().ratio_jump_1mine_pip) and candel_state == "green":
          return [True , "green" ]
       
       elif (difference > result or difference > Jump_1mine_manage().ratio_jump_1mine_pip) and candel_state == "red":
          return [True , "red" ]
 


       