import numpy as np
import urenderer

# Crie uma cena com três objetos, um filho do outro:
# Objeto0 -> Objeto1 -> Objeto2
#
# Configure as transformações para que todos os objetos sejam visíveis e renderize a cena
#
# Altere a transformação do objeto avô dos outros e renderize a cena.
# Observe como que os objetos filhos se movem juntos

if __name__ == "__main__":
    urenderer.utils.clear_workdir("03-grandchild")
    renderer = urenderer.renderer.PyplotRenderer(1920, 1080)
    runtime = urenderer.application.Runtime(renderer, name="03-grandchild")

    main_cube = urenderer.node.Node()

    main_cube.translation = np.array([0, 0, -5], np.float64)
    main_cube.rotation = np.array([45, 45, 90], np.float64)
    main_cube.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    
    cube_1 = urenderer.node.Node()
    cube_1.translation = np.array([0, 1, 0], np.float64)
    cube_1.rotation = np.array([0, 0, 0], np.float64)
    cube_1.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    
    cube_2 = urenderer.node.Node()

    cube_2.translation = np.array([0, 1, 0], np.float64)
    cube_2.rotation = np.array([0, 0, 0], np.float64)
    cube_2.render_data = urenderer.geometry.polygonal_ifs.get_ifs_cube()
    
    cube_1.add_child(cube_2)
    main_cube.add_child(cube_1)
    runtime.scene.add_child(main_cube)
    # Crie a cena

    runtime.iter(capture=True)
    
    
    main_cube.rotation = np.array([45, 45, 135], np.float64)
    # Rotacione o nó avô

    runtime.iter(capture=True)
