clc
clear all;
file = ["data-100", "data-80", "data-60", "data-40", "data-20","data20","data40", "data60", "data80" "data100"];
voltages = [-100, -80, -60, -40, -20, 20, 40, 60, 80, 100];
for i = 1:10
    data = readmatrix(file(i));
    time = data(:, 1);
    angle = data(:, 2)*pi/180;
    omega = data(:, 3)*pi/180;
    U_pr = voltages(i);
    figure(1)
    plot(time, omega)
    xlabel("time, s")
    ylabel("omega, rad/s")
    hold all
    par0 = [0.1, 0.000256];
    fun = @(par, time)U_pr*par(1)*(time-par(2)*(1-exp(-time/par(2))));
    par = lsqcurvefit(fun, par0, time, angle);
    k = par(1);
    Tm = par(2);
    w_nls = U_pr * k;
    time_apr = 0:0.01:1;
    theta = U_pr*k*(1-exp(-time_apr/Tm));
    plot(time_apr, theta)
    simulink_info = sim('LAB_sim');
    plot(simulink_info.omega.Time, simulink_info.omega.Data, '--')
    grid
    legend('experiment', 'omegaa', "simulink",  'Location','eastoutside')
    hold off
    graph_name = sprintf('Graph_omega_%d.pdf', i);
    exportgraphics(gca, graph_name)
end