clc
clear all;
file = ["data-100", "data-80", "data-60", "data-40", "data-20","data20","data40", "data60", "data80" "data100"];
voltages = [-100, -80, -60, -40, -20, 20, 40, 60, 80, 100];
k_all = [];
Tm_all = [];
w_all = [];
for i = 1:10
    data = readmatrix(file(i));
    time = data(:, 1);
    angle = data(:, 2)*pi/180;
    U_pr = voltages(i);
    par0 = [0.1, 0.000256];
    fun = @(par, time)U_pr*par(1)*(time-par(2)*(1-exp(-time/par(2))));
    par = lsqcurvefit(fun, par0, time, angle);
    k = par(1);
    Tm = par(2);
    k_all(i,:) = k;
    Tm_all(i,:) = Tm;
    w_nls = U_pr * k;
    w_all(i,:) = w_nls;
    time_apr = 0:0.01:1;
    theta = U_pr*k*(time_apr - Tm*(1-exp(-time_apr/Tm)));
    figure(1)
    plot(time_apr, theta)
    xlabel("time, s")
    ylabel("angle, rad")
    hold on




    omega = data(:, 3)*pi/180;
    theta = U_pr*k*(1-exp(-time_apr/Tm));
    figure(2)
    plot(time_apr, theta)
    hold on
    plot(time, omega)
    xlabel("time, s")
    ylabel("omega, rad/s")
    hold on
end
figure(1)
grid
legend("-100%", "-80%", "-60%", "-40%", "-20%", "20%", "40%", "60%", "80%", "100%", 'Location','eastoutside')
exportgraphics(gca,'All_graphs_angle.pdf')
figure(2)
grid
legend("-100%", "-80%", "-60%", "-40%", "-20%", "20%", "40%", "60%", "80%", "100%", 'Location','eastoutside')
exportgraphics(gca,'All_graphs_omega.pdf')
figure("Name","Зависимость omega от напряжения")
plot(voltages, w_all)
grid
xlabel("voltage, %")
ylabel("omega, rad/s")
exportgraphics(gca,'Зависимость omega от напряжения.pdf')
figure("Name","Зависимость величены Tm от напряжения")
plot(voltages, Tm_all)
grid
xlabel("voltage, %")
ylabel("Tm, s")
exportgraphics(gca,'Зависимость  величены Tm от напряжения.pdf')