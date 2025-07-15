import pandas as pd
import matplotlib.pyplot as plt 
tabela = pd.DataFrame({
    'idade':[20, 23, 18, 45, 31],

    'nome' : ['joao', 'maria', 'vini', 'pedro', 'jose']

})

plt.hist(tabela['idade'])
