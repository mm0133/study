clc
clear
close all;

input_img=imread('Lena.png');
[LL, HL, LH, HH] = dwt2(input_img,'haar');

[LL_LL, LL_HL, LL_LH, LL_HH]= dwt2(LL,'haar');
HH_zero=HH.*0;

output_img = idwt2(LL, HL, LH, HH_zero,'haar');

A=[LL_LL, LL_HL];
B=[LL_LH, LL_HH];
C=[A;B];
A=[C,HL];
B=[LH,HH];
C=[A;B];

figure
tiledlayout(1,2)
nexttile
imshow(uint8(input_img))
title('Input image')

nexttile
imshow(uint8(output_img))
title('Output image')

figure
imshow(uint8(C))


