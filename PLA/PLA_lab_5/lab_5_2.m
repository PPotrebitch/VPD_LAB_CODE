f = [1 1 2 2 2 3 3 3 3 4 4 4 4 5 5 5 6 6 6 7 7 7 8 9 10]; 
s = [4 8 1 5 10 4 6 8 9 1 8 9 10 2 6 9 7 8 9 3 5 9 2 10 5]; 
Graph = digraph(f, s); 
figure; 
h = plot(Graph); 
title('Веб-страницы'); 

% Инициализация матрицы M нулями
M = zeros(10);

% Заполнение матрицы M
for k = 1:length(f)
    i = s(k);
    j = f(k);
    outDegree = outdegree(Graph, j);
    if outDegree ~= 0
        M(i, j) = 1 / outDegree;
    end
end

% Нахождение собственных значений и собственных векторов
[eigenvecs, eigenvals] = eig(M);
eigenvals = diag(eigenvals);

pr = centrality(Graph,'pagerank','MaxIterations',200,'FollowProbability',1); 
nodes = {'Page_1'; 'Page_2'; 'Page_3'; 'Page_4'; 'Page_5'; 'Page_6'; 'Page_7'; 'Page_8'; 'Page_9'; 
'Page_10'} 
pr_table = table(nodes, pr, 'VariableNames', {'WebPage', 'PageRank'}) 
