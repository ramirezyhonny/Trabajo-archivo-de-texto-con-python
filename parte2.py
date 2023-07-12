import re
from collections import Counter
opt=0;
while opt!=5:
    print("MENÚ DE OPCIONES");
    print("1- Mostrar el total de palabras del archivo txt.");
    print("2- Calcular cantidad de ocurrencias de cada palabra. Mostrar de Mayor a menor.");
    print("3- Eliminar artículos, conjunciones, preposiciones, adverbios, y signos de puntuación. Mostrar en un nuevo archivo");
    print("4- Mostrar las 10 palabras con mayor frecuencia en  nuevo texto.");
    print("5- Finalizar");
    opt=int(input("Ingrese la taréa a realizar: "));
    if opt==1:
        with open("texto.txt","r")as archivo:
            cont=archivo.read();
            palabras=cont.split();
            cant_pal=len(palabras);
            print(f"Palabras: {cant_pal}");
    elif opt==2:
        with open("texto.txt","r") as archivo:
            cont=archivo.read();
            palabras=cont.split();
            contar={};
            for palabra in palabras:
                contar[palabra]=contar.get(palabra, 0)+1;
        orden=sorted(contar, key=contar.get, reverse=True);
        for palabra in orden:
            print(f"Palabra: {palabra} => Ocurrencia: {contar[palabra]}");
    elif opt==3:
        with open("texto.txt","r") as archivo:
            textoOriginal=archivo.read();
        elimPals=['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas',
                 'y', 'o', 'pero', 'porque', 'a', 'ante', 'bajo', 'con', 'de',
                 'desde', 'en', 'entre', 'hacia', 'hasta', 'para', 'por', 'según',
                 'sin', 'sobre', 'tras', 'además', 'también', 'mientras', 'aunque',
                 'si', 'no', 'sí', 'quizás', 'quizá', 'talvez', 'tal vez',
                 'El', 'La', 'Los', 'Las', 'Un', 'Una', 'Unos', 'Unas',
                 'Y', 'O', 'Pero', 'Porque', 'A', 'Ante', 'Bajo', 'Con', 'De',
                 'Desde', 'En', 'Entre', 'Hacia', 'Hasta', 'Para', 'Por', 'Según',
                 'Sin', 'Sobre', 'Tras', 'Además', 'También', 'Mientras', 'Aunque',
                 'Si', 'No', 'Sí', 'Quizás', 'Quizá', 'Talvez', 'Tal Vez',
                 'asimismo', 'tampoco', 'así', 'entonces', 'entretanto', 'por consiguiente',
                 'no obstante', 'sin embargo', 'por otro lado', 'por lo tanto', 'por ende',
                 'además', 'en conclusión', 'en resumen', 'en cambio', 'en suma'];
        limpiarTexto=re.sub(r"[^\w\s]", "", textoOriginal);
        limpiarTexto.lower();
        palabras=limpiarTexto.split();
        buscarPals=[palabra for palabra in palabras if palabra not in elimPals]
        textoLimpio=" ".join(buscarPals);
        archivoLimpio="archivoLimpio.txt";
        with open("archivoLimpio", "w") as archivo2:
            archivo2.write(textoLimpio);
        print(f"Se creó el nuevo archivo: ({archivoLimpio}) con texto limpio.");
    elif opt==4:
        with open("archivoLimpio","r") as archivo:
            cont=archivo.read();
        palabras=cont.split();
        frecuencia=Counter(palabras);
        primeros10=frecuencia.most_common(10);
        for palabra,ocurrencia in primeros10:
            print(f"Palabra: {palabra}=> Ocurrencia: {ocurrencia}"); 
    elif opt==5:
        print("FIN DEL PROGRAMA. Gracias👌")
        break;
    else:
        print("Opción inválida. INTENTE NUEVAMENTE");
