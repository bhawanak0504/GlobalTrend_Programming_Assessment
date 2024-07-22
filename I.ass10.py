def transpose_matrix(matrix):
   
    rows = len(matrix)
    cols = len(matrix[0]) 
    
    
    transpose = [[0 for _ in range(rows)] for _ in range(cols)]
    
    
    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]
    
    return transpose


def get_matrix_from_input():
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        
        matrix = []
        print("Enter the elements row-wise:")
        for i in range(rows):
            row = []
            for j in range(cols):
                element = int(input(f"Enter element [{i}][{j}]: "))
                row.append(element)
            matrix.append(row)
        
        return matrix
    
    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return None


matrix = get_matrix_from_input()
if matrix:
    print("Original Matrix:")
    for row in matrix:
        print(row)
    
    transposed_matrix = transpose_matrix(matrix)
    print("\nTransposed Matrix:")
    for row in transposed_matrix:
        print(row)