clear; close all; clc; hold off;
format long 


% Data Read
load TQQQ_MinMaxB.txt

A=TQQQ_MinMaxB(:,2);
Percent = 1:length(A);length(A)

ClsVal = TQQQ_MinMaxB(:,7);
MaxVal = TQQQ_MinMaxB(:,8);
MinVal = TQQQ_MinMaxB(:,9);

for i = 2:2945
  Percent(i) = ClsVal(i)/ClsVal(i+1) -1 ;
end
Percent(1) = 0 ;
Percent(2946) = 0;

% MDD Caculation
MDD_cls    = ClsVal;
MDD_Max    = MaxVal;
MDD_Min    = MinVal;

MDD_HighLow_cls = MDD_cls ;
MDD_HighLow_Max = MDD_Max ;
MDD_HighLow_Min = MDD_Min ;

MDD_HighLow_cls = 0 ;
MDD_HighLow_Max = 0 ;
MDD_HighLow_Min = 0 ;

MDD_cls(1) = 0;
MDD_Min(1) = 0;
MDD_Max(1) = 0;

for i = 2:2946
  %______________ MDD 하락시 전고점값 유지
  if  (MDD_cls(i) > ClsVal(i-1))        % 전고점 회복 
       MDD_cls(i) = ClsVal(i) ;
  else MDD_cls(i) = MDD_cls(i-1) ; endif % 전고점 아래

  if  (MDD_Min(i) > MinVal(i-1)) 
       MDD_Min(i) = MinVal(i) ;
  else MDD_Min(i) = MDD_Min(i-1) ; endif

  if  (MDD_Max(i) > MaxVal(i-1)) 
       MDD_Max(i) = MaxVal(i) ;
  else MDD_Max(i) = MDD_Max(i-1) ; endif

  %______________ 깊은 전고점 찾기
  if  (MDD_cls(i) > ClsVal(i-1))        % 전고점 회복
       MDD_HighLow_cls(i) = 0 ;        
  else MDD_HighLow_cls(i) = 1 ; endif  % 전고점 아래

  if  (MDD_Min(i) > MinVal(i-1)) 
       MDD_HighLow_Max(i) = 0 ; 
  else MDD_HighLow_Max(i) = 1 ; endif
  
  if  (MDD_Max(i) > MaxVal(i-1)) 
       MDD_HighLow_Min(i) = 0 ; 
  else MDD_HighLow_Min(i) = 1 ; endif

end

#{
%______________ 전고점 회복 기간
cls_Count = MDD_HighLow_cls ;
for i = 1:2946
  if ( MDD_HighLow_cls(i) ) 
        clsCount(i) = 0;
  else  clsCount(i) = clsCount(i) + 1 ; endif
end
______________ Max. Min 전고점
#}

% 
ClsPercentMDD = abs(MDD_cls-ClsVal)./MDD_cls;
MinPercentMDD = abs(MDD_cls-MinVal)./MDD_cls;
MaxPercentMDD = abs(MDD_cls-MaxVal)./MDD_cls;
ClsPercentMDD(1)=0;
MinPercentMDD(1)=0;
MaxPercentMDD(1)=0; 

diff_A = (MaxVal./MinVal-1)*100;
cdf_diff_A = diff_A;
cdf_diff_A = 0 ;

for i = 2:2946
  cdf_diff_A(i) = cdf_diff_A(i-1) + diff_A(i);
end

cdf_diff_AInv = 1-cdf_diff_A./max(cdf_diff_A);
cdf_diff_A    =   cdf_diff_A./max(cdf_diff_A);

referCurve    = 1:length(cdf_diff_A);
referCurve    =   referCurve./max(referCurve);
referCurveInv = 1-referCurve./max(referCurve);

%___________ stock Nomalize.
% log and Nomalizel
% set minimum 1. for log
logClsVal = ClsVal./min(ClsVal) ;
logMaxVal = MaxVal./min(MaxVal) ;
logMinVal = MinVal./min(MinVal) ;

% set maximum 1 for display
logClsVal = log(logClsVal)./max(logClsVal) ;
logMaxVal = log(logMaxVal)./max(logMaxVal) ;
logMinVal = log(logMinVal)./max(logMinVal) ;

%___________ MDD Nomalize.
MDD_cls(1) = 0;
MDD_Min(1) = 0;
MDD_Max(1) = 0;

% log and Nomalizel
% set minimum 1. for log
logMDD_ClsVal = MDD_cls./min(MDD_cls) ;
logMDD_MaxVal = MDD_Max./min(MDD_Max) ;
logMDD_MinVal = MDD_Min./min(MDD_Min) ;

% set maximum 1 for display
logMDD_ClsVal = log(logMDD_ClsVal)./max(logMDD_ClsVal) ;
logMDD_MaxVal = log(logMDD_MaxVal)./max(logMDD_MaxVal) ;
logMDD_MinVal = log(logMDD_MinVal)./max(logMDD_MinVal) ;

%___________________________
%__________ Display Zone. __
%___________________________
hold on;grid;
plot(logClsVal,'b');
plot(logMaxVal,'m');
plot(logMinVal,'c');
title('TQQQ MDD curve');
ylabel('MDD & stock price');
xlabel('Day');


figure,hold on;grid;
plot(ClsPercentMDD*8,'b')
plot(MaxPercentMDD*8,'g')
plot(MinPercentMDD*8,'r');

plot(logMDD_ClsVal,'m');
plot(logMDD_MaxVal,'y');
plot(logMDD_MinVal,'c');
plot(logClsVal,'r');
plot(logMaxVal,'g');
plot(logMinVal,'b');

title('TQQQ MDD curve');
ylabel('MDD & stock price');
xlabel('Day');


figure,plot(ClsPercentMDD,'b');grid; hold on;
       plot(MaxPercentMDD,'r')
       plot(MinPercentMDD,'g');
       plot(cdf_diff_A)
       plot(referCurve,'r')

plot(logClsVal) ;
plot(logMaxVal) ;
plot(logMinVal) ;

title('TQQQ MDD curve');
ylabel('MDD & stock price');
xlabel('Day');

figure, 
plot(MDD_HighLow_Min); grid; hold on;

plot(ClsPercentMDD,'b')
plot(MaxPercentMDD,'g')
plot(MinPercentMDD,'r');

plot(abs(log(MDD_cls)),'m');
plot(abs(log(MDD_Max)),'y');
plot(abs(log(MDD_Min)),'c');


% max(ClsPercentMDD)
% ans = 0.699220747064556
% sum(ClsPercentMDD)
% ans = 346.1133344321364
% sum(ClsPercentMDD)/length(ClsPercentMDD)
% ans = 0.117485856901608

whos
