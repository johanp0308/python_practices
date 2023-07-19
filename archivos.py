ruta = "D:/Workspace/Python/Udemy/miarchivo.pdf"
fd = open(ruta, "w") # w = crea si no existe
                      # a = agrega al final

fd.write("""
========================================
Archivo de Pdf para prueba de agregacion 
dqwdqww
qwdqwdq

qwdqwdqw
qwdqwd
qwdqwd
         """)
# fd.seek(0)
# lectura = fd.readline()
# print(lectura)
fd.close()


ruta = "D:/Workspace/Python/Udemy/miarchivo.pdf"
fd = open(ruta, "w")