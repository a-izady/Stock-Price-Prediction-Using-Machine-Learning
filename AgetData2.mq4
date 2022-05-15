//+------------------------------------------------------------------+
//|                                                     AgetData.mq4 |
//|                                          Copyright © 2005,fxpars |
//|                                                                  |
//+------------------------------------------------------------------+
#property copyright "Copyright © 2005, fxpars"
#property link      "http://forum.fxpars.com/forum/"
#property indicator_chart_window

#define   _DAYSECONDS_ 86400; // 1day = 24hr * 60min * 60sec = 86400sec

int start()
  {
   datetime dt=0;//D'2002.01.01 00:00'; 
   int handle;
   int cnt;
   int _year = 2002;
   int _month = 1;
   int _day = 1;
   string strline;
   string name_file;
   if(Period()!=60)
   if( Period()!=24*60)
   //if( Period()!=4*60)
   //if( Period()!=1) 
   return 0;
   //Delete minur time frame file -----------
   //if(Period()==60)
   //FileDelete(Symbol()+ "5"+ ".prn",false);
   //-------------------------------------
   name_file = Symbol()+ Period()+ ".csv";
   handle = FileOpen(name_file , FILE_CSV|FILE_WRITE, "\t");
   if(handle<1)
      {
      Print("cannot open file error-",GetLastError());
      return(0);
      }
      
   else {
   FileWrite(handle,"<DATE>,<TIME>,<OPEN>,<HIGH>,<LOW>,<CLOSE>,<VOL>");
   int counted_bars=Bars-1;
   int barss=MathMin(10000,counted_bars);
   dt=TimeCurrent();
   dt=dt-(barss+1)*_DAYSECONDS_;    
   for (cnt=barss;cnt>=0;cnt--)
      {
      if (Period() < 1440)
         {
//         strline = DoubleToStr(_year,0);
//         if (_month < 10)
//            strline = strline + "0" + DoubleToStr(_month,0);
//         else
//            strline = strline + DoubleToStr(_month,0);
//      
//         if (_day < 10)
//            strline = strline + "0" + DoubleToStr(_day,0);
//         else
//            strline = strline + DoubleToStr(_day,0);
                  int d=1;
                  /*if(TimeDayOfWeek(dt)==0)
                  d++;
                  if(TimeDayOfWeek(dt)==6)
                  {d++;d++;}*/
                  dt=dt+d*_DAYSECONDS_;    
                  if(dt>TimeCurrent())
                  {
                  Alert("ellit_confirm Error 98453 :Current Time Over Load " + Symbol());
                  return 0;
                  }             
         }
      else
         {
         //strline = TimeToStr(Time[cnt],TIME_DATE|TIME_SECONDS);
         //strline = StringSubstr(strline,0,4) + StringSubstr(strline,5,2) + StringSubstr(strline,8,2);
         dt=Time[cnt];
         }
         strline = TimeToStr(dt,TIME_DATE|TIME_SECONDS);
         strline = StringSubstr(strline,0,4) + StringSubstr(strline,5,2) + StringSubstr(strline,8,2);
      strline = strline + ",0," + DoubleToStr(Open[cnt],4) + "," + DoubleToStr(High[cnt],4) + "," + DoubleToStr(Low[cnt],4) + "," + DoubleToStr(Close[cnt],4) + "," + DoubleToStr(Volume[cnt],0);
      FileWrite(handle, strline);
      
      if (Period() < 1440)
         {
         if (_day < 28) 
            _day++; 
         else 
            {
            _day = 1;
            _month++;
            if (_month > 12)
               {
               _month = 1;
               _year++;
               }
            }
         }
      }
   FileClose(handle);
   return(0);
  }
 }

