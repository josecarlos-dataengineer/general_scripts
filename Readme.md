## checksize.py
O arquivo **checksize.py** contém uma classe chamada size_scan, que contém os métodos **to_list**, **to_df** e to_graph.
Estas funções permitem checar o tamanho das pastas de um dado caminho, por exemplo:
***size_scan.to_graph(path=r'C:\Users\SALA443',n=12)***: Neste caso a função retornará um gráfico de barras com os doze maiores pastas do diretório informado como path. As outras funções funcionam do mesmo jeito, mas não tem o segundo arqgumento, uma vez que sempre retornam todos as pastas do diretório informado.