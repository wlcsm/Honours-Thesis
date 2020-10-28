import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

karatsuba = pd.read_csv("karatsuba.txt", delimiter=' ')
kronecker = pd.read_csv("kronecker.txt", delimiter=' ')
fft = pd.read_csv("fft.txt", delimiter=' ')
schoolbook = pd.read_csv("schoolbook.txt", delimiter=' ')

# The par_iter vs iter
karatsuba.plot(x      = "degree", 
          y      = ["time"],
          kind   = "line", 
          legend = False,
          xlabel = "Degree",  
          ylabel = "Time (μs)", 
          title  = "Karatsuba's Multiplication")

# The par_iter vs iter
schoolbook.plot(x      = "degree", 
          y      = ["1-var", "2-var", "5-var",  "10-var"],
          kind   = "line", 
          xlabel = "Number of non-zero terms",  
          ylabel = "Time (μs)", 
          title  = "Schoolbook Multiplication")

# The benchmarks
kronecker.plot(x      = "degree", 
          y      = ["2-var", "5-var",  "10-var"],
          kind   = "line", 
          xlabel = "Number of non-zero terms",  
          ylabel = "Time (μs)", 
          # rot    = 20,
          title  = "Kronecker Substitution")

fft.plot(x      = "degree", 
          y      = ["time"],
          kind   = "line", 
          legend = False,
          xlabel = "Degree",  
          ylabel = "Time (μs)", 
          # rot    = 20,
          title  = "FFT-based Polynomial Multiplication")

plt.show()

