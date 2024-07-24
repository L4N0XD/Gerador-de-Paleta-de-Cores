# Gerador de Paleta de Cores

Este script em Python utiliza a biblioteca `matplotlib` para gerar uma paleta de cores a partir de uma cor base especificada.

## Funcionamento

1. **Função `generate_palette`**:
   - **Entrada**: Recebe uma cor base em formato hexadecimal (`base_color`) e o número de cores desejadas na paleta (`num_colors`).
   - **Processo**: Converte a cor base para o formato RGB utilizando `mcolors.hex2color`, e define a cor preta como outra referência.
   - **Saída**: Calcula uma paleta de cores variando suavemente entre a cor base e o preto. Cada cor na paleta é calculada como uma mistura linear entre a cor base e o preto, ajustada pela posição na sequência de cores.

2. **Visualização da Paleta**:
   - A função gera uma lista de cores em formato hexadecimal utilizando `mcolors.to_hex`.
   - Em seguida, converte essas cores para o formato RGB para visualização com `mcolors.hex2color`.

3. **Plotagem da Paleta**:
   - Utiliza `matplotlib` para criar um gráfico de imagem (`imshow`) que mostra a paleta de cores gerada.
   - Configura o subplot para não exibir ticks nos eixos (`xticks=[], yticks=[]`) e sem moldura (`frame_on=False`).
   - A imagem é exibida com uma relação de aspecto automática (`aspect='auto'`).

4. **Saída de Dados**:
   - Para cada cor na paleta, é impresso um índice numerado e a cor correspondente.

