clear all;
format short g;
clc;
Cmin=90;
Cmax=156;
n=3;
k1=(Cmax-Cmin)/n;


for k=1:k1
    dim=0;
    fix=Cmin+k*n;
   

    
    %PARTITIONS
    P1= [Cmax];
    for i=1:Cmax-P1(1)
        P1=[P1,1];
    end
    
    P2=[fix];
    for i=1:Cmax-fix
        P2=[P2,1];
        dim=dim+1/2;
    end
    dim=dim+(fix*fix/2)+(Cmax*Cmax/2);
          
    G=graph();
    
    %ADD NODES
    for i=1:n
        H=addnode(G,i);
    end

    %ADD edges
    h=0;  
    for i=1:length(P1)
        m=0; 
        for j=1:floor(P1(i)/2)
            H=addedge(H,1+h+m,P1(i)-m+h,1);
            m=m+1;
        end
        h=h+P1(i);
    end
    
    h=0;
    for i=1:length(P2)
        m=0;
        for j=1:floor(P2(i)/2)       
            H=addedge(H,1+h+m,P2(i)-m+h,2);
            m=m+1;
        end
        h=h+P2(i);
        
    end
 
    
    

    [c,edgecycles] = allcycles(H);
    
    
    Cycles={};
    

    
    for i=1:length(c)
        Cycles=[Cycles,sort(c{i})];
    end
    
    
    bins = conncomp(H);
    number_of_paths=length(unique(sort(bins)));
    paths={};
    
    
    
    for component=1:number_of_paths
        list=[];
        count=1;
        for element=bins
            if element==component
                list=[list,count];
            end
            count=count+1;
        end
        list=sort(list);
        paths=[paths;{list}];
    end
    
    
    row=[];
    for i=1:length(Cycles)
        for j=1:length(paths)
            if isequal(Cycles{i},paths{j})
                row=[row,j];
            end
        end
     
    end
    c=0;
    for i=row
        paths(i-c,:)=[];
        c=c+1;
    end
    index=2*length(Cycles)+length(paths)-1;
    
    
    
    %PLOT MEANDER
    p=plot(H,LineWidth=2,NodeColor='r',EdgeColor='b');
    fontSize = 20;
    title('Meander graph $\mathcal{G}_{\frac{\lambda_{22}}{\lambda_{0}}}$' ,'Interpreter', 'latex');

end

