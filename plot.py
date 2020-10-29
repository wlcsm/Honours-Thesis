import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

karatsuba = pd.read_csv("karatsuba.txt", delimiter=' ')
kronecker = pd.read_csv("kronecker.txt", delimiter=' ')
fft = pd.read_csv("fft.txt", delimiter=' ')
schoolbook = pd.read_csv("schoolbook.txt", delimiter=' ')

karatsuba.plot(x      = "degree", 
          y      = ["time"],
          kind   = "line", 
          legend = False,
          xlabel = "Degree",  
          ylabel = "Time (s)", 
          title  = "Karatsuba Multiplication")

schoolbook.plot(x      = "degree", 
          y      = ["1-var", "2-var", "5-var",  "10-var"],
          kind   = "line", 
          xlabel = "Number of non-zero terms",  
          ylabel = "Time (s)", 
          title  = "Schoolbook Multiplication")

kronecker.plot(x      = "degree", 
          y      = ["2-var", "5-var",  "10-var"],
          kind   = "line", 
          xlabel = "Number of non-zero terms",  
          ylabel = "Time (s)", 
          title  = "Kronecker Substitution")

fft.plot(x      = "degree", 
          y      = ["time"],
          kind   = "line", 
          legend = False,
          # logx = True,
          xlabel = "Degree",  
          ylabel = "Time (s)", 
          title  = "FFT-based Multiplication")

plt.show()

