S=load('movement_of_point.mat');
S=cell2mat(struct2cell(S));
time=S.time;
y= S.y;

N = numel(time);
T= time(end);
Fs= N/T;
f = -Fs/2:(1/T):Fs/2-(1/T) + ((1/T)/2)*mod(N,2);

FFT_before = fft(y);
FFT_shift = fftshift(FFT_before);

mag = abs(FFT_shift/N);
phase = angle(FFT_shift);

tiledlayout(3,1)

nexttile
plot(time,y)
title('Input signal')
xlabel('Time(sec)');


nexttile
plot(f,mag)
xlim([-15 15])
title('Magnitude')
xlabel('Frequency(Hz)');
nexttile

plot(f,phase)
xlim([-15 15])
title('Phase')
xlabel('Frequency(Hz)');


[M,I]=max(mag);
A=f(I);
B=f((N+1)-(I-1)); %realnumber signal의 dft변환 그래프가 y축대칭임을 이용
fprintf('Frequency at max magnitude is %f\n',A);
fprintf('Frequency at max magnitude is %f\n',B);
