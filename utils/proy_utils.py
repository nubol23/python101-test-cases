import cv2
import matplotlib.pyplot as plt

def mostrar_imagen(file_path):
    img = cv2.cvtColor( cv2.imread(file_path), cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    plt.axis('off')
    plt.show()
    
def mostrar_recommendaciones(query_dish, recommendations):
    query_image = 'static/renamed_images/'+ '_'.join(query_dish.split()).lower() + '.png'
    print(query_dish)
    mostrar_imagen(query_image)

    print('Recomendados:')
    print('_'*50)
    print()
    for recommendation in recommendations:
        recommendation_image = 'static/renamed_images/'+ '_'.join(recommendation.split()).lower() + '.png'
        print(recommendation)
        mostrar_imagen(recommendation_image)
