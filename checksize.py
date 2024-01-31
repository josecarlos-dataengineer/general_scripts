# import sys
# sys.path.append(r'C:\Users\SALA443\Desktop\Projeto_B3\checksize\Lib\site-packages')
import os
import pandas as pd

class size_scan():
    def get_size(start_path):
        
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(start_path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                # skip if it is symbolic link
                if not os.path.islink(fp):
                    total_size += os.path.getsize(fp)

        return total_size

    def to_list(path):
        
        # path = r'C:\Users\SALA443\desktop\projetos'
        dirs = os.listdir(path)
        data = list()
        for d in dirs:
            try:                
                dd = os.path.join(path, d)
                # print(f"{d}, {size_scan.get_size(d)}, 'bytes'")
                dt = f"{dd},{d}, {size_scan.get_size(dd)}, 'bytes'"
                data.append(dt)
            except Exception as e:
                pass
        
        return data
    
    def to_df(path):         
            
        dt = size_scan.to_list(path)

        list2 = []
        for d in range(len(dt)):
            list2.append(list(dt[d].split(',')))            

        df = pd.DataFrame(list2,columns = ['path','name','size','category'])
        
        return df    
    
    def to_graph(path:str,n:int):        
              
        df = size_scan.to_df(path)
        df['size'] = pd.to_numeric(df['size'])
        df = df.sort_values('size',ascending=False)
        df = df[:n]
        fig = df.plot.barh(x='name',y='size')
        
        

        
                    