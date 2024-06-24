clc
clear all

m_p = 15.6 / 1000;
r_p = 23/2/1000;
J_ed = m_p*r_p^2/2;
i = 48;
J = i^2 *J_ed ;
L = 0.0047;
r = 11.12 / 1000;
BAZA = (145.55+22.25)/1000;
k_s = 285;
k_r = 690;
k_e = 0.269307532254461;
k_m = k_e;
R = 5.719189347486274;


data = readmatrix("file.txt");
th = data(:, 1);
x  = data(:, 2);
y = data(:, 3);

data05_0 = readmatrix("Coord 0.5_0.txt");
th_1 = data05_0(:, 1);
x_1  = data05_0(:, 2);
y_1 = data05_0(:, 3);

figure(1)
plot(x, y,'LineWidth', 3,'Color',"blue", "DisplayName", "Really locatio map of robot")
title("location map of robot");
legend("Location", "southoutside");
xlabel("x, м");
ylabel("y, м");
grid on;
set(gca, 'GridAlpha', 0.7);
set(gca, 'LineWidth', 1.1);
fontsize(gcf, 20, "points");
hold on
% 
% figure(2)
% plot(x_1, y_1,'LineWidth', 3,'Color',"red", "DisplayName", "Really locatio map of robot")
% title("location map of robot");
% legend("Location", "southoutside");
% xlabel("x, м");
% ylabel("y, м");
% grid on;
% set(gca, 'GridAlpha', 0.7);
% set(gca, 'LineWidth', 1.1);
% fontsize(gcf, 20, "points");
            
goal_x = -1;
goal_y = 0;
figure(3)
Timer = 62.1;
simulin_data = sim("lab4.slx");
plot(simulin_data.x.Data, simulin_data.y.Data, 'LineWidth', 2,...
      'DisplayName', "cимуляция", "Color", 'red')
hold on;
goal_x = 1;
goal_y = 0;
figure(3)
Timer = 48.75;
simulin_data = sim("lab4.slx");
plot(simulin_data.x.Data, simulin_data.y.Data, 'LineWidth', 2,...
          'DisplayName', "cимуляция", "Color", 'g')
hold on;
goal_x = 0;
goal_y = -1;
figure(3)
Timer = 51.25;
simulin_data = sim("lab4.slx");
plot(simulin_data.x.Data, simulin_data.y.Data, 'LineWidth', 2,...
           'DisplayName', "cимуляция", "Color", 'm')
hold on;
goal_x = 0;
goal_y = 1;
figure(3)
Timer = 51.25;
simulin_data = sim("lab4.slx");
plot(simulin_data.x.Data, simulin_data.y.Data, 'LineWidth', 2,...
        'DisplayName', "cимуляция", "Color", 'y')
            
 xlabel("x, м");
ylabel("y, м");
grid on;
set(gca, 'GridAlpha', 0.7);
set(gca, 'LineWidth', 1.1);
fontsize(gcf, 20, "points");