# MST Boruvka Algorithm Performance Measurement (Яковлев краш) 

This program measures the performance of Boruvka's algorithm for finding the minimum spanning tree (MST) of a graph. It compares the performance using adjacency list and adjacency matrix representations.

## Table of Contents


1. [Installation](#installation)
2. [Usage](#usage)
3. [Examples](#examples)
4. [File Structure](#file-structure)
5. [Dependencies](#dependencies)
6. [Results](#results)
7. [Authors and License](#authors-and-license)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/MoisieievVasya/Boruvka-algorithm
```
- open the directory
```bash
cd Boruvka-algorithm
```

2. Install the required dependencies:
```bash
pip install pandas networkx matplotlib 
```

## Usage
3. Run the performance measurement script:

```bash
python main.py
```
4. The results will be saved in `by_list.txt` and `by_matrix.txt` files.

If you want to get diagrams of the results, you can run the script :
```bash
python analysis.py
```



## Examples

You can run the performance measurement script with different numbers of vertices and densities. The script will generate a graph and calculate the minimum spanning tree using Boruvka's algorithm. The performance of the algorithm is then measured and the results are saved.





## File Structure

- `main.py.`: Main script to measure the performance.
- `analysis.py`: Script to analyze the results.
- `README.md`: This file.
- `by_list.txt`: Results of performance measurement using adjacency list.
- `by_matrix.txt`: Results of performance measurement using adjacency matrix.

## Dependencies

- Python 3.x
- networkx
- matplotlib
- pandas 


## Results
The results of the performance measurement are saved in by_list.txt and by_matrix.txt files. These files contain the performance of the algorithm for different numbers of vertices and densities. The analysis.py script can be used to visualize these results. 
## Authors and License

This program was written by Moisieiev Vasya and Zahar Staric. It is licensed under the MIT License.
