##PyPond

##A digital life simulator inspired by NanoPond, Avida, Tierra, etc.

## Made by Paras Chopra (http://paraschopra.com/)

INST_NUMBER = 21 ## Total number of instructions

from random import *

class Cell:


    #cell_id is the id of the cell
    #location_x and location_y are the location of the cell in the pond
    #genome is an array containing genome of the cell
    #register is the variable holding value of the register
    #self_ptr is the pointer to the self genome
    #neigh_ptr is the pointer to the neighbour genome
    #parents is the array containing (ids of the parents and time) in order of ascending time
    #generation is the number of generations the cell has been through. A generation is increased everytime other cell writes into it 
    #facing points to direction the cell is facing: 0 top, 1 right, 2 down, 3 left

    def __init__(self, cell_id=0, energy=0, location_x=0,location_y=0, list_parents=[], genome=[], register=0, self_ptr=0, neigh_ptr=0, facing=0,color=0):

        self.cell_id=cell_id
        self.location_x=location_x
        self.location_y=location_y
        self.genome=genome
        self.register=register
        self.self_ptr=self_ptr
        self.neigh_ptr=neigh_ptr
        self.facing=facing
        self.list_parents=list_parents
        self.energy=energy
        self.color=color

    def add_parent(self,parent):
        self.list_parents[0:0]=[parent]


class Pond:

    #width is width of the pond
    #height is the height of the pond
    #pond_depth is the length of genome
    #initial_population is the initial population of the pong
    #mutation_rate is the rate of mutation while executing/reading/writing
    #permission_rate is the probability of granting permsision to read/write neighbours
    #mean_energy is alloted initially and after each run
    #variation_energy is the variation in energy alloted. If variation energy>mean_energy, this would mean that even negative energy can be allotted


    def __init__(self, width=500, height=500, pond_depth=100, initial_population=100, mutation_rate=0.005, permission_rate=0.01, mean_energy=5000, variation_energy=10000, mean_program_length=50, variation_program_length=20, dump=True, filename='test.csv'):
        
        self.width=width
        self.height=height
        self.initial_population=initial_population
        self.mutation_rate=mutation_rate
        self.permission_rate=permission_rate
        self.mean_energy=mean_energy
        self.variation_energy=variation_energy
        self.mean_program_length=mean_program_length
        self.variation_program_length=variation_program_length

        self.not_none=[] ## array to keep track of all cells present in the pond

        self.pond_depth=pond_depth

        self.cell_counter=1 ## counter to track cell's id
        
        self.pond=[]

        self.dump=dump

        if self.dump:
            self.filename=filename
            self.file=open(filename,'w')

            self.file.write(str(width)+"|"+str(height)+"|"+str(pond_depth)+"|"+str(mutation_rate)+"|"+str(permission_rate)+"|"+str(mean_energy)+"|"+str(variation_energy)+"|"+str(mean_program_length)+"|"+str(variation_program_length)+"\n")

        ##create blank cells

        for i in range(width):

            self.pond.append([])

            
            self.pond[i]=[None]*height

            for j in range(height):
                
                location_x=i
                location_y=j
                cell_id=self.cell_counter
                facing=randint(0,3)
                genome=[0]*self.pond_depth ## default genome

                temp=Cell(location_x=location_x,location_y=location_y,energy=0,cell_id=cell_id,facing=facing,genome=genome,list_parents=[])
                temp.energy=self.mean_energy+randint(-1*self.variation_energy,1*self.variation_energy)

                if temp.energy<0:
                    temp.energy=0
                
                self.generate_random_genome(temp)
                
                self.pond[location_x][location_y]=temp

                if self.dump:
                    self.dump_cell(temp, 0)
                
                self.cell_counter=self.cell_counter+1

        ##generate cells at random locations


        for i in range(initial_population):
            

            location_x=randint(0,width-1)
            location_y=randint(0,height-1)

            cell=self.pond[location_x][location_y]

            while [cell.location_x,cell.location_y] in self.not_none:
                location_x=randint(0,width-1)
                location_y=randint(0,height-1)
                cell=self.pond[location_x][location_y]
                
            
            #self.generate_random_genome(cell)

            #cell.energy=self.mean_energy+randint(-1*self.variation_energy,1*self.variation_energy)

            #if cell.energy<0:
                #cell.energy=0

            #if self.dump:
                #self.dump_cell(cell, 0)
                
            self.not_none.append([location_x,location_y])


    def run(self,execution_runs=10000):
        if execution_runs>0:
            for i in range(1,execution_runs+1):
                self.run_once(i)

        else:
            i=1
            running=True
            while running:
                for event in pygame.event.get():
                    if event.type == QUIT: 
                        running=False
                    else: 
                        self.run_once(i)
                        i=i+1
        if self.dump:
            self.file.close()


    #execution runs is the number of times execution should run.. at one time, only one program is executed

    def run_once(self,i=0):

        rand_cell=None
        neigh=None

        rand_cell=randint(0,len(self.not_none)-1) # pick a random cell
        
        rand_cell=self.pond[self.not_none[rand_cell][0]][self.not_none[rand_cell][1]]

        rand_cell.register=0
        rand_cell.self_ptr=0
        rand_cell.neigh_ptr=0

        permission=self.get_permission_status(rand_cell)
        neigh=self.get_neighbour(rand_cell)

        print i,rand_cell.cell_id,neigh.cell_id
        
        #execute it

        stop=False
        j=0

        modified_cells=[]
        
        while j<len(rand_cell.genome):

            if rand_cell.energy==0: stop=True
            
            rand_cell.energy=rand_cell.energy-1

            
            inst=rand_cell.genome[j]

            if random()<=self.mutation_rate: ##mutation probability
                inst=randint(0,INST_NUMBER-1)

            if stop==True: break
                
            if inst==0: #STOP
                stop=True

            elif inst==1: ##NOOP
                pass

            elif inst==2: ## PERM (sets 0 in register if permission is there)
                if permission:
                    rand_cell.register=0

            elif inst==3: ##INC
                rand_cell.register=(rand_cell.register+1) % INST_NUMBER

            elif inst==4: ##DEC
                rand_cell.register=(rand_cell.register-1) % INST_NUMBER

            elif inst==5: ##INCSELFPTR

                rand_cell.self_ptr=(rand_cell.self_ptr+1) % self.pond_depth

            elif inst==6: ##DECSELFPTR

                rand_cell.self_ptr=(rand_cell.self_ptr-1) % self.pond_depth

            elif inst==7: ##INCNEIGHPTR

                rand_cell.neigh_ptr=(rand_cell.neigh_ptr+1) % self.pond_depth                

            elif inst==8: ##DECNEIGHPTR

                rand_cell.neigh_ptr=(rand_cell.neigh_ptr+1) % self.pond_depth           

            elif inst==9: #READSELF
                if random()<=self.mutation_rate: ##mutation probability
                    rand_cell.register=randint(0,INST_NUMBER-1)
                else:
                    rand_cell.register=rand_cell.genome[rand_cell.self_ptr]
                

            elif inst==10: #WRITESELF
                init_val=rand_cell.genome[rand_cell.self_ptr]
                if random()<=self.mutation_rate: ##mutation probability
                    rand_cell.genome[rand_cell.self_ptr]=randint(0,INST_NUMBER-1)
                else:
                    rand_cell.genome[rand_cell.self_ptr]=rand_cell.register

                rand_cell.color=rand_cell.color+rand_cell.genome[rand_cell.self_ptr]-init_val

            elif inst==11: #READNEIGH

                if permission:
                    if random()<=self.mutation_rate: ##mutation probability
                        rand_cell.register=randint(0,INST_NUMBER-1)
                    else:
                        rand_cell.register=neigh.genome[rand_cell.neigh_ptr]

            elif inst==12: #WRITENEIGH

                if permission:

                    init_val=neigh.genome[rand_cell.neigh_ptr]
                    
                    if random()<=self.mutation_rate: ##mutation probability
                        neigh.genome[rand_cell.neigh_ptr]=randint(0,INST_NUMBER-1)
                    else:
                        neigh.genome[rand_cell.neigh_ptr]=rand_cell.register                        

                    neigh.color=neigh.color+neigh.genome[rand_cell.neigh_ptr]-init_val

                    if [neigh.location_x,neigh.location_y] not in self.not_none:
                        self.not_none.append([neigh.location_x,neigh.location_y])

                    modified=False
                    # check if already modified in current time slot

                    for parent in neigh.list_parents:
        
                        if parent[0]==rand_cell.cell_id and parent[1]==i:
                                modified=True
                                break


                    if modified==False:
                        
                        neigh.add_parent([rand_cell.cell_id,i])
                        modified_cells.append([neigh.location_x,neigh.location_y])
                        neigh.cell_id=self.cell_counter
                        self.cell_counter=self.cell_counter+1

            elif inst==13: #FACE

                rand_cell.facing=rand_cell.register % 4
                permission=self.get_permission_status(rand_cell)
                neigh=self.get_neighbour(rand_cell)

            elif inst==14: #ZEROREG

                rand_cell.register=0

            elif inst==15: #ZEROSELF

                rand_cell.self_ptr=0

            elif inst==16: #ZERONEIGH

                rand_cell.neigh_ptr=0

            elif inst==17: #JUMP past the REP if register=0

                if rand_cell.register==0:

                    stack=[]
                    stack.append(j)

                    k=j+1
                    while k<len(rand_cell.genome):
                        inside_inst=rand_cell.genome[k]
                        if inside_inst==17: ##another Jump
                            stack.append(k)
                        elif inside_inst==18: ## REP
                            stack.pop()
                            if not stack: #empty stack
                                break
                        #elif inside_inst==0: #STOP
                            #stop=True
                            #break
                        k=k+1

                    j=k

            elif inst==18: #REP jumps past JUMP if register!=0

                if rand_cell.register!=0:

                    stack=[]
                    stack.append(j)

                    k=j-1
                    while k>=0:
                        inside_inst=rand_cell.genome[k]
                        if inside_inst==18: ##another REP
                            stack.append(k)
                        elif inside_inst==17: ## JUMP
                            stack.pop()
                            if not stack: #empty stack
                                break
                        k=k-1

                    j=k+1

            elif inst==19: #CMPSELF compares self_ptr instruction with register and returns 0 if equal
                if rand_cell.genome[rand_cell.self_ptr]==rand_cell.register:
                    rand_cell.register=0

            elif inst==20: #CMPNEIGH compares neigh_ptr instruction with register and returns 0 if equal
                if neigh.genome[rand_cell.neigh_ptr]==rand_cell.register:
                    rand_cell.register=0

            j=j+1

        rand_cell.energy=rand_cell.energy+randint(-1*self.variation_energy,1*self.variation_energy)


        if rand_cell.energy<0: rand_cell.energy=0

        if self.dump:
            self.dump_cell(rand_cell,i)

            for location in modified_cells:
                self.dump_cell(self.pond[location[0]][location[1]],i)

        #print rand_cell.genome, rand_cell.register, neigh.genome

    def dump_cell(self,cell,time):

        self.file.write(str(time)+"|"+str(cell.cell_id)+"|"+str(cell.genome)+"|"+str(cell.location_x)+"|"+str(cell.location_y)+"|"+str(cell.list_parents)+"|"+str(cell.energy)+"|"+str(cell.facing)+"|"+str(cell.color)+"\n") 

    def generate_random_genome(self,cell):

        program_length=self.mean_program_length+randint(-1*self.variation_program_length,1*self.variation_program_length)

        for i in range(program_length):
            cell.genome[i]=randint(0,INST_NUMBER-1)
            cell.color=cell.color+cell.genome[i]



    #used to check if permission is there

    def get_permission_status(self,cell):

        perm = False

        neigh=self.get_neighbour(cell)
        
        #check for common parents

        for parent in cell.list_parents:

            if perm==True: break
            
            parent_id = parent[0]

            for j in neigh.list_parents:

                if j[0]==parent_id:
                    perm=True
                    
        
        return (perm or (random() <= self.permission_rate) or (neigh.genome[0]==0) or (neigh.energy==0))



    def get_neighbour(self,cell):

        if cell.facing==0:
        
            return self.pond[cell.location_x][cell.location_y-1]

        elif cell.facing==1:

            return self.pond[(cell.location_x+1)% self.width][cell.location_y]

        elif cell.facing==2:

            return self.pond[cell.location_x][(cell.location_y+1)%self.height]

        else:

            return self.pond[cell.location_x-1][cell.location_y]
        
            
if __name__=="__main__":
    a=Pond(100,100,filename='test.dat')
    a.run(1000)
