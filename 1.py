import os

def build_G(csv_file):

    #init graph dict
    g={}

    #here we open csv file
    with open(csv_file,'r') as f:
        cont=f.read()

    #here we get field content
    for line in cont.split('\n'):
        if line != '':

            fields=line.split(';')

            #build origin node
            if fields[0] not in g.keys():
                g[fields[0]]={}

            #build destination node         
            if fields[1] not in g.keys():
                g[fields[1]]={}

            #build edge origin>destination
            if fields[1] not in g[fields[0]]:
                g[fields[0]][fields[1]]=(fields[2])

    return g

def main():

    #filename
    csv_file="mynode.csv"

    #build graph
    G=build_G(csv_file)

    #G is now a python dict
    #G={'27': {}, '75': {'14': 2.85, '23': 0.9}, '89': {}, '14': {'75': 2.9}, '23': {'27': 4.9, '89': 3.49, '14': 1.29}}


    #write to file
    f = open('dotgraph.txt','w')
    f.writelines('digraph G {\nnode [width=.3,height=.3,shape=circle,style=filled,color=skyblue];\noverlap="false";\nrankdir="LR";\n')
    f.writelines

    for i in G:
        for j in G[i]:
            #get weight
            weight = G[i][j]
            s= '      '+ i
            s +=  ' -> ' +  j + ' [dir=none,label="' + str(G[i][j]) + '",penwidth='+str(weight)+',color=black]'
            if s!='      '+ i:
                s+=';\n'
                f.writelines(s)

    f.writelines('}')
    f.close()

    #generate graph image from graph text file
    os.system("dot -Tjpg -omyImage.jpg dotgraph.txt")

main()