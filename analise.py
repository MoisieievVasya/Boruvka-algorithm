import pandas as pd
import matplotlib.pyplot as plt

def read_file_to_df(filename):
    df = pd.read_csv(filename, sep=' ', header=None)
    df.columns = ['Density', 'Vertices', 'Time', 'MST Weight']
    return df
def analise():
    df_list = read_file_to_df('output_files/by_list_raw.txt')
    df_matrix = read_file_to_df('output_files/by_matrix_raw.txt')

    # Calculate average time for each number of vertices
    avg_time_list = df_list.groupby('Vertices')['Time'].mean()
    avg_time_matrix = df_matrix.groupby('Vertices')['Time'].mean()

    # Group by density and vertices
    grouped_list = df_list.groupby(['Density', 'Vertices'])['Time'].mean()
    grouped_matrix = df_matrix.groupby(['Density', 'Vertices'])['Time'].mean()

    densities = df_list['Density'].unique()

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(avg_time_list, label='List')
    plt.plot(avg_time_matrix, label='Matrix')
    plt.xlabel('Number of Vertices')
    plt.ylabel('Average Time')
    plt.title('Average Time for Each Number of Vertices')
    plt.legend()
    plt.show()


    for density in densities:
        plt.figure(figsize=(10, 6))
        plt.plot(grouped_list[density], label='List')
        plt.plot(grouped_matrix[density], label='Matrix')
        plt.xlabel('Number of Vertices')
        plt.ylabel('Average Time')
        plt.title(f'Density: {density}')
        plt.legend()
        plt.show()