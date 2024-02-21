clc
clear all;
file = "U_I_2.csv"; 
for i = 1:10
    data = readmatrix(file(i));
    U_input_1 = data(:, 1)
    U_input_2 = data(:, 3)
    I_out_1 = data(:, 2)
    I_out_2 = data(:, 4)
    figure(1)
    plot(U_input_1, I_out_1)
    xlabel("U, volt")
    ylabel("I, Am")
    grid
    figure(2)
    plot(U_input_2, I_out_2)
    xlabel("U, volt")
    ylabel("I, Am")
    grid
end