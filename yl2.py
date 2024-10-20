# Lisab elemendid stacki
def stack_push(stack): 
    for i in range(5): #Lisab 5 numbrit stacki (0-4)
        stack.append(i) #Lisab iga elemendi loppu
    return stack #Tagastab stacki
  
# Eemaldab yhe elemendi stacki topist
def stack_pop(stack):
    if len(stack) > 0: #kontrollib kas stackis on elemente
        print("Pop :", stack[-1]) #Kuvab virna top elementi
        stack.pop() #Eemaldab stacki top elemendi
    else:
        print("Stack is empty.") #Naitab kui stack on tyhi
    return stack #Tagastab stacki
  
#Naitab stacki top elementi
def stack_peek(stack):
    if len(stack) > 0: #Kontrollib kas on elemente
        element = stack[-1]
        print("Element on stack top:", element) #Kuivab top elemendi
    else:
        print("Stack is empty.") #naitab kui on stack tyhi
  
#Otsib elementi stackist aga ei eemalda seda
def stack_search(stack, element):
    pos = -1 #Hoiab muutuja positsiooni
    #Tsykkel mis laheb stacki topist allapoole
    for i in range(len(stack)-1, -1, -1):
        if stack[i] == element:
            pos = len(stack) - i #Leitakse elemendi positsioon mis lisati viimasena
            break

    if pos == -1:  # Kui elementi ei leitud
        print("Elementi ei leitud")
    else:
        print("Element leiti positsioonil", pos)  # Kuvab leitud elemendi positsiooni

#Teeme tyhja stacki
stack = []
stack_push(stack)  # Push elements into the stack
stack_pop(stack)   # Pop one element from the stack
stack_push(stack)  # Push elements again
stack_peek(stack)  # Peek the top element of the stack
stack_search(stack, 2)  # Search for an element
stack_search(stack, 6)  # Search for a non-existing element
