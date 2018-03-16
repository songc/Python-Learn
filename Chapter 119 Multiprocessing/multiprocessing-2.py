from multiprocessing import Pool
def cube(x):
    return x ** 3
if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(cube,[1,2,3]))