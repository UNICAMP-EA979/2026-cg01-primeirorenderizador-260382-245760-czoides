import numpy as np
import urenderer

# Renderize uma cena em que o algoritmo de oclusão falha
#
# Observe o método urenderer.renderer.pyplot_renderer.PyplotRenderer::end
# Ele desenha a cena utilizando o "algoritmo do pintor" (painter's algorithm)
# para determinar a visibilidade dos triângulos (qual deve estar por cima do outro)
#
# Crie uma cena com dois cubos de forma que o algoritmo do pintor falhe de forma
# visualmente perceptível.

if __name__ == "__main__":
    urenderer.utils.clear_workdir("04-intersection")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="04-intersection")
    
    cube = urenderer.node.Node()

    cube.translation = np.array([0, 0, -5], np.float64)
    cube.rotation = np.array([0, 45, 0], np.float64)
    cube.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    
    runtime.scene.add_child(cube)
    """
       O algoritmo do pintor desenha os triângulos na tela com base
    na ordenação da profundidade média (eixo z) dos vértices de
    cada triângulo.

    Entretanto, no exemplo encontrado pela dupla, observa-se um
    erro de renderização: é possível visualizar a base do cubo
    mesmo estando perfeitamente paralela ao plano horizontal
    x = 0, algo fisicamente impossível.

    Ao analisar os triângulos do cubo em mais detalhe, nota-se
    que o triângulo da base e os triângulos das faces possuem
    exatamente a mesma média de profundidade.

    Dessa forma, torna-se imprevisível determinar qual triângulo
    será desenhado por último na tela. O resultado final passa
    então a depender de fatores como a ordem de declaração dos
    triângulos, erros de ponto flutuante e o algoritmo de
    ordenação utilizado.

    Além disso, esse comportamento evidencia uma das limitações
    clássicas do algoritmo do pintor, que pode falhar em
    situações de sobreposição ou empate de profundidade entre
    polígonos.


            
    """
    
    
    runtime.iter(capture=True)
