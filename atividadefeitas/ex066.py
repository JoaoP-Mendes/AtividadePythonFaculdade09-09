populacao_a = 80000
populacao_b = 200000
crescimento_a = 0.03  # 3%
crescimento_b = 0.015  # 1.5%

anos = 0

print("Evolução das populações:")
print(f"Ano {anos}: País A = {populacao_a:.0f} habitantes | País B = {populacao_b:.0f} habitantes")

# Loop enquanto a população A for menor que a população B
while populacao_a < populacao_b:
    # Calcula o crescimento populacional para cada país
    populacao_a += populacao_a * crescimento_a
    populacao_b += populacao_b * crescimento_b
    anos += 1
    
    print(f"Ano {anos}: País A = {populacao_a:.0f} habitantes | País B = {populacao_b:.0f} habitantes")

print(f"\nSerão necessários {anos} anos para a população do país A ultrapassar ou igualar a do país B.")
print(f"População final - País A: {populacao_a:.0f} habitantes")
print(f"População final - País B: {populacao_b:.0f} habitantes")