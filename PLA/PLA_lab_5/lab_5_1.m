clear all; close all; clc
% Создаем матрицу смежности для графа
adj_matrix = zeros(20);

% Кластеры:
% 1 группа: Вершины 1-5
% 2 группа: Вершины 6-10
% 3 группа: Вершины 11-15
% 4 группа: Вершины 16-20

% Связи внутри каждой группы
for i = 1:5
    for j = 1:5
        if i ~= j
            adj_matrix(i, j) = 1;
        end
    end
end

for i = 6:10
    for j = 6:10
        if i ~= j
            adj_matrix(i, j) = 1;
        end
    end
end

for i = 11:15
    for j = 11:15
        if i ~= j
            adj_matrix(i, j) = 1;
        end
    end
end

for i = 16:20
    for j = 16:20
        if i ~= j
            adj_matrix(i, j) = 1;
        end
    end
end

% Связи между группами
adj_matrix(3, 7) = 1;
adj_matrix(7, 3) = 1;

adj_matrix(12, 18) = 1;
adj_matrix(18, 12) = 1;

adj_matrix(9, 18) = 1;
adj_matrix(18, 9) = 1;

adj_matrix(3, 12) = 1;
adj_matrix(12, 3) = 1;

% Построение графа
Graph = graph(adj_matrix);
figure;
h = plot(Graph);
title('Друзья');

% Расчет матрицы Лапласа
deg_matrix = diag(sum(adj_matrix));
laplacian_matrix = deg_matrix - adj_matrix;

[eigenvecs, eigenvals] = eig(laplacian_matrix);
eigenvals = diag(eigenvals);

% Кластеризация для k = 2
k = 2;
eigenvecs_2 = eigenvecs(:, 1:k);
[idx, C] = kmeans(eigenvecs_2, k);

% Настройка цветов для вершин
colors = zeros(20, 3);
for i = 1:20
    if idx(i) == 1
        colors(i, :) = [1 0 0]; % красный
    elseif idx(i) == 2
        colors(i, :) = [0 1 0]; % зеленый
    end
end

% Построение графа с кластеризацией
figure;
h_c_1 = plot(Graph);
title('Кластеризация для k=2');
h_c_1.NodeColor = colors;

% Кластеризация для k = 3
k = 3;
eigenvecs_3 = eigenvecs(:, 1:k);
[idx, C] = kmeans(eigenvecs_3, k);

colors = zeros(20, 3);
for i = 1:20
    if idx(i) == 1
        colors(i, :) = [1 0 0]; % красный
    elseif idx(i) == 2
        colors(i, :) = [0 1 0]; % зеленый
    elseif idx(i) == 3
        colors(i, :) = [0 0 1]; % синий
    end
end

% Построение графа с кластеризацией
figure;
h_c_2 = plot(Graph);
title('Кластеризация для k=3');
h_c_2.NodeColor = colors;

% Кластеризация для k = 4
k = 4;
eigenvecs_4 = eigenvecs(:, 1:k);
[idx, C] = kmeans(eigenvecs_4, k);

colors = zeros(20, 3);
for i = 1:20
    if idx(i) == 1
        colors(i, :) = [1 0 0]; % красный
    elseif idx(i) == 2
        colors(i, :) = [0 1 0]; % зеленый
    elseif idx(i) == 3
        colors(i, :) = [0 0 1]; % синий
    elseif idx(i) == 4
        colors(i, :) = [1 0 1]; % пурпурный
    end
end
% Построение графа с кластеризацией
figure;
h_c_3 = plot(Graph);
title('Кластеризация для k=4');
h_c_3.NodeColor = colors;

% Кластеризация для k = 5
k = 5;
eigenvecs_5 = eigenvecs(:, 1:k);
[idx, C] = kmeans(eigenvecs_5, k);

colors = zeros(20, 3);
for i = 1:20
    if idx(i) == 1
        colors(i, :) = [1 0 0]; % красный
    elseif idx(i) == 2
        colors(i, :) = [0 1 0]; % зеленый
    elseif idx(i) == 3
        colors(i, :) = [0 0 1]; % синий
    elseif idx(i) == 4
        colors(i, :) = [1 0 1]; % пурпурный
    elseif idx(i) == 5
        colors(i, :) = [1 1 0]; % желтый
    end
end


% Построение графа с кластеризацией
figure;
h_c_4 = plot(Graph);
title('Кластеризация для k=5');
h_c_4.NodeColor = colors;

% Кластеризация для k = 6
k = 6;
eigenvecs_6 = eigenvecs(:, 1:k);
[idx, C] = kmeans(eigenvecs_6, k);

colors = zeros(20, 3);
for i = 1:20
    if idx(i) == 1
        colors(i, :) = [1 0 0]; % красный
    elseif idx(i) == 2
        colors(i, :) = [0 1 0]; % зеленый
    elseif idx(i) == 3
        colors(i, :) = [0 0 1]; % синий
    elseif idx(i) == 4
        colors(i, :) = [1 0 1]; % пурпурный
    elseif idx(i) == 5
        colors(i, :) = [1 1 0]; % желтый
    elseif idx(i) == 6
        colors(i, :) = [0 1 1]; % голубой
    end
end

% Построение графа с кластеризацией
figure;
h_c_5 = plot(Graph);
title('Кластеризация для k=6');
h_c_5.NodeColor = colors;
