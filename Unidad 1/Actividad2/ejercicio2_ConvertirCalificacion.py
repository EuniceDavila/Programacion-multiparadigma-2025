print("Conversión de calificación numérica a letra")
calificacion = int(input("Ingresa tu calificación (0-100): "))


if (calificacion>=90) and (calificacion<=100):
    letra = "A"
elif (calificacion>=80) and (calificacion<=89):
    letra = "B"
elif (calificacion>=70) and (calificacion<=79):
    letra = "C"
elif (calificacion>=60) and (calificacion<=69):
    letra = "D"
elif (calificacion>=0) and (calificacion<=59):
    letra = "F"
else:
    letra = "Calificación inválida"

print(f"Tu calificación en letra es: {letra}")