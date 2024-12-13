from manim import *
import numpy as np

COLORES = [
    RED,
    GREEN,
    YELLOW,
    PURPLE,
    ORANGE
]

# Глобальные данные для куба
CUBE_VERTICES = np.array([
    [-1, 1, 1, -1, -1, 1, 1, -1],
    [-1, -1, 1, 1, -1, -1, 1, 1],
    [-1, -1, -1, -1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
])

CUBE_FACES = [
    [0, 1, 5, 4],  # Передняя грань
    [1, 2, 6, 5],  # Правая грань
    [2, 3, 7, 6],  # Задняя грань
    [3, 0, 4, 7],  # Левая грань
    [0, 1, 2, 3],  # Нижняя грань
    [4, 5, 6, 7]  # Верхняя грань
]

def bmatrix(a):
    """Возвращает LaTeX bmatrix с проверкой на целые числа."""
    if len(a.shape) > 2:
        raise ValueError('bmatrix может отображать максимум двумерные массивы')
    lines = []
    for row in a:
        formatted_row = []
        for num in row:
            if int(num) == num:  # Проверяем, является ли число целым
                formatted_row.append(str(int(num)))
            else:
                formatted_row.append(f"{num:.2f}")
        lines.append(' & '.join(formatted_row))
    rv = [r'\begin{bmatrix}']
    rv += ['  ' + line + r'\\' for line in lines]
    rv += [r'\end{bmatrix}']
    return '\n'.join(rv)

# Функция для создания осей и их подписей
def create_axes():
    axes = ThreeDAxes(
        x_range=[-5, 5, 1],
        y_range=[-5, 5, 1],
        z_range=[-5, 5, 1],
        axis_config={"stroke_width": 2}  # Уменьшаем толщину осей
    )

    # Подписываем оси с использованием Tex
    x_label = Tex("X", color=RED).next_to(axes.x_axis.get_end(), RIGHT)
    y_label = Tex("Y", color=GREEN).next_to(axes.y_axis.get_end(), UP)
    z_label = Tex("Z", color=BLUE).next_to(axes.z_axis.get_end(), OUT)

    return axes, x_label, y_label, z_label

# Функция для создания граней куба с новыми вершинами
def create_cube_faces(vertices, faces_indices, color=BLUE):
    cube_faces = []
    for face in faces_indices:
        polygon = Polygon(
            *[vertices[:3, i] for i in face],  # Извлекаем 3D координаты
            color=color, fill_opacity=0.5, stroke_color=WHITE
        )
        cube_faces.append(polygon)
    return cube_faces

# Функция для начальной отрисовки сцены с осями и кубом
def initialize_scene(scene):
    # Создание осей и подписей
    axes, x_label, y_label, z_label = create_axes()

    # Создание граней куба
    cube_faces = create_cube_faces(CUBE_VERTICES, CUBE_FACES, color=BLUE)

    # Настройка камеры
    scene.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)

    # Анимации осей и подписей
    scene.play(Create(axes))
    scene.play(Write(x_label), Write(y_label), Write(z_label))

    # Анимация отображения куба
    scene.play(*[Create(face) for face in cube_faces])

    return axes, x_label, y_label, z_label, cube_faces

# Функция для обновления граней куба после трансформаций
def update_cube_faces(scene, original_faces, new_vertices, faces_indices, color=RED):
    # Создание новых граней куба после трансформации
    new_cube_faces = create_cube_faces(new_vertices, faces_indices, color=color)

    # Анимация замены старых граней куба на новые
    scene.play(*[ReplacementTransform(original_faces[i], new_cube_faces[i]) for i in range(len(original_faces))])

    # Удаляем старые грани, заменяя их новыми
    scene.remove(*original_faces)

    return new_cube_faces

# Функция для анимации преобразования матрицы
def show_matrix_transformation(scene, transformation_matrix, latex_matrix, vertices, faces, color, text_old=None):
    # Преобразование вершин куба
    transformed_vertices = np.dot(transformation_matrix, vertices)

    # Создание объекта MathTex для LaTeX
    text = MathTex(latex_matrix)
    text.scale(0.7)
    text.to_corner(UL)

    # Удаление старого текста с анимацией
    if text_old:
        scene.play(Uncreate(text_old))

    scene.add_fixed_in_frame_mobjects(text)
    scene.play(Write(text))

    # Обновление граней куба с обновленными вершинами
    faces = update_cube_faces(scene, faces, transformed_vertices, CUBE_FACES, color=color)

    return faces, transformed_vertices, text

# Функция для плавного удаления куба и осей
def remove_cube_and_axes(scene, cube_faces, axes, x_label, y_label, z_label):
    # Плавное удаление граней куба
    scene.play(*[FadeOut(face) for face in cube_faces])

    # Плавное удаление осей и подписей
    scene.play(FadeOut(axes), FadeOut(x_label), FadeOut(y_label), FadeOut(z_label))

# Классы задач
class task1(ThreeDScene):
    def construct(self):
        # Инициализация сцены с осями и кубом
        axes, x_label, y_label, z_label, cube_faces = initialize_scene(self)

        # Пауза для отображения результата
        self.wait(5)

        # Плавное удаление куба и осей
        remove_cube_and_axes(self, cube_faces, axes, x_label, y_label, z_label)

class task2(ThreeDScene):
    def construct(self):
        # Инициализация сцены с осями и кубом
        axes, x_label, y_label, z_label, cube_faces = initialize_scene(self)

        scale_matrices = [
            np.array([
                [2, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]),
            np.array([
                [1, 0, 0, 0],
                [0, 2, 0, 0],
                [0, 0, 0.5, 0],
                [0, 0, 0, 1]
            ]),
            np.array([
                [0.5, 0, 0, 0],
                [0, 0.5, 0, 0],
                [0, 0, 2, 0],
                [0, 0, 0, 1]
            ]),
        ]

        now_vertices = CUBE_VERTICES
        text_old = None

        for index, scale_matrix in enumerate(scale_matrices):
            color = COLORES[index]
            scale_latex = bmatrix(scale_matrix)

            # Вызов функции для анимации матрицы
            cube_faces, now_vertices, text_old = show_matrix_transformation(
                self, scale_matrix, scale_latex, now_vertices, cube_faces, color=color, text_old=text_old
            )

            # Пауза для отображения результата
            self.wait(1)

        # Плавное удаление куба и осей
        remove_cube_and_axes(self, cube_faces, axes, x_label, y_label, z_label)

class task3(ThreeDScene):
    def construct(self):
        # Инициализация сцены с осями и кубом
        axes, x_label, y_label, z_label, cube_faces = initialize_scene(self)

        # Матрицы перемещения:
        # 1. Перемещение по оси X на 2 единицы
        # 2. Перемещение по оси Y на -1.5 единицы
        # 3. Перемещение по оси Z на 1 единицу
        # 4. Перемещение по вектору (1, 1, 1)
        translation_matrices = [
            # Перемещение по X на +2
            np.array([
                [1, 0, 0, 2],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]),
            # Перемещение по Y на -1.5
            np.array([
                [1, 0, 0, 0],
                [0, 1, 0, -1.5],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]),
            # Перемещение по Z на +1
            np.array([
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ]),
            # Перемещение по вектору (1, 1, 1)
            np.array([
                [1, 0, 0, 1],
                [0, 1, 0, 1],
                [0, 0, 1, 1],
                [0, 0, 0, 1]
            ])
        ]

        # Начальные вершины куба
        now_vertices = CUBE_VERTICES
        text_old = None

        # Векторы перемещения для визуализации
        translation_vectors = [
            np.array([2, 0, 0]),    # Вектор вдоль X
            np.array([0, -1.5, 0]), # Вектор вдоль Y
            np.array([0, 0, 1]),    # Вектор вдоль Z
            np.array([1, 1, 1])     # Произвольный вектор
        ]

        # Текстовые описания перемещений
        translation_descriptions = [
            "Перемещение на 2 единицы вдоль оси X",
            "Перемещение на -1.5 единицы вдоль оси Y",
            "Перемещение на 1 единицу вдоль оси Z",
            "Перемещение по вектору (1, 1, 1)"
        ]

        for index, translation_matrix in enumerate(translation_matrices):
            color = COLORES[index]
            translation_latex = bmatrix(translation_matrix)

            # Добавляем текстовое описание перемещения
            description = Text(translation_descriptions[index], font_size=24)
            description.to_corner(UR)
            self.add_fixed_in_frame_mobjects(description)

            # Добавляем вектор перемещения
            vector = translation_vectors[index]
            arrow = Arrow(ORIGIN, vector, color=color)
            self.add(arrow)

            # Вызов функции для анимации матрицы
            cube_faces, now_vertices, text_old = show_matrix_transformation(
                self, translation_matrix, translation_latex, now_vertices, cube_faces, color=color, text_old=text_old
            )

            # Пауза для отображения результата
            self.wait(2)

            # Убираем вектор и описание из сцены
            self.remove(arrow)
            self.remove(description)

        # Плавное удаление куба и осей
        remove_cube_and_axes(self, cube_faces, axes, x_label, y_label, z_label)

class task4(ThreeDScene):
    def construct(self):
        # Инициализация сцены с осями и кубом
        axes, x_label, y_label, z_label, cube_faces = initialize_scene(self)

        # Матрицы поворота:
        # 1. Поворот на 45 градусов вокруг оси X
        # 2. Поворот на 60 градусов вокруг оси Y
        # 3. Поворот на 30 градусов вокруг оси Z
        # 4. Поворот на 45 градусов вокруг вектора (1,1,1)
        rotation_matrices = [
            # Поворот на 45° вокруг оси X
            np.array([
                [1, 0, 0, 0],
                [0, np.cos(np.pi/4), -np.sin(np.pi/4), 0],
                [0, np.sin(np.pi/4), np.cos(np.pi/4), 0],
                [0, 0, 0, 1]
            ]),
            # Поворот на 60° вокруг оси Y
            np.array([
                [np.cos(np.pi/3), 0, np.sin(np.pi/3), 0],
                [0, 1, 0, 0],
                [-np.sin(np.pi/3), 0, np.cos(np.pi/3), 0],
                [0, 0, 0, 1]
            ]),
            # Поворот на 30° вокруг оси Z
            np.array([
                [np.cos(np.pi/6), -np.sin(np.pi/6), 0, 0],
                [np.sin(np.pi/6), np.cos(np.pi/6), 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ]),
            # Поворот на 45° вокруг вектора (1,1,1)
            # Матрица поворота вокруг произвольного вектора через формулу Родрига
            np.array([
                [0.8047, -0.3107, 0.5060, 0],
                [0.5060, 0.8047, -0.3107, 0],
                [-0.3107, 0.5060, 0.8047, 0],
                [0, 0, 0, 1]
            ])
        ]

        # Начальные вершины куба
        now_vertices = CUBE_VERTICES
        text_old = None

        # Векторы для отображения осей вращения
        vectors = [
            np.array([2, 0, 0]),  # Вектор оси X (красный)
            np.array([0, 2, 0]),  # Вектор оси Y (зеленый)
            np.array([0, 0, 2]),  # Вектор оси Z (синий)
            np.array([2, 2, 2])   # Произвольный вектор (1,1,1) (оранжевый)
        ]

        # Текстовые описания поворотов
        rotation_descriptions = [
            "Поворот на 45° вокруг оси X",
            "Поворот на 60° вокруг оси Y",
            "Поворот на 30° вокруг оси Z",
            "Поворот на 45° вокруг вектора (1,1,1)"
        ]

        for index, rotation_matrix in enumerate(rotation_matrices):
            color = COLORES[index]
            rotation_latex = bmatrix(rotation_matrix)

            # Добавляем текстовое описание поворота
            description = Text(rotation_descriptions[index], font_size=24)
            description.to_corner(UR)
            self.add_fixed_in_frame_mobjects(description)

            # Добавляем вектор, вокруг которого будет вращение
            vector = vectors[index]
            arrow = Arrow(ORIGIN, vector, color=color)
            self.add(arrow)

            # Вызов функции для анимации матрицы
            cube_faces, now_vertices, text_old = show_matrix_transformation(
                self, rotation_matrix, rotation_latex, now_vertices, cube_faces, color=color, text_old=text_old
            )

            # Пауза для отображения результата
            self.wait(2)

            # Убираем вектор и описание из сцены
            self.remove(arrow)
            self.remove(description)

        # Плавное удаление куба и осей
        remove_cube_and_axes(self, cube_faces, axes, x_label, y_label, z_label)


class task5(ThreeDScene):
    def construct(self):
        # Инициализация сцены с осями и кубом
        axes, x_label, y_label, z_label, cube_faces = initialize_scene(self)

        # Начальные вершины куба
        now_vertices = CUBE_VERTICES
        text_old = None

        # Вершина, вокруг которой будем вращать (первая вершина куба)
        pivot_point = CUBE_VERTICES[:3, 0]  # Берём первые три координаты первой вершины

        # Углы поворота (в радианах)
        angles = [np.pi/4, np.pi/3, np.pi/6]  # 45°, 60°, 30°
        
        # Матрицы для вращения вокруг вершины:
        # 1. Сдвиг в начало координат
        # 2. Поворот
        # 3. Сдвиг обратно
        for i, angle in enumerate(angles):
            # Матрица сдвига в начало координат
            translation_to_origin = np.array([
                [1, 0, 0, -pivot_point[0]],
                [0, 1, 0, -pivot_point[1]],
                [0, 0, 1, -pivot_point[2]],
                [0, 0, 0, 1]
            ])

            # Матрица поворота (для каждой оси)
            if i == 0:  # Вокруг X
                rotation = np.array([
                    [1, 0, 0, 0],
                    [0, np.cos(angle), -np.sin(angle), 0],
                    [0, np.sin(angle), np.cos(angle), 0],
                    [0, 0, 0, 1]
                ])
                axis_text = "X"
            elif i == 1:  # Вокруг Y
                rotation = np.array([
                    [np.cos(angle), 0, np.sin(angle), 0],
                    [0, 1, 0, 0],
                    [-np.sin(angle), 0, np.cos(angle), 0],
                    [0, 0, 0, 1]
                ])
                axis_text = "Y"
            else:  # Вокруг Z
                rotation = np.array([
                    [np.cos(angle), -np.sin(angle), 0, 0],
                    [np.sin(angle), np.cos(angle), 0, 0],
                    [0, 0, 1, 0],
                    [0, 0, 0, 1]
                ])
                axis_text = "Z"

            # Матрица сдвига обратно
            translation_back = np.array([
                [1, 0, 0, pivot_point[0]],
                [0, 1, 0, pivot_point[1]],
                [0, 0, 1, pivot_point[2]],
                [0, 0, 0, 1]
            ])

            # Полная матрица преобразования
            transform_matrix = np.dot(translation_back, np.dot(rotation, translation_to_origin))
            
            color = COLORES[i]
            transform_latex = bmatrix(transform_matrix)

            # Добавляем текстовое описание
            description = Text(f"Поворот на {int(angle * 180/np.pi)}° вокруг оси {axis_text}\nотносительно вершины ({pivot_point[0]}, {pivot_point[1]}, {pivot_point[2]})", 
                            font_size=24)
            description.to_corner(UR)
            self.add_fixed_in_frame_mobjects(description)

            # Отмечаем вершину, вокруг которой происходит вращение
            dot = Dot3D(point=pivot_point, color=color)
            self.add(dot)

            # Вызов функции для анимации матрицы
            cube_faces, now_vertices, text_old = show_matrix_transformation(
                self, transform_matrix, transform_latex, now_vertices, cube_faces, color=color, text_old=text_old
            )

            # Пауза для отображения результата
            self.wait(2)

            # Убираем описание и точку
            self.remove(description)
            self.remove(dot)

        # Плавное удаление куба и осей
        remove_cube_and_axes(self, cube_faces, axes, x_label, y_label, z_label)

