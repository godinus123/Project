clear; close all;
clc;
format long 

load QQQ_editB.txt

A=QQQ_editB(:,2);
Percent = 1:length(A);


for i = 1:2946
  if (i == 1) Percent(1) = 0 ;
  else        Percent(i) = A(i)/A(i+1) -1 ;  endif
end
Percent(2947) = 0;




localMax    = A;
localMax(1) = 0;

for i = 2:2947
  if (localMax(i) > localMax(i-1)) localMax(i) = A(i) ;
  else        localMax(i) = localMax(i-1) ; endif
end

absMDD = localMax-A;
percentMDD = absMDD./localMax;

plot(A);
figure, plot(Percent);
figure,plot(log(A));
figure, plot(localMax);
figure, plot(absMDD);
figure, plot(percentMDD*100,'g');grid; hold on;
p=90*log(A)./max(log(A))-20; 
plocalMax=90*log(localMax)./max(log(localMax))-20; 
plot(p,'r');
plot(plocalMax,'b');
title('TQQQ MDD curve');
ylabel('MDD & stock price');
xlabel('Day');



whos





