from pyscript import document,display


elements = {"H":("Hydrogen",1, 1.008,) , #Getting 11/17 elements
           
           "He":("Helium",2, 4.0026,),
           
           "C":("Carbon",6, 12.011,), 
           
           "N":("Nitrogen",7, 14.007,), 
           
           "O":("Oxygen",8, 15.999,) , 

           "F":("Fluorine",9, 18.998,) , 

           "Ne":("Neon",10, 20.180,), 

           "P":("Phosphorus",15, 30.974,), 

           "S":("Sulfur",16, 32.06,), 

           "Ar":("Argon",18, 39.948,),

           "Se":("Selenium",34, 78.971,),}

    #Element name, order from the sun, number of moonss

def search_element(e):
    Element1 = document.getElementById("element1").value #adding a value to the ID
    result = elements.get(Element1, ("Element not found", "-","-")) #creating failsafe if input does not exist also giving value to Element1

    document.getElementById("code").innerText = Element1 #calling Element1
    document.getElementById("ElementName").innerText = result[0]
    document.getElementById("AtomicNumber").innerText = result[1]   #calling 3 aspects with their values
    document.getElementById("AtomicMass").innerText = result[2] 





