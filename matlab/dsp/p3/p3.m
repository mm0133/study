clc
clear
close all;
x1 = 0:1:500;
x2 = 1:1:500;
x3 = 1:1:500;
y1=sin(10*pi*x1/1000);
y2=sin(40*pi*x2/1000);
y3=sin(100*pi*x3/1000);
y=[y1,y2,y3];

f1= -500:2/3:500;
FFT_before = fft(y);
FFT_shift = fftshift(FFT_before);

mag1 = abs(FFT_shift/1500);
phase1 = unwrap(angle(FFT_shift));



x1 = 0:1:2000;
x2 = 1:1:2000;
x3 = 1:1:2000;
y1=sin(10*pi*x1/1000);
y2=sin(40*pi*x2/1000);
y3=sin(100*pi*x3/1000);
y_=[y1,y2,y3];

f2= -500:1/6:500;
FFT_before = fft(y_);
FFT_shift = fftshift(FFT_before);

mag2 = abs(FFT_shift/6000);
phase2 =unwrap(angle(FFT_shift));




tiledlayout(3,2)

nexttile
plot(y)
xlim([0 1500])
title('Input signal t=0.5')
xlabel('Time(millisec)');

nexttile
plot(y_)
title('Input signal t=2')
xlabel('Time(millisec)');
xlim([0 6000])

nexttile
plot(f1,mag1)
xlim([0 60])
title('Magnitude')
xlabel('Frequency(Hz)');

nexttile
plot(f2,mag2)
xlim([0 60])
title('Magnitude')
xlabel('Frequency(Hz)');


nexttile
plot(f1,phase1)
xlim([0 60])

title('Phase')
xlabel('Frequency(Hz)');

nexttile
plot(f2,phase2)
xlim([0 60])

title('Phase')
xlabel('Frequency(Hz)');
