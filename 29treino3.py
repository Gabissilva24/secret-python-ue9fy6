#3. Faça um Programa que leia três números inteiros e mostre o maior deles.

primeiro: int
segundo: int
terceiro: int
maior = int


primeiro = int(input('Digite o primeiro número: '))
segundo = int(input('Digite o segundo número: '))
terceiro = int(input('Digite o terceiro número: '))
maior = primeiro

if segundo > maior:
  maior = segundo
if terceiro > maior:
  maior = terceiro

print('O maior núemro é: ', maior)

if primeiro>segundo and primeiro>terceiro:
  print('primeiro é maior que segundo e terceiro: ')
elif segundo>primeiro and segundo>terceiro:
  print('segundo é maior que primeiro e terceiro: ')
else:
  print('terceiro é maior que primeiro e segundo: ')