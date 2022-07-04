'''
Melisa ATEŞ
atesmel12@gmail.com
'''
# Bu kodda Enine arama(breadth first search) yapılır
#İlk olarak verilen vertexin en yakınlarına gidilir ve sonrasında komşu vertexlerde de aynı işlem yapılılarak arama sonlanır.
import math

'''
"black":2 kez ziyaret edilmiş ve kuyruktan çıkartılmış.
"white":Hiç ziyaret edilmemiş.
"gray":1 kez ziyaret edilmiş.
'''
colors = {"black": (0, 0, 0),
          "white": (255, 255, 255),
          "gray": (128, 128, 128)
         }

class Point:
    def __init__(self,color, d, pi,id):
        self.id=id
        self.color = color
        self.d = d
        self.pi = pi

def bfs(G, s):

    s.color=colors.get("gray")
    s.d=0
    s.pi=None
    
    Q = []
    Q.append(s)
    
    while Q:

       m = Q.pop(0)
       print (m.id, end = " ") 
       
       neighbor=generate_neighbor_edges(G,m.id)#Sıradan çıkarılan vertexin komşuları çağırılır.

       for i in neighbor:#vertexin komşu vertexleri içinde gezilir.
        #neigbor dizisi çoklu elemanlardan oluşursa diye o elemanların içinde de gezilerek komşu vertexlere ulaşılır.
            for v in i:
                for g in vx:  # Komşu vertexlerin tüm özelliklerine ulaşmak için g kullanılır.
                    if g.id==v: # id'si v olan objeye ulaşılır.

                        if g.color==colors.get("white"): # not visited
                            
                            g.color=colors.get("gray")
                            g.d=m.d+1
                            g.pi=m
                            Q.append(g)
                        
                        m.color = colors.get("black")  # visited
                        print (m.color, end = " ") 

def generate_neighbor_edges(graph,vertex):#graph'taki verilen vertexin komşu id'leri return edilir.
    
    edges = []
    for key,value in graph.items():
        if key==vertex:
            edges.append(value)

    return edges



if __name__ == '__main__':
    #Bir graf oluşturulur.
    G = {
    '5' : ['3','7'],
    '3' : ['2', '4'],
    '7' : ['8'],
    '2' : [],
    '4' : ['8'],
    '8' : []
    }
 

    vx=[]#Herbir vertex objesini tutar.
    for key,value in G.items():
        #İlk başta her bir vertex'e başlangıç değerleri verilerek renkleri beyaz yapılır.
        obj=Point(colors.get("white"), math.inf, None,key)
        vx.append(obj)

        
    print("Breadfirst:")
    #Grafta istenilen vertexin adresleri tutan vx dizisindeki adresi gönderilir.
    bfs(G,vx[0])
