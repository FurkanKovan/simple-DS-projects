import numpy as np


def calculate(my_list):
    matrix = my_list
    # Converting list to 3,3 matrix
    try:
        matrix = np.array(my_list).reshape(3, 3)
    except ValueError:
        print("List must contain nine numbers.")
        exit()

    # Assigning the column and row values to axes
    axis1 = []
    axis2 = []
    flattened = []
    for i in range(matrix.shape[1]):
        axis1.append(matrix[:, i].tolist())
        axis2.append(matrix[i, :].tolist())

    # Creating the calculations dictionary
    calculations = {
        'mean': [axis1, axis2, flattened],
        'variance': [axis1, axis2, flattened],
        'standard deviation': [axis1, axis2, flattened],
        'max': [axis1, axis2, flattened],
        'min': [axis1, axis2, flattened],
        'sum': [axis1, axis2, flattened],
    }

    # Calculating the wanted values and writing them to the dictionary
    calculations['mean'][0] = [np.average(axis1[0]), np.average(axis1[1]), np.average(axis1[2])]
    calculations['mean'][1] = [np.average(axis2[0]), np.average(axis2[1]), np.average(axis2[2])]
    calculations['mean'][2] = np.average([axis1, axis2])

    calculations['variance'][0] = [np.var(axis1[0]), np.var(axis1[1]), np.var(axis1[2])]
    calculations['variance'][1] = [np.var(axis2[0]), np.var(axis2[1]), np.var(axis2[2])]
    calculations['variance'][2] = np.var([axis1, axis2])

    calculations['standard deviation'][0] = [np.std(axis1[0]), np.std(axis1[1]), np.std(axis1[2])]
    calculations['standard deviation'][1] = [np.std(axis2[0]), np.std(axis2[1]), np.std(axis2[2])]
    calculations['standard deviation'][2] = np.std([axis1, axis2])

    calculations['max'][0] = [np.max(axis1[0]), np.max(axis1[1]), np.max(axis1[2])]
    calculations['max'][1] = [np.max(axis2[0]), np.max(axis2[1]), np.max(axis2[2])]
    calculations['max'][2] = np.max([axis1, axis2])

    calculations['min'][0] = [np.min(axis1[0]), np.min(axis1[1]), np.min(axis1[2])]
    calculations['min'][1] = [np.min(axis2[0]), np.min(axis2[1]), np.min(axis2[2])]
    calculations['min'][2] = np.min([axis1, axis2])

    calculations['sum'][0] = [np.sum(axis1[0]), np.sum(axis1[1]), np.sum(axis1[2])]
    calculations['sum'][1] = [np.sum(axis2[0]), np.sum(axis2[1]), np.sum(axis2[2])]
    calculations['sum'][2] = np.max([np.sum(calculations['sum'][0]), np.sum(calculations['sum'][1])])

    return calculations


if __name__ == '__main__':
    print(calculate([0, 1, 2, 3, 4, 5, 6, 7, 8]))
    print("\n")
    print(calculate([0, 1, 3, 5]))
