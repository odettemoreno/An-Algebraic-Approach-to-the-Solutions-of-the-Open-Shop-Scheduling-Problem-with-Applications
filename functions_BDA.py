import numpy as np
import scipy
import math as m



def nmax(matriz):   
    filmax=max([sum(i) for i in matriz ])
    colmax=max([sum(i) for i in matriz.T ])
    
    return filmax,colmax


def tratin(matdeT):
    numf,numc= matdeT.shape
    contlong=[]

    
    for i in range(numf):
        contlong.append(np.sum(matdeT[i], axis=0))
    
    indices=[]
    k=len(contlong)

    
    for i in range(k):
        n=max(contlong)
        indices.append(contlong.index(n))
        contlong[contlong.index(n)]=0
        
        
    MatrizT=np.array([matdeT[indices[0]]])
    for i in range(numf-1): 
        MatrizT=np.vstack([MatrizT,matdeT[indices[i+1]]])
    
    MatrizT.tolist()
    
    numeromaximo=sum(MatrizT[0])

    MP=[]
    
    for vector in MatrizT:
        MA=[]
        j=1
        for elemento in vector:
            MA.append([elemento,j])
            j+=1       
        MP.append(MA)
    
    return MP,numeromaximo 


# COLUMNAS

def TMyTEFSC(Lac,numeromaximo):
    nf=len(Lac)
    nc=(len(Lac)+1)*(numeromaximo)
    msj=np.zeros((nf,nc))-1
    
    for k in range(Lac[0][0][0]):
        msj[0][k]=Lac[0][0][1]
        

    Lac[0].pop(0)
        
        
    
    for j in range(nc):
        
        for i in range(nf):
            
            if len(Lac[i])!=0 and msj[i][j]==-1:
      
                mataux=[row[j:j+Lac[i][0][0]] for row in msj[:]]
                listaux=[]
                 
                for fila in mataux:
                    for elemento in fila:
                        listaux.append(int(elemento))
                    
            
                
                if set(listaux)&set([Lac[i][0][1]])==set():
                     
                    for m in range(Lac[i][0][0]):
                        msj[i][j+m]=Lac[i][0][1]
                         
                    Lac[i].pop(0)
               
                else:
                    msj[i][j]=0
                    
            else:
                pass
                
                
    msj=msj.tolist()   
            
    contdmd=[]
    
    for i in msj:
        contdmd.append(i.count(-1))
        
    ndmd=nc-min(contdmd) 
    
    msj=np.array(msj)
    msj=msj.T[0:ndmd] 
    msj=msj.T
    
    return msj.tolist()   


def conttFSC(cada):  
    sumadordeceros=0
    sumadordeunos=0
    
    for i in cada:
      sumadordeceros=sumadordeceros+i.count(0)
      sumadordeunos=sumadordeunos+i.count(-1)
    
    return sumadordeceros,sumadordeunos



def TMyTEFSF(elem,numf,numc):
    MatrizAux1 = [] 
    MatrizAux2 = [] 
    MatrizAux3 = [] 
     
    
    k=0
    
    for i in elem[0]:
        n,m = i
        
        k = [m]*n
        
        MatrizAux1 = MatrizAux1+k
    
    longpf=len(MatrizAux1)
    
    
    for i in range(longpf*(numf-1)):
        MatrizAux1=MatrizAux1+[-1]
    MatrizAux2=[MatrizAux1]
    
    i=0
    
    
    for i in range(numf-1):
        p=0
        i+=1
        MatrizAux5=[]
        
        for j in range(numc):
            
            
            nu,inn = elem[i][j]
            MatrizAux3 = [fila[p:p+nu+1] for fila in MatrizAux2]
            MatrizAux4 = []
            
            for M in MatrizAux3:
                MatrizAux4 = MatrizAux4 + M
           
            
            while True:
                
                if {inn} & set(MatrizAux4)!=set():
                   
                    
                    p=p+1
                    MatrizAux3 = [fila[p:p+nu] for fila in MatrizAux2]
                    MatrizAux4 = []
                    
                    for M in MatrizAux3:
                        MatrizAux4 = MatrizAux4 + M
                     
                           
                else:
                    break
                
                MatrizAux5.append(0) 
            
            MatrizAux5=MatrizAux5+[inn]*nu
           
            p=p+nu
            
        
        longg=len(MatrizAux2[0])-len(MatrizAux5)
        
        
        for i in range(longg):
            MatrizAux5=MatrizAux5+[-1]
        
        MatrizAux2.append(MatrizAux5)
     
        
    MatrizAcumulacionFinalA=[]
    eliminador=[]
     
    
    for i in MatrizAux2:
        eliminador.append(i.count(-1))
        cantelim=min(eliminador)
    
    
    for i in MatrizAux2:
        
        if cantelim==0:
          pass
    
        else:    
            for c in range(cantelim):
              i.remove(-1)
              
        MatrizAcumulacionFinalA.append(i)
    
    
    return MatrizAcumulacionFinalA


def conttFSF(cada):
    
    sumadordeceros=0
    sumadordeunos=0
    
    for i in cada:
           
      sumadordeceros=sumadordeceros+i.count(0)
      sumadordeunos=sumadordeunos+i.count(-1)
    
    return sumadordeceros,sumadordeunos

def selector(matriz):
    ttotal=sum([sum(fila) for fila in matriz])
    sumcol=max([sum(fila) for fila in matriz.T])
    sumfil=max([sum(fila) for fila in matriz])
    maxfc=max(sumcol,sumfil)
    return maxfc,ttotal

def colsum(matriz):
    val=[]
    a,b=matriz.shape

    for i in range(b):
        su = 0;
        for j in range(a):
            su =su+ matriz[j][i]
        val.append(su)

        
    return val

def Ttotal(val):
    suma=0
    for i in range(len(val)):
        suma=suma+val[i]
    return suma



def vertices(matrizc):
    Vertices=[]
    for i in matrizc:
        for j in i:
            Vertices.append(j)
    Vertices=list(sorted(set(Vertices)))
    
    return Vertices
        
        
def sucessor_sequence(polygons,Vertices):
    Sucessor_sequence=[]
    vertex=0
    for vertice in Vertices:
        Sucessor_sequence.append([])
        for i in range(len(polygons)):
            for j in range(len(polygons[i])):
                if int(vertice)==int(polygons[i][j]):
                    Sucessor_sequence[vertex].append(i+1)
        vertex=vertex+1


    for i in range(len(Sucessor_sequence)):
      Sucessor_sequence[i].append(Sucessor_sequence[i][0])
    
      
      
    return Sucessor_sequence
        
        
    
def dimensions(sum_rows1,numf,Sucessor_sequence,Vertices):
    dimension=0
    truncated=[]
    multiplicity=[]
    for i in sum_rows1:
        
        if i==1:
            multiplicity.append(2)
            truncated.append(1)
        if i==0:
            multiplicity.append(0)
        if i!=1 and i!=0:
            multiplicity.append(1)
    
  
    mul=0
    for i in multiplicity:
      mul=mul+i
      
    dimension=2*numf
    for k,val in    enumerate(sum_rows1):
       dimension=dimension+val*(multiplicity[k]*val-1)
       
    loops=0
    Loops=[]

    for i in range(len(Sucessor_sequence)):
        loopsc=0
        k=1
        for j in range(len(Sucessor_sequence[i])-1):
            if int(Sucessor_sequence[i][k])==int(Sucessor_sequence[i][j]):
                loops=loops+1
                loopsc=loopsc+1
         
            k=k+1
        Loops.append(loopsc)


    center=1+mul+numf-len(Vertices)+loops-len(truncated)

    o=0
    for k,val in enumerate(sum_rows1):
        o=o+val*multiplicity[k]
    entropy=0
    for k,val in enumerate(sum_rows1):
        if val!=0:
            alpha=(val*multiplicity[k])/o
            entropy=entropy+(alpha*m.log2(alpha))
    entropy=-entropy

    
    return dimension,center,entropy,loops,Loops
    
    