"""
sent_message = 'este es un mensaje que jamas deberia salir de aqui.'

with open('sent_message.txt', 'w') as file:
  file.write(sent_message)
documento=open("sent_message.txt","r")
print(documento.read())"""
with open('sent_message.txt', 'r+') as file: #abrir archivo en modo lectura y escritura
  # Read the sent message from the file 
  original_message = file.read() 
      
  # Move the cursor to the beginning of the file
  file.seek(0)
  # Modify the message to simulate unsending
  unsent_message = 'This message has been unsent.'
  file.truncate() #borra el contenido del archivo
  file.write(unsent_message) #escribe el nuevo mensaje
  file.seek(0) #mueve el cursor al inicio del archivo
  print(f"ahora mensaje es {file.read()} ") #imprime el nuevo mensaje