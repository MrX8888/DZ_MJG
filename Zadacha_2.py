import math
import numpy as np

# Дано:
F_a = 1          # Площадь выходного сечения идеального сопла Лаваля, (м^2)
P_t = 2e6        # Полное давление, (Па)
T_t = 1000       # Температура торможения, (К)
P0 = 1e5         # Давление среды, куда происходит истечение, (Па)
R = 287          # Газовая постоянная, (Дж/кг*К)
gamma = 1.4

# Решение:

P_a = P0        # Т.к. режим течения расчётный

# Определим ГДФ для выходного сечения:

lymda = 1.857
pi = P_a / P_t
tao = 1 - ((gamma-1)/(gamma+1))*math.pow(lymda, 2)
q = lymda * math.pow(((gamma+1)/2), (1/(gamma-1))) * math.pow(1 - ((gamma-1)/(gamma+1))*math.pow(lymda, 2), (1/(gamma-1)))
E = pi / tao

# Определим скорость и температуру потока в выходном сечении:

T_a = tao * T_t                                     # Темепратура в выходном сечении
W_k = math.sqrt((2*gamma/(gamma+1))*R*T_t)          # Скорость в критическом сечении
W_a = lymda * W_k                                   # Скорость в выходном сечении

print (f"Скорость в выходном сечении: {W_a}", f"Температура в выходном сечении: {T_a}", sep="\n")

# Определим расход воздуха
W_a = lymda * W_k                                   # Скорость в выходном сечении
Rho_t = P_t / (R * T_t) # Плотность
Rho_a = E * Rho_t
G = W_a * Rho_a * F_a

print (f"Расход воздуха: {G}")

# Диаметр критического сечения сопла:

lymda_k = 1
tao_k = 1 - ((gamma-1)/(gamma+1)) * lymda_k
pi_k = math.pow((1 - ((gamma-1)/(gamma+1)) * lymda_k), gamma/(gamma-1))
E_k = pi_k / tao_k
Rho_k = E_k * Rho_t
#F_k = G / (W_k * Rho_k)
F_k = (F_a * W_a * Rho_a) / (W_k * Rho_k)
d_k = math.sqrt((4 * F_k)/np.pi)
print (f"Диаметр критического сечения: {d_k}")
