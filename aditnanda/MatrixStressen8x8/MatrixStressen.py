from multiprocessing import Process, Pipe
import numpy as np

class MatrixStressen:

    # mendefinisikan matrix x dan y
    global x,y,n

    # matrix 8x8
    x = np.array(
        [[5, 1, 2, 0, 7, 8, 2, 1],
         [2, 3, 0, 2, 0, 4, 1, 3],
         [4, 5, 7, 1, 5, 2, 31, 1],
         [2, 0, 1, 3, 2, 4, 1, 5],
         [2, 4, 2, 1, 1, 2, 3, 4],
         [2, 5, 7, 3, 5, 2, 1, 0],
         [1, 0, 2, 3, 0, 2, 4, 1],
         [4, 0, 5, 1, 3, 7, 4, 2]])
    y = np.array(
        [[5, 1, 2, 0, 7, 8, 2, 1],
         [2, 3, 0, 2, 0, 4, 1, 3],
         [4, 5, 7, 1, 5, 2, 31, 1],
         [2, 0, 1, 3, 2, 4, 1, 5],
         [2, 4, 2, 1, 1, 2, 3, 4],
         [2, 5, 7, 3, 5, 2, 1, 0],
         [1, 0, 2, 3, 0, 2, 4, 1],
         [4, 0, 5, 1, 3, 7, 4, 2]])

    n = len(x)

    def partMatrix(self):
        part = int(n/2)

        a = x[:part, :part]
        b = x[:part, part:]
        c = x[part:, :part]
        d = x[part:, part:]
        e = y[:part, :part]
        f = y[:part, part:]
        g = y[part:, :part]
        h = y[part:, part:]
        return [a, b, c, d, e, f, g, h]

    def multiply(self, x, y):
        result = np.zeros([len(x), len(y)], dtype=int)

        for i in range(len(x)):
            for j in range(len(y[0])):
                for k in range(len(y)):
                    result[i][j] += x[i][k] * y[k][j]
        return result

    def add(self, x, y):
        result = np.zeros([len(x), len(y)], dtype=int)

        for i in range(len(x)):
            for j in range(len(x[0])): result[i][j] = x[i][j] + y[i][j]
        return result

    def subtract(self, x, y):
        result = np.zeros([len(x), len(y)], dtype=int)

        for i in range(len(x)):
            for j in range(len(x[0])): result[i][j] = x[i][j] - y[i][j]
        return result

    def matrixMl(self, connect, a, c, e, f):
        m1 = self.multiply(self.add(a, c), self.add(e, f))
        connect.send(m1)
        connect.close

    def matrixM2(self, connect, b, d, g, h):
        m2 = self.multiply(self.add(b, d), self.add(g, h))
        connect.send(m2)
        connect.close

    def matrixM3(self, connect, a, d, e, h):
        m3 = self.multiply(self.subtract(a, d), self.add(e, h))
        connect.send(m3)
        connect.close

    def matrixM4(self, connect, a, f, h):
        m4 = self.multiply(a, self.subtract(f, h))
        connect.send(m4)
        connect.close

    def matrixM5(self, connect, c, d, e):
        m5 = self.multiply(self.add(c, d), e)
        connect.send(m5)
        connect.close

    def matrixM6(self, connect, a, b, h):
        m6 = self.multiply(self.add(a, b), h)
        connect.send(m6)
        connect.close

    def matrixM7(self, connect, d, g, e):
        m7 = self.multiply(d, self.subtract(g, e))
        connect.send(m7)
        connect.close

    def mergeMatrix(self, ml, m2, m3, m4, m5, m6, m7):
        M1 = ml.recv()
        M2 = m2.recv()
        M3 = m3.recv()
        M4 = m4.recv()
        M5 = m5.recv()
        M6 = m6.recv()
        M7 = m7.recv()
        i = self.subtract(self.subtract(self.add(M2, M3), M6), M7)
        j = self.add(M4, M6)
        k = self.add(M5, M7)
        l = self.subtract(self.subtract(self.subtract(M1, M3), M4), M5)
        iMergeK = np.concatenate((i, k))
        jMergeL = np.concatenate((j, l))
        matrixAll = np.concatenate((iMergeK, jMergeL), axis=1)
        print(matrixAll)

    def main(self):
        matrix = self.partMatrix()

        M1IN, M1OUT = Pipe()
        M2IN, M2OUT = Pipe()
        M3IN, M3OUT = Pipe()
        M4IN, M4OUT = Pipe()
        M5IN, M5OUT = Pipe()
        M6IN, M6OUT = Pipe()
        M7IN, M7OUT = Pipe()

        ProsesM1 = Process(target=self.matrixMl, args=(M1IN, matrix[0], matrix[2], matrix[4], matrix[5],))
        ProsesM2 = Process(target=self.matrixM2, args=(M2IN, matrix[1], matrix[3], matrix[6], matrix[7],))
        ProsesM3 = Process(target=self.matrixM3, args=(M3IN, matrix[0], matrix[3], matrix[4], matrix[7],))
        ProsesM4 = Process(target=self.matrixM4, args=(M4IN, matrix[0], matrix[5], matrix[7],))
        ProsesM5 = Process(target=self.matrixM5, args=(M5IN, matrix[2], matrix[3], matrix[4],))
        ProsesM6 = Process(target=self.matrixM6, args=(M6IN, matrix[0], matrix[1], matrix[7],))
        ProsesM7 = Process(target=self.matrixM7, args=(M7IN, matrix[3], matrix[6], matrix[4],))
        ProsesMerge = Process(target=self.mergeMatrix, args=(M1OUT, M2OUT, M3OUT, M4OUT, M5OUT, M6OUT, M7OUT,))

        ProsesM1.start()
        ProsesM2.start()
        ProsesM3.start()
        ProsesM4.start()
        ProsesM5.start()
        ProsesM6.start()
        ProsesM7.start()
        ProsesMerge.start()

        ProsesM1.join()
        ProsesM2.join()
        ProsesM3.join()
        ProsesM4.join()
        ProsesM5.join()
        ProsesM6.join()
        ProsesM7.join()
        ProsesMerge.join()

if __name__ == '__main__':
    # start_time = time.time()
    MatrixStressen().main()
    # print("\n\n--- %s seconds ---" % (time.time() - start_time))




