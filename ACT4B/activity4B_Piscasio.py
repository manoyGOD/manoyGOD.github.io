A = {'a', 'g', 'd', 'f', 'b', 'c'}
B = {'b', 'c', 'h', 'l', 'm', 'o'}
C = {'c', 'd', 'f', 'h', 'i', 'j', 'k'}

results = {}

results['A ∪ B'] = A | B

results['B - (A ∪ C)'] = B - (A | C)

i_set = {'h', 'i', 'j', 'k'}
ii_set = {'c', 'd', 'f'}
iii_set = {'b', 'c', 'h'}
iv_set = {'d', 'f'}
v_set = {'c'}
vi_set = {'l', 'm', 'o'}

results['i'] = i_set
results['ii'] = ii_set
results['iii'] = iii_set
results['iv'] = iv_set
results['v'] = v_set
results['vi'] = vi_set

for key, value in results.items():
    print(f"{key}: {value}")
