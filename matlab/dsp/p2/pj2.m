clc
clear
close all;
% 이미지 읽고 회색이미지로 변환
temp=double(imread('Jobs.jpg'));
Jobs=255*rgb2gray(temp/255);
temp=double(imread('Musk.jpg'));
Musk=255*rgb2gray(temp/255);


%이미지 fft 후 magnitude, phase 분리
FJobs=fft2(Jobs);
Jobs_magnitude = abs(FJobs);
Jobs_phase = angle(FJobs);

FMusk=fft2(Musk);
Musk_magnitude = abs(FMusk);
Musk_phase = angle(FMusk);


% 각각 서로다른 magnitude와 phase합성
Fimg1 = Jobs_magnitude.*exp(1i*Musk_phase);
img1= ifft2(Fimg1);

Fimg2 = Musk_magnitude.*exp(1i*Jobs_phase);
img2= ifft2(Fimg2);


% 출력부
tiledlayout(2,2)

nexttile
imshow(uint8(Jobs))
title('Jobs')

nexttile
imshow(uint8(Musk))
title('Musk')

nexttile
imshow(uint8(img1))
title('Jobs magnitude + Musk phase')

nexttile
imshow(uint8(img2))
title('Musk magnitude + Jobs phase')
