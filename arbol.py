import os

class node():
    def __init__(self, dato):
        self.left = None
        self.right = None
        self.dato = dato

class arbol():
    def __init__(self):
        self.root = None


    def findMax(self,a):
        if(a is None):
            return float('-inf') 
        elif a.right==None:
            print(a.dato)
            return a.dato
        else:
            return self.findMax(a.right)
            
    def findMin(self,a):
       if(a is None):
            return float('-inf') 
       elif a.left==None:
            print(a.dato)
            return a.dato
       else:
            return self.findMax(a.left)
          
    def insert(self, a, dato):
        if a == None:
            a = node(dato)
        else:
            d = a.dato
            if dato < d:
                a.left = self.insert(a.left, dato)
            else:
                a.right = self.insert(a.right, dato)
        return a




    
    def deleteNode(self,a, dato): 
  

        if a is None: 
            return self.root  
      

        if dato < a.dato: 
            a.left = self.deleteNode(a.left, dato) 
      
     
        elif(dato > a.dato): 
            a.right = self.deleteNode(a.right, dato) 
      
      
        else: 

            if a.left is None : 
                temp = a.right  
                a = None 
                return temp  
                  
            elif a.right is None : 
                temp = a.left  
                a = None
                return temp 
      
            
            temp = self.findMin(a.right) 
      

            a.dato = temp.dato 
      
            
            a.right = self.deleteNode(a.right , temp.dato) 
      
      
        return a







    def inorder(self, a):
        if a == None:
            return None
        else:
            self.inorder(a.left)
            print(a.dato)
            self.inorder(a.right)

    def preorder(self, a):
        if a == None:
            return None
        else:
            print(a.dato)
            self.preorder(a.left)
            self.preorder(a.right)

    def postorder(self, a):
        if a == None:
            return None
        else:
            self.postorder(a.left)
            self.postorder(a.right)
            print(a.dato)

    def buscar(self, dato, a):
        if a == None:
            return None
        else:
            if dato == a.dato:
                return a.dato
            else:
                if dato < a.dato:
                    return self.buscar(dato, a.left)
                else:
                    return self.buscar(dato, a.right)
        
       

tree = arbol()

while True:
    os.system("cls")
    print("Arbol ABB")
    opc = input("\n1.-Insertar nodo \n2.-Inorden \n3.-Preorden \n4.-Postorden \n5.-Buscar \n6.-Buscar Maximo \n7.-Buscar Minimo \n8.-Eliminar Nodo \n9.-Salir \n\nElige una opcion -> ")

    if opc == '1':
        nodo = input("\nIngresa el nodo -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            tree.root = tree.insert(tree.root, nodo)
        else:
            print("\nIngresa solo digitos...")
    elif opc == '2':
        if tree.root == None:
            print("Vacio")
        else:
            tree.inorder(tree.root)
    elif opc == '3':
        if tree.root == None:
            print("Vacio")
        else:
            tree.preorder(tree.root)
    elif opc == '4':
        if tree.root == None:
            print("Vacio")
        else:
            tree.postorder(tree.root)
    elif opc == '5':
        nodo = input("\nIngresa el nodo a buscar -> ")
        if nodo.isdigit():
            nodo = int(nodo)
            if tree.buscar(nodo, tree.root) == None:
                print("\nNodo no encontrado")
            else:
                print("\nNodo encontrado -> ",tree.buscar(nodo, tree.root))
        else:
            print("\nIngresa solo digitos...")
            tree.postorder(tree.root)
    elif opc == '6':
        print("El numero mayor es")
        tree.findMax(tree.root)
    elif opc == '7':
        print("El numero menor es")
        tree.findMin(tree.root)
    elif opc == '8':
       nodo = input("\nIngresa el nodo a eliminar -> ")
       if nodo.isdigit():
            nodo = int(nodo)
            tree.deleteNode(tree.root, nodo)
    elif opc == '9':
        print("\nElegiste salir...\n")
        os.system("pause")
        break
    else:
        print("\nElige una opcion correcta...")
    print()
    os.system("pause")

print()
