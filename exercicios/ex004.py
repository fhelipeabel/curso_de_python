entrada = input("Digite o que quiser: ")

# Verificação do tipo de dado básico
print("Tipo primitivo:\n", type(entrada))

# Verificação de Caracteres e Alfabeto
print("Todos são alfanuméricos e têm pelo menos 1 caráctere:\n", entrada.isalnum())
print("Todos são letras do alfabeto:\n", entrada.isalpha())
print("Todos fazem parte da tabela ASCII:\n", entrada.isascii())

# Verificação de Números
print("Todos são números decimais:\n", entrada.isdecimal())
print("Todos são dígitos sem especiais, espaços ou vazios:\n", entrada.isdigit())
print("Todos são numéricos (frações/romanos/numeros/unicode/etc):\n", entrada.isnumeric())

# Verificação de Maiúsculas e Minúsculas
print("Todas as letras são maiúsculas:\n", entrada.isupper())
print("Todas as letras são minúsculas:\n", entrada.islower())
print("Todas iniciais maiúsculas:\n", entrada.istitle())

# Outras validações
print("Tem espaço em branco/tabulação/quebra de linha:\n", entrada.isspace())
print("Tem apenas carácteres imprimíveis:\n", entrada.isprintable())
print("Serve para ser um identificador:\n", entrada.isidentifier())